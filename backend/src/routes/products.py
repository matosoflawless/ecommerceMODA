from flask import Blueprint, jsonify, request
from src.models.ecommerce import Product
from src.models.user import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products():
    """Obter lista de produtos com filtros opcionais"""
    try:
        # Parâmetros de query
        category = request.args.get('category')
        search = request.args.get('search')
        sort_by = request.args.get('sort_by', 'name')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))

        # Query base
        query = Product.query

        # Filtros
        if category and category != 'all':
            query = query.filter(Product.category == category)
        
        if search:
            query = query.filter(Product.name.contains(search))

        # Ordenação
        if sort_by == 'price-low':
            query = query.order_by(Product.price.asc())
        elif sort_by == 'price-high':
            query = query.order_by(Product.price.desc())
        elif sort_by == 'rating':
            query = query.order_by(Product.rating.desc())
        else:  # name
            query = query.order_by(Product.name.asc())

        # Paginação
        products = query.paginate(
            page=page, 
            per_page=per_page, 
            error_out=False
        )

        return jsonify({
            'products': [product.to_dict() for product in products.items],
            'total': products.total,
            'pages': products.pages,
            'current_page': page,
            'per_page': per_page
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@products_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Obter detalhes de um produto específico"""
    try:
        product = Product.query.get_or_404(product_id)
        return jsonify(product.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@products_bp.route('/products/categories', methods=['GET'])
def get_categories():
    """Obter lista de categorias disponíveis"""
    try:
        categories = db.session.query(Product.category).distinct().all()
        category_list = [cat[0] for cat in categories if cat[0]]
        return jsonify({'categories': category_list})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@products_bp.route('/products/featured', methods=['GET'])
def get_featured_products():
    """Obter produtos em destaque (com melhor rating ou mais vendidos)"""
    try:
        limit = int(request.args.get('limit', 8))
        products = Product.query.order_by(Product.rating.desc()).limit(limit).all()
        return jsonify([product.to_dict() for product in products])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

