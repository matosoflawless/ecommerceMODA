# E-Commerce MBWay - Projeto Completo

Este é o projeto completo de e-commerce com integração MBWay.

## 📁 Estrutura do Projeto

```
ecommerce_project_full/
├── frontend/                 # Aplicação React (Frontend)
│   ├── src/
│   │   ├── components/      # Componentes React
│   │   ├── context/         # Contextos (CartContext)
│   │   ├── App.jsx          # Componente principal
│   │   ├── main.jsx         # Ponto de entrada
│   │   └── index.css        # Estilos globais
│   ├── package.json         # Dependências (CORRIGIDO)
│   ├── vite.config.js       # Configuração Vite
│   └── index.html           # HTML principal
├── backend/                 # API Flask (Backend)
│   ├── src/
│   │   ├── main.py          # Aplicação Flask
│   │   ├── models/          # Modelos de dados
│   │   ├── routes/          # Rotas da API
│   │   └── services/        # Serviços (MBWay)
│   ├── requirements.txt     # Dependências Python
│   └── Procfile            # Para deployment
├── README.md               # Documentação principal
├── DEPLOYMENT.md           # Guia de deployment
└── RESUMO_EXECUTIVO.md     # Resumo do projeto
```

## 🚀 Como Usar

### Frontend (React)
```bash
cd frontend
npm install --legacy-peer-deps
npm run dev
```

### Backend (Flask)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python src/main.py
```

## 🌐 URLs

- **Frontend Deployado:** https://ssoqmmmg.manus.space
- **Local Frontend:** http://localhost:5173
- **Local Backend:** http://localhost:5000

## 📋 Funcionalidades

✅ Página inicial com produtos em destaque  
✅ Catálogo de produtos com filtros  
✅ Carrinho de compras funcional  
✅ Checkout com integração MBWay  
✅ Design responsivo  
✅ API RESTful completa  

## 🔧 Resolução de Problemas

Se tiver problemas com dependências:
```bash
npm cache clean --force
rm -rf node_modules package-lock.json
npm install --legacy-peer-deps
```

---

**Desenvolvido com ❤️ em Portugal 🇵🇹**

