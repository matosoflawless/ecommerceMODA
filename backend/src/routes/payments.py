from flask import Blueprint, jsonify, request
from src.models.ecommerce import Order, OrderItem, Product
from src.models.user import db, User
from src.services.mbway_service import MBWayService
import time
import random

payments_bp = Blueprint('payments', __name__)
mbway_service = MBWayService()

@payments_bp.route('/payments/mbway/request', methods=['POST'])
def create_mbway_payment():
    """Criar pedido de pagamento MBWay"""
    try:
        data = request.get_json()
        
        # Validar dados obrigatórios
        required_fields = ['order_id', 'phone_number']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Campo obrigatório: {field}'}), 400
        
        order_id = data['order_id']
        phone_number = data['phone_number']
        
        # Verificar se a encomenda existe
        order = Order.query.get(order_id)
        if not order:
            return jsonify({'error': 'Encomenda não encontrada'}), 404
        
        if order.status != 'pending':
            return jsonify({'error': 'Encomenda já processada'}), 400
        
        # Validar número de telemóvel
        if not mbway_service.validate_phone_number(phone_number):
            return jsonify({'error': 'Número de telemóvel inválido'}), 400
        
        # Formatar número de telemóvel
        formatted_phone = mbway_service.format_phone_number(phone_number)
        
        # Criar pedido de pagamento MBWay
        payment_result = mbway_service.create_payment_request(
            formatted_phone, 
            order.total_amount, 
            order_id
        )
        
        if payment_result['status'] == 'success':
            # Atualizar encomenda com dados do pagamento
            order.mbway_phone = formatted_phone
            order.status = 'payment_requested'
            db.session.commit()
            
            return jsonify({
                'status': 'success',
                'request_id': payment_result['request_id'],
                'message': payment_result['message'],
                'expires_at': payment_result['expires_at']
            })
        else:
            return jsonify({
                'status': 'error',
                'message': payment_result['message']
            }), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@payments_bp.route('/payments/mbway/status/<string:request_id>', methods=['GET'])
def check_mbway_payment_status(request_id):
    """Verificar estado do pagamento MBWay"""
    try:
        order_id = request.args.get('order_id')
        if not order_id:
            return jsonify({'error': 'order_id é obrigatório'}), 400
        
        # Verificar estado do pagamento
        status_result = mbway_service.check_payment_status(request_id, order_id)
        
        if status_result['status'] in ['paid', 'rejected', 'expired']:
            # Atualizar estado da encomenda
            order = Order.query.get(order_id)
            if order:
                if status_result['status'] == 'paid':
                    order.status = 'paid'
                    
                    # Atualizar stock dos produtos
                    for item in order.items:
                        product = Product.query.get(item.product_id)
                        if product and product.stock >= item.quantity:
                            product.stock -= item.quantity
                    
                elif status_result['status'] in ['rejected', 'expired']:
                    order.status = 'failed'
                
                db.session.commit()
        
        return jsonify(status_result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@payments_bp.route('/payments/mbway/simulate', methods=['POST'])
def simulate_mbway_payment():
    """Simular pagamento MBWay para demonstração"""
    try:
        data = request.get_json()
        order_id = data.get('order_id')
        action = data.get('action', 'approve')  # approve, reject, expire
        
        if not order_id:
            return jsonify({'error': 'order_id é obrigatório'}), 400
        
        order = Order.query.get(order_id)
        if not order:
            return jsonify({'error': 'Encomenda não encontrada'}), 404
        
        # Simular tempo de processamento
        time.sleep(2)
        
        if action == 'approve':
            order.status = 'paid'
            
            # Atualizar stock dos produtos
            for item in order.items:
                product = Product.query.get(item.product_id)
                if product and product.stock >= item.quantity:
                    product.stock -= item.quantity
            
            message = 'Pagamento aprovado com sucesso'
            
        elif action == 'reject':
            order.status = 'failed'
            message = 'Pagamento rejeitado pelo cliente'
            
        else:  # expire
            order.status = 'failed'
            message = 'Pedido de pagamento expirou'
        
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'order_status': order.status,
            'message': message
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@payments_bp.route('/payments/methods', methods=['GET'])
def get_payment_methods():
    """Obter métodos de pagamento disponíveis"""
    return jsonify({
        'methods': [
            {
                'id': 'mbway',
                'name': 'MBWay',
                'description': 'Pagamento via telemóvel',
                'icon': 'smartphone',
                'enabled': True,
                'fees': 0.0
            },
            {
                'id': 'multibanco',
                'name': 'Multibanco',
                'description': 'Referência Multibanco',
                'icon': 'building',
                'enabled': True,
                'fees': 0.0
            },
            {
                'id': 'card',
                'name': 'Cartão de Crédito/Débito',
                'description': 'Visa, Mastercard',
                'icon': 'credit-card',
                'enabled': True,
                'fees': 0.0
            }
        ]
    })

@payments_bp.route('/payments/validate-phone', methods=['POST'])
def validate_phone_number():
    """Validar número de telemóvel para MBWay"""
    try:
        data = request.get_json()
        phone_number = data.get('phone_number')
        
        if not phone_number:
            return jsonify({'error': 'Número de telemóvel é obrigatório'}), 400
        
        is_valid = mbway_service.validate_phone_number(phone_number)
        formatted_phone = mbway_service.format_phone_number(phone_number) if is_valid else None
        
        return jsonify({
            'valid': is_valid,
            'formatted': formatted_phone,
            'message': 'Número válido' if is_valid else 'Número de telemóvel inválido'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

