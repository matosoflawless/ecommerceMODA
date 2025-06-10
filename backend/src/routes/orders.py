from flask import Blueprint, jsonify, request
from src.models.ecommerce import Order, OrderItem, Product
from src.models.user import db, User
import time
import random

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['POST'])
def create_order():
    """Criar uma nova encomenda"""
    try:
        data = request.get_json()
        
        # Validar dados obrigatórios
        required_fields = ['email', 'first_name', 'last_name', 'phone', 'address', 
                          'city', 'postal_code', 'payment_method', 'items']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Campo obrigatório: {field}'}), 400

        # Validar itens
        if not data['items'] or len(data['items']) == 0:
            return jsonify({'error': 'Carrinho vazio'}), 400

        # Calcular total
        total_amount = 0
        order_items = []
        
        for item in data['items']:
            product = Product.query.get(item['id'])
            if not product:
                return jsonify({'error': f'Produto não encontrado: {item["id"]}'}), 404
            
            if product.stock < item['quantity']:
                return jsonify({'error': f'Stock insuficiente para {product.name}'}), 400
            
            item_total = product.price * item['quantity']
            total_amount += item_total
            
            order_items.append({
                'product_id': product.id,
                'quantity': item['quantity'],
                'price': product.price
            })

        # Adicionar IVA (23%)
        total_amount *= 1.23

        # Criar utilizador se não existir
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            user = User(
                username=data['email'].split('@')[0],
                email=data['email']
            )
            db.session.add(user)
            db.session.flush()  # Para obter o ID

        # Criar encomenda
        order = Order(
            user_id=user.id,
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone=data['phone'],
            address=data['address'],
            city=data['city'],
            postal_code=data['postal_code'],
            payment_method=data['payment_method'],
            mbway_phone=data.get('mbway_phone'),
            total_amount=total_amount,
            status='pending'
        )
        
        db.session.add(order)
        db.session.flush()  # Para obter o ID da encomenda

        # Criar itens da encomenda
        for item_data in order_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item_data['product_id'],
                quantity=item_data['quantity'],
                price=item_data['price']
            )
            db.session.add(order_item)

        db.session.commit()

        return jsonify({
            'order_id': order.id,
            'total_amount': total_amount,
            'status': 'created',
            'message': 'Encomenda criada com sucesso'
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@orders_bp.route('/orders/<int:order_id>/payment', methods=['POST'])
def process_payment(order_id):
    """Processar pagamento de uma encomenda"""
    try:
        order = Order.query.get_or_404(order_id)
        
        if order.status != 'pending':
            return jsonify({'error': 'Encomenda já processada'}), 400

        # Simular processamento de pagamento
        # Em produção, aqui seria feita a integração com o gateway de pagamento
        time.sleep(2)  # Simular tempo de processamento
        
        # Simular sucesso/falha (95% sucesso)
        if random.random() < 0.95:
            order.status = 'paid'
            
            # Atualizar stock dos produtos
            for item in order.items:
                product = Product.query.get(item.product_id)
                if product:
                    product.stock -= item.quantity
            
            db.session.commit()
            
            return jsonify({
                'status': 'success',
                'order_id': order.id,
                'message': 'Pagamento processado com sucesso'
            })
        else:
            order.status = 'failed'
            db.session.commit()
            
            return jsonify({
                'status': 'failed',
                'order_id': order.id,
                'message': 'Falha no processamento do pagamento'
            }), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@orders_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Obter detalhes de uma encomenda"""
    try:
        order = Order.query.get_or_404(order_id)
        return jsonify(order.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@orders_bp.route('/orders/user/<string:email>', methods=['GET'])
def get_user_orders(email):
    """Obter encomendas de um utilizador"""
    try:
        orders = Order.query.filter_by(email=email).order_by(Order.created_at.desc()).all()
        return jsonify([order.to_dict() for order in orders])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

