import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { useState } from 'react'
import Header from './components/Header'
import Home from './components/Home'
import Products from './components/Products'
import Cart from './components/Cart'
import Checkout from './components/Checkout'
import { CartProvider } from './context/CartContext'
import './App.css'

function App() {
  return (
    <CartProvider>
      <Router>
        <div className="min-h-screen bg-background">
          <Header />
          <main>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/produtos" element={<Products />} />
              <Route path="/carrinho" element={<Cart />} />
              <Route path="/checkout" element={<Checkout />} />
            </Routes>
          </main>
        </div>
      </Router>
    </CartProvider>
  )
}

export default App

