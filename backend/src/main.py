import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import json

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Configurar CORS para permitir requests do frontend
CORS(app, origins=['*'])

# Dados de exemplo para produtos
SAMPLE_PRODUCTS = [
    {
        'id': 1,
        'name': 'Smartphone Premium',
        'description': 'Smartphone de última geração com câmara profissional',
        'price': 599.99,
        'original_price': 699.99,
        'image_url': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=400&fit=crop',
        'category': 'Tecnologia',
        'rating': 4.8,
        'reviews_count': 124,
        'stock': 50
    },
    {
        'id': 2,
        'name': 'Auriculares Bluetooth',
        'description': 'Auriculares sem fios com cancelamento de ruído',
        'price': 89.99,
        'original_price': 129.99,
        'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=400&fit=crop',
        'category': 'Tecnologia',
        'rating': 4.6,
        'reviews_count': 89,
        'stock': 30
    },
    {
        'id': 3,
        'name': 'Smartwatch Desportivo',
        'description': 'Relógio inteligente para desporto e fitness',
        'price': 249.99,
        'original_price': 299.99,
        'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&h=400&fit=crop',
        'category': 'Tecnologia',
        'rating': 4.7,
        'reviews_count': 156,
        'stock': 25
    },
    {
        'id': 4,
        'name': 'Tablet 10 polegadas',
        'description': 'Tablet com ecrã de alta resolução',
        'price': 329.99,
        'original_price': 399.99,
        'image_url': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400&h=400&fit=crop',
        'category': 'Tecnologia',
        'rating': 4.5,
        'reviews_count': 78,
        'stock': 20
    }
]

@app.route('/api/products')
def get_products():
    return jsonify(SAMPLE_PRODUCTS)

@app.route('/api/products/<int:product_id>')
def get_product(product_id):
    product = next((p for p in SAMPLE_PRODUCTS if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Produto não encontrado'}), 404

@app.route('/api/products/featured')
def get_featured_products():
    return jsonify(SAMPLE_PRODUCTS[:4])

@app.route('/api/payments/methods')
def get_payment_methods():
    return jsonify({
        'methods': [
            {'id': 'mbway', 'name': 'MBWay', 'recommended': True},
            {'id': 'multibanco', 'name': 'Multibanco', 'recommended': False},
            {'id': 'card', 'name': 'Cartão de Crédito/Débito', 'recommended': False}
        ]
    })

@app.route('/api/orders', methods=['POST'])
def create_order():
    return jsonify({
        'id': 'ORD-12345',
        'status': 'pending',
        'message': 'Encomenda criada com sucesso'
    })

@app.route('/api/payments/mbway/request', methods=['POST'])
def request_mbway_payment():
    return jsonify({
        'id': 'PAY-67890',
        'status': 'pending',
        'message': 'Pedido de pagamento MBWay enviado. Verifique o seu telemóvel.'
    })

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

