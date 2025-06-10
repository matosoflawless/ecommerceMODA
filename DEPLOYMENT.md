# Guia de Deployment - E-Commerce MBWay

## 🚀 Deployment em Produção

### Frontend (React)

#### Opção 1: Vercel (Recomendado)
```bash
# 1. Build da aplicação
cd ecommerce-mbway
pnpm run build

# 2. Deploy no Vercel
npx vercel --prod
```

#### Opção 2: Netlify
```bash
# 1. Build da aplicação
pnpm run build

# 2. Deploy manual ou conectar repositório Git
# Upload da pasta dist/ para Netlify
```

### Backend (Flask)

#### Opção 1: Railway
```bash
# 1. Criar Procfile
echo "web: python src/main.py" > Procfile

# 2. Configurar variáveis de ambiente
# DATABASE_URL, SECRET_KEY, etc.

# 3. Deploy via Git
git push railway main
```

#### Opção 2: Heroku
```bash
# 1. Criar Procfile
echo "web: gunicorn --bind 0.0.0.0:$PORT src.main:app" > Procfile

# 2. Instalar gunicorn
pip install gunicorn
pip freeze > requirements.txt

# 3. Deploy
git push heroku main
```

## 🔧 Configurações de Produção

### Variáveis de Ambiente

#### Frontend (.env.production)
```
VITE_API_URL=https://sua-api.herokuapp.com
VITE_ENVIRONMENT=production
```

#### Backend
```
SECRET_KEY=sua-chave-secreta-forte
DATABASE_URL=postgresql://user:pass@host:port/db
FLASK_ENV=production
CORS_ORIGINS=https://seu-frontend.vercel.app
```

### Base de Dados

#### PostgreSQL (Produção)
```python
# src/main.py
import os

if os.environ.get('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
    # SQLite para desenvolvimento
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
```

## 🔒 Segurança em Produção

### HTTPS
- Certificados SSL/TLS obrigatórios
- Redirecionamento HTTP → HTTPS
- HSTS headers

### CORS
```python
# Configuração restritiva para produção
CORS(app, origins=[
    'https://seu-dominio.com',
    'https://www.seu-dominio.com'
])
```

### Secrets
- Nunca commitar chaves de API
- Usar variáveis de ambiente
- Rotação regular de secrets

## 📊 Monitorização

### Logs
```python
import logging

if app.config['ENV'] == 'production':
    logging.basicConfig(level=logging.INFO)
```

### Métricas
- Tempo de resposta da API
- Taxa de conversão de checkout
- Erros de pagamento MBWay

## 🔄 CI/CD

### GitHub Actions
```yaml
# .github/workflows/deploy.yml
name: Deploy
on:
  push:
    branches: [main]

jobs:
  deploy-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
      - run: pnpm install
      - run: pnpm run build
      - uses: vercel/action@v1

  deploy-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt
      - run: python -m pytest
      - uses: railway/action@v1
```

## 🧪 Testes

### Frontend
```bash
# Testes unitários
pnpm run test

# Testes E2E
pnpm run test:e2e
```

### Backend
```bash
# Testes da API
python -m pytest tests/

# Coverage
python -m pytest --cov=src tests/
```

## 📈 Performance

### Frontend
- Code splitting
- Lazy loading
- Image optimization
- CDN para assets

### Backend
- Database indexing
- Query optimization
- Caching (Redis)
- Rate limiting

## 🔧 Manutenção

### Backups
- Base de dados diários
- Logs rotativos
- Snapshots de código

### Updates
- Dependências de segurança
- Patches do sistema
- Monitoring de vulnerabilidades

---

**Nota**: Este guia assume deployment básico. Para produção real com MBWay, consulte a documentação oficial da SIBS e implemente as medidas de segurança adequadas.

