import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group'
import { Separator } from '@/components/ui/separator'
import { CreditCard, Smartphone, Building, CheckCircle, ArrowLeft } from 'lucide-react'
import { useCart } from '../context/CartContext'
import { Link } from 'react-router-dom'

const Checkout = () => {
  const { items, getTotalPrice, clearCart } = useCart()
  const [paymentMethod, setPaymentMethod] = useState('mbway')
  const [isProcessing, setIsProcessing] = useState(false)
  const [orderComplete, setOrderComplete] = useState(false)
  const [formData, setFormData] = useState({
    email: '',
    firstName: '',
    lastName: '',
    phone: '',
    address: '',
    city: '',
    postalCode: '',
    mbwayPhone: ''
  })

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setIsProcessing(true)

    // Simular processamento do pagamento
    setTimeout(() => {
      setIsProcessing(false)
      setOrderComplete(true)
      clearCart()
    }, 3000)
  }

  if (items.length === 0 && !orderComplete) {
    return (
      <div className="min-h-screen py-8">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center py-16">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Carrinho vazio</h2>
            <p className="text-xl text-gray-600 mb-8">Adicione produtos ao carrinho para continuar</p>
            <Link to="/produtos">
              <Button size="lg">
                <ArrowLeft className="h-4 w-4 mr-2" />
                Ver Produtos
              </Button>
            </Link>
          </div>
        </div>
      </div>
    )
  }

  if (orderComplete) {
    return (
      <div className="min-h-screen py-8">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center py-16">
            <CheckCircle className="h-24 w-24 text-green-500 mx-auto mb-6" />
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Encomenda Confirmada!</h2>
            <p className="text-xl text-gray-600 mb-8">
              Obrigado pela sua compra. Receberá um email de confirmação em breve.
            </p>
            <div className="space-x-4">
              <Link to="/">
                <Button size="lg">Voltar ao Início</Button>
              </Link>
              <Link to="/produtos">
                <Button variant="outline" size="lg">Continuar Compras</Button>
              </Link>
            </div>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen py-8">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold mb-4">Finalizar Compra</h1>
          <p className="text-xl text-gray-600">Complete os seus dados para finalizar a encomenda</p>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {/* Checkout Form */}
            <div className="space-y-6">
              {/* Contact Information */}
              <Card>
                <CardHeader>
                  <CardTitle>Informações de Contacto</CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div>
                    <Label htmlFor="email">Email *</Label>
                    <Input
                      id="email"
                      name="email"
                      type="email"
                      required
                      value={formData.email}
                      onChange={handleInputChange}
                      placeholder="seu@email.com"
                    />
                  </div>
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <Label htmlFor="firstName">Nome *</Label>
                      <Input
                        id="firstName"
                        name="firstName"
                        required
                        value={formData.firstName}
                        onChange={handleInputChange}
                        placeholder="João"
                      />
                    </div>
                    <div>
                      <Label htmlFor="lastName">Apelido *</Label>
                      <Input
                        id="lastName"
                        name="lastName"
                        required
                        value={formData.lastName}
                        onChange={handleInputChange}
                        placeholder="Silva"
                      />
                    </div>
                  </div>
                  <div>
                    <Label htmlFor="phone">Telefone *</Label>
                    <Input
                      id="phone"
                      name="phone"
                      type="tel"
                      required
                      value={formData.phone}
                      onChange={handleInputChange}
                      placeholder="+351 912 345 678"
                    />
                  </div>
                </CardContent>
              </Card>

              {/* Shipping Address */}
              <Card>
                <CardHeader>
                  <CardTitle>Morada de Entrega</CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div>
                    <Label htmlFor="address">Morada *</Label>
                    <Input
                      id="address"
                      name="address"
                      required
                      value={formData.address}
                      onChange={handleInputChange}
                      placeholder="Rua das Flores, 123"
                    />
                  </div>
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <Label htmlFor="city">Cidade *</Label>
                      <Input
                        id="city"
                        name="city"
                        required
                        value={formData.city}
                        onChange={handleInputChange}
                        placeholder="Lisboa"
                      />
                    </div>
                    <div>
                      <Label htmlFor="postalCode">Código Postal *</Label>
                      <Input
                        id="postalCode"
                        name="postalCode"
                        required
                        value={formData.postalCode}
                        onChange={handleInputChange}
                        placeholder="1000-001"
                      />
                    </div>
                  </div>
                </CardContent>
              </Card>

              {/* Payment Method */}
              <Card>
                <CardHeader>
                  <CardTitle>Método de Pagamento</CardTitle>
                </CardHeader>
                <CardContent>
                  <RadioGroup value={paymentMethod} onValueChange={setPaymentMethod}>
                    <div className="flex items-center space-x-2 p-4 border rounded-lg">
                      <RadioGroupItem value="mbway" id="mbway" />
                      <Label htmlFor="mbway" className="flex items-center space-x-2 cursor-pointer flex-1">
                        <Smartphone className="h-5 w-5 text-green-600" />
                        <span>MBWay</span>
                        <span className="text-sm text-gray-500">(Recomendado)</span>
                      </Label>
                    </div>
                    <div className="flex items-center space-x-2 p-4 border rounded-lg">
                      <RadioGroupItem value="multibanco" id="multibanco" />
                      <Label htmlFor="multibanco" className="flex items-center space-x-2 cursor-pointer flex-1">
                        <Building className="h-5 w-5 text-blue-600" />
                        <span>Multibanco</span>
                      </Label>
                    </div>
                    <div className="flex items-center space-x-2 p-4 border rounded-lg">
                      <RadioGroupItem value="card" id="card" />
                      <Label htmlFor="card" className="flex items-center space-x-2 cursor-pointer flex-1">
                        <CreditCard className="h-5 w-5 text-purple-600" />
                        <span>Cartão de Crédito/Débito</span>
                      </Label>
                    </div>
                  </RadioGroup>

                  {paymentMethod === 'mbway' && (
                    <div className="mt-4">
                      <Label htmlFor="mbwayPhone">Número de Telemóvel MBWay *</Label>
                      <Input
                        id="mbwayPhone"
                        name="mbwayPhone"
                        type="tel"
                        required
                        value={formData.mbwayPhone}
                        onChange={handleInputChange}
                        placeholder="+351 912 345 678"
                        className="mt-2"
                      />
                      <p className="text-sm text-gray-600 mt-2">
                        Receberá uma notificação no seu telemóvel para confirmar o pagamento
                      </p>
                    </div>
                  )}
                </CardContent>
              </Card>
            </div>

            {/* Order Summary */}
            <div>
              <Card className="sticky top-24">
                <CardHeader>
                  <CardTitle>Resumo da Encomenda</CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  {/* Products */}
                  <div className="space-y-3">
                    {items.map((item) => (
                      <div key={item.id} className="flex justify-between items-center">
                        <div className="flex items-center space-x-3">
                          <img 
                            src={item.image} 
                            alt={item.name}
                            className="w-12 h-12 object-cover rounded"
                          />
                          <div>
                            <p className="font-medium">{item.name}</p>
                            <p className="text-sm text-gray-600">Qty: {item.quantity}</p>
                          </div>
                        </div>
                        <p className="font-semibold">€{(item.price * item.quantity).toFixed(2)}</p>
                      </div>
                    ))}
                  </div>

                  <Separator />

                  {/* Totals */}
                  <div className="space-y-2">
                    <div className="flex justify-between">
                      <span>Subtotal</span>
                      <span>€{getTotalPrice().toFixed(2)}</span>
                    </div>
                    <div className="flex justify-between">
                      <span>Envio</span>
                      <span className="text-green-600">Grátis</span>
                    </div>
                    <div className="flex justify-between">
                      <span>IVA (23%)</span>
                      <span>€{(getTotalPrice() * 0.23).toFixed(2)}</span>
                    </div>
                    <Separator />
                    <div className="flex justify-between font-bold text-lg">
                      <span>Total</span>
                      <span>€{(getTotalPrice() * 1.23).toFixed(2)}</span>
                    </div>
                  </div>

                  {/* Submit Button */}
                  <Button 
                    type="submit" 
                    className="w-full" 
                    size="lg"
                    disabled={isProcessing}
                  >
                    {isProcessing ? (
                      <>
                        <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                        A processar...
                      </>
                    ) : (
                      `Pagar €${(getTotalPrice() * 1.23).toFixed(2)}`
                    )}
                  </Button>

                  <p className="text-xs text-gray-600 text-center">
                    Ao finalizar a compra, aceita os nossos termos e condições
                  </p>
                </CardContent>
              </Card>
            </div>
          </div>
        </form>
      </div>
    </div>
  )
}

export default Checkout

