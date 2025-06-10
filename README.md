# E-Commerce com Integração MBWay

Um site de e-commerce completo desenvolvido com React (frontend) e Flask (backend), incluindo integração simulada com pagamentos MBWay.

## 🚀 Funcionalidades

### Frontend (React)
- **Página Inicial**: Hero section com destaque para pagamento MBWay
- **Catálogo de Produtos**: Listagem com filtros, pesquisa e ordenação
- **Carrinho de Compras**: Gestão de produtos, quantidades e totais
- **Checkout**: Formulário completo com múltiplos métodos de pagamento
- **Integração MBWay**: Campo específico para número de telemóvel
- **Design Responsivo**: Compatível com desktop e mobile
- **Interface Moderna**: Componentes UI com Radix UI

### Backend (Flask)
- **API RESTful**: Endpoints para produtos, encomendas e pagamentos
- **Base de Dados**: SQLite com modelos para produtos, utilizadores e encomendas
- **Integração MBWay**: Serviço simulado com validação de números portugueses
- **CORS**: Configurado para comunicação frontend-backend
- **Gestão de Stock**: Atualização automática após compras

### Integração MBWay
- **Validação de Números**: Verificação de números de telemóvel portugueses
- **Simulação Realista**: Processo de pagamento com estados (pendente, pago, rejeitado)
- **API Estruturada**: Endpoints específicos para pagamentos MBWay
- **Experiência Completa**: Desde o pedido até à confirmação

## 📁 Estrutura do Projeto

```
ecommerce-mbway/          # Frontend React
├── src/
│   ├── components/       # Componentes React
│   │   ├── ui/          # Componentes UI reutilizáveis
│   │   ├── Header.jsx   # Cabeçalho com navegação
│   │   ├── Home.jsx     # Página inicial
│   │   ├── Products.jsx # Catálogo de produtos
│   │   ├── Cart.jsx     # Carrinho de compras
│   │   └── Checkout.jsx # Processo de checkout
│   ├── context/         # Contextos React
│   │   └── CartContext.jsx # Gestão do carrinho
│   └── App.jsx          # Componente principal
├── package.json
└── vite.config.js

ecommerce-api/            # Backend Flask
├── src/
│   ├── models/          # Modelos da base de dados
│   │   ├── user.py      # Modelo de utilizador
│   │   └── ecommerce.py # Modelos de produtos e encomendas
│   ├── routes/          # Rotas da API
│   │   ├── products.py  # API de produtos
│   │   ├── orders.py    # API de encomendas
│   │   └── payments.py  # API de pagamentos
│   ├── services/        # Serviços
│   │   └── mbway_service.py # Integração MBWay
│   └── main.py          # Aplicação principal
├── venv/                # Ambiente virtual Python
└── requirements.txt
```

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Node.js 18+ e pnpm
- Python 3.11+ e pip
- Git

### Frontend (React)

```bash
cd ecommerce-mbway
pnpm install
pnpm run dev
```

O frontend estará disponível em: http://localhost:5173

### Backend (Flask)

```bash
cd ecommerce-api
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

pip install -r requirements.txt
python src/main.py
```

O backend estará disponível em: http://localhost:5000

## 📱 Como Usar

### 1. Navegação
- Aceda à página inicial em http://localhost:5173
- Explore os produtos em destaque
- Use a navegação para ver todos os produtos

### 2. Compras
- Adicione produtos ao carrinho
- Aceda ao carrinho para rever os itens
- Clique em "Finalizar Compra"

### 3. Checkout
- Preencha os dados de contacto e morada
- Selecione "MBWay" como método de pagamento
- Introduza o número de telemóvel
- Clique em "Pagar"

### 4. Pagamento MBWay (Simulado)
- O sistema simula o envio de notificação para o telemóvel
- O pagamento é processado automaticamente
- Receberá confirmação de sucesso

## 🔧 API Endpoints

### Produtos
- `GET /api/products` - Listar produtos
- `GET /api/products/{id}` - Detalhes do produto
- `GET /api/products/categories` - Categorias disponíveis
- `GET /api/products/featured` - Produtos em destaque

### Encomendas
- `POST /api/orders` - Criar encomenda
- `GET /api/orders/{id}` - Detalhes da encomenda
- `GET /api/orders/user/{email}` - Encomendas do utilizador

### Pagamentos MBWay
- `POST /api/payments/mbway/request` - Criar pedido de pagamento
- `GET /api/payments/mbway/status/{id}` - Verificar estado
- `POST /api/payments/validate-phone` - Validar número
- `GET /api/payments/methods` - Métodos disponíveis

## 🎯 Características Técnicas

### Frontend
- **React 18** com Hooks e Context API
- **Vite** para desenvolvimento rápido
- **React Router** para navegação
- **Radix UI** para componentes acessíveis
- **CSS Modules** para estilos

### Backend
- **Flask** com blueprints organizados
- **SQLAlchemy** para ORM
- **Flask-CORS** para comunicação cross-origin
- **SQLite** como base de dados
- **Validação** de dados de entrada

### Integração MBWay
- **Validação** de números portugueses (+351 9XXXXXXXX)
- **Simulação** de estados de pagamento
- **Timeout** e gestão de erros
- **Formatação** automática de números

## 🔒 Segurança

- Validação de dados no frontend e backend
- Sanitização de inputs
- Gestão de erros adequada
- CORS configurado adequadamente

## 📈 Melhorias Futuras

### Funcionalidades
- Autenticação de utilizadores
- Histórico de encomendas
- Sistema de avaliações
- Gestão de stock em tempo real
- Notificações por email

### Integração Real MBWay
- Integração com API real da SIBS
- Webhooks para confirmações
- Gestão de timeouts reais
- Logs de transações

### Performance
- Cache de produtos
- Lazy loading de imagens
- Paginação otimizada
- CDN para assets

## 🤝 Contribuição

Este projeto foi desenvolvido como demonstração de integração MBWay. Para contribuir:

1. Faça fork do projeto
2. Crie uma branch para a funcionalidade
3. Implemente as mudanças
4. Teste thoroughly
5. Submeta um pull request

## 📄 Licença

Este projeto é fornecido como exemplo educacional. Use responsavelmente e adapte às suas necessidades.

## 📞 Suporte

Para questões sobre implementação ou integração real com MBWay, consulte:
- [Documentação SIBS](https://www.pay.sibs.com/)
- [ifthenpay API](https://ifthenpay.com/docs/)
- [MBWay Integradores](https://www.mbway.pt/integradores-mb-way/)

---

**Desenvolvido com ❤️ em Portugal 🇵🇹**

