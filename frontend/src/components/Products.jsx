import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { ShoppingCart, Star, Search, Filter } from 'lucide-react'
import { useCart } from '../context/CartContext'

// Dados de exemplo para todos os produtos
const allProducts = [
  {
    id: 1,
    name: "Smartphone Premium",
    price: 599.99,
    originalPrice: 699.99,
    image: "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=400&fit=crop",
    rating: 4.8,
    reviews: 124,
    category: "Tecnologia"
  },
  {
    id: 2,
    name: "Auriculares Bluetooth",
    price: 89.99,
    originalPrice: 129.99,
    image: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=400&fit=crop",
    rating: 4.6,
    reviews: 89,
    category: "Tecnologia"
  },
  {
    id: 3,
    name: "Smartwatch Desportivo",
    price: 249.99,
    originalPrice: 299.99,
    image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&h=400&fit=crop",
    rating: 4.7,
    reviews: 156,
    category: "Tecnologia"
  },
  {
    id: 4,
    name: "Tablet 10 polegadas",
    price: 329.99,
    originalPrice: 399.99,
    image: "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400&h=400&fit=crop",
    rating: 4.5,
    reviews: 78,
    category: "Tecnologia"
  },
  {
    id: 5,
    name: "Câmara Digital",
    price: 449.99,
    originalPrice: 549.99,
    image: "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=400&h=400&fit=crop",
    rating: 4.9,
    reviews: 203,
    category: "Tecnologia"
  },
  {
    id: 6,
    name: "Portátil Gaming",
    price: 899.99,
    originalPrice: 1099.99,
    image: "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400&h=400&fit=crop",
    rating: 4.7,
    reviews: 167,
    category: "Tecnologia"
  },
  {
    id: 7,
    name: "T-shirt Casual",
    price: 24.99,
    originalPrice: 34.99,
    image: "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=400&fit=crop",
    rating: 4.3,
    reviews: 45,
    category: "Moda"
  },
  {
    id: 8,
    name: "Ténis Desportivos",
    price: 79.99,
    originalPrice: 99.99,
    image: "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&h=400&fit=crop",
    rating: 4.6,
    reviews: 112,
    category: "Moda"
  }
]

const Products = () => {
  const { addToCart } = useCart()
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedCategory, setSelectedCategory] = useState('all')
  const [sortBy, setSortBy] = useState('name')

  const categories = ['all', ...new Set(allProducts.map(product => product.category))]

  const filteredProducts = allProducts
    .filter(product => 
      product.name.toLowerCase().includes(searchTerm.toLowerCase()) &&
      (selectedCategory === 'all' || product.category === selectedCategory)
    )
    .sort((a, b) => {
      switch (sortBy) {
        case 'price-low':
          return a.price - b.price
        case 'price-high':
          return b.price - a.price
        case 'rating':
          return b.rating - a.rating
        default:
          return a.name.localeCompare(b.name)
      }
    })

  const handleAddToCart = (product) => {
    addToCart(product)
  }

  return (
    <div className="min-h-screen py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold mb-4">Todos os Produtos</h1>
          <p className="text-xl text-gray-600">Descubra a nossa seleção completa</p>
        </div>

        {/* Filters */}
        <div className="bg-white p-6 rounded-lg shadow-sm border mb-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {/* Search */}
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-4 w-4" />
              <Input
                placeholder="Pesquisar produtos..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="pl-10"
              />
            </div>

            {/* Category Filter */}
            <Select value={selectedCategory} onValueChange={setSelectedCategory}>
              <SelectTrigger>
                <SelectValue placeholder="Categoria" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">Todas as Categorias</SelectItem>
                {categories.filter(cat => cat !== 'all').map(category => (
                  <SelectItem key={category} value={category}>{category}</SelectItem>
                ))}
              </SelectContent>
            </Select>

            {/* Sort */}
            <Select value={sortBy} onValueChange={setSortBy}>
              <SelectTrigger>
                <SelectValue placeholder="Ordenar por" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="name">Nome A-Z</SelectItem>
                <SelectItem value="price-low">Preço: Baixo para Alto</SelectItem>
                <SelectItem value="price-high">Preço: Alto para Baixo</SelectItem>
                <SelectItem value="rating">Melhor Avaliação</SelectItem>
              </SelectContent>
            </Select>
          </div>
        </div>

        {/* Products Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {filteredProducts.map((product) => (
            <Card key={product.id} className="group hover:shadow-lg transition-shadow">
              <CardHeader className="p-0">
                <div className="relative overflow-hidden rounded-t-lg">
                  <img 
                    src={product.image} 
                    alt={product.name}
                    className="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300"
                  />
                  {product.originalPrice > product.price && (
                    <div className="absolute top-2 left-2 bg-red-500 text-white px-2 py-1 rounded text-sm font-semibold">
                      -{Math.round(((product.originalPrice - product.price) / product.originalPrice) * 100)}%
                    </div>
                  )}
                  <div className="absolute top-2 right-2 bg-black bg-opacity-50 text-white px-2 py-1 rounded text-xs">
                    {product.category}
                  </div>
                </div>
              </CardHeader>
              <CardContent className="p-4">
                <CardTitle className="text-lg mb-2">{product.name}</CardTitle>
                <div className="flex items-center mb-2">
                  <div className="flex items-center">
                    {[...Array(5)].map((_, i) => (
                      <Star 
                        key={i} 
                        className={`h-4 w-4 ${i < Math.floor(product.rating) ? 'text-yellow-400 fill-current' : 'text-gray-300'}`} 
                      />
                    ))}
                  </div>
                  <span className="text-sm text-gray-600 ml-2">({product.reviews})</span>
                </div>
                <div className="flex items-center space-x-2">
                  <span className="text-2xl font-bold text-primary">€{product.price}</span>
                  {product.originalPrice > product.price && (
                    <span className="text-lg text-gray-500 line-through">€{product.originalPrice}</span>
                  )}
                </div>
              </CardContent>
              <CardFooter className="p-4 pt-0">
                <Button 
                  className="w-full"
                  onClick={() => handleAddToCart(product)}
                >
                  <ShoppingCart className="h-4 w-4 mr-2" />
                  Adicionar ao Carrinho
                </Button>
              </CardFooter>
            </Card>
          ))}
        </div>

        {filteredProducts.length === 0 && (
          <div className="text-center py-12">
            <p className="text-xl text-gray-600">Nenhum produto encontrado.</p>
            <p className="text-gray-500 mt-2">Tente ajustar os filtros de pesquisa.</p>
          </div>
        )}
      </div>
    </div>
  )
}

export default Products

