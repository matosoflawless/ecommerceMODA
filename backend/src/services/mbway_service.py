import requests
import time
import random
import uuid
from datetime import datetime, timedelta

class MBWayService:
    """Serviço para integração com MBWay (simulado)"""
    
    def __init__(self, api_key="demo_key", base_url="https://api.ifthenpay.com"):
        self.api_key = api_key
        self.base_url = base_url
        self.is_demo = True  # Modo demonstração
    
    def create_payment_request(self, phone_number, amount, order_id):
        """
        Criar pedido de pagamento MBWay
        
        Args:
            phone_number (str): Número de telemóvel do cliente
            amount (float): Valor a pagar
            order_id (int): ID da encomenda
            
        Returns:
            dict: Resposta com detalhes do pedido de pagamento
        """
        try:
            # Em modo demo, simular a criação do pedido
            if self.is_demo:
                return self._simulate_payment_request(phone_number, amount, order_id)
            
            # Em produção, fazer request real para a API
            payload = {
                'mbWayKey': self.api_key,
                'orderId': str(order_id),
                'amount': str(amount),
                'mobileNumber': phone_number,
                'description': f'Pagamento encomenda #{order_id}'
            }
            
            response = requests.post(
                f"{self.base_url}/api/mbway/payment",
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {
                    'status': 'error',
                    'message': f'Erro na API: {response.status_code}'
                }
                
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Erro na comunicação: {str(e)}'
            }
    
    def _simulate_payment_request(self, phone_number, amount, order_id):
        """Simular criação de pedido de pagamento"""
        # Simular tempo de processamento
        time.sleep(1)
        
        # Gerar ID único para o pedido
        request_id = str(uuid.uuid4())
        
        # Simular resposta da API
        return {
            'status': 'success',
            'request_id': request_id,
            'order_id': order_id,
            'amount': amount,
            'phone_number': phone_number,
            'expires_at': (datetime.now() + timedelta(minutes=5)).isoformat(),
            'message': 'Pedido de pagamento criado. Verifique o seu telemóvel.'
        }
    
    def check_payment_status(self, request_id, order_id):
        """
        Verificar estado do pagamento
        
        Args:
            request_id (str): ID do pedido de pagamento
            order_id (int): ID da encomenda
            
        Returns:
            dict: Estado atual do pagamento
        """
        try:
            if self.is_demo:
                return self._simulate_payment_status(request_id, order_id)
            
            # Em produção, consultar API real
            response = requests.get(
                f"{self.base_url}/api/mbway/payment/{request_id}",
                params={'mbWayKey': self.api_key},
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {
                    'status': 'error',
                    'message': f'Erro na consulta: {response.status_code}'
                }
                
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Erro na comunicação: {str(e)}'
            }
    
    def _simulate_payment_status(self, request_id, order_id):
        """Simular verificação de estado do pagamento"""
        # Simular diferentes estados baseados em probabilidades
        rand = random.random()
        
        if rand < 0.1:  # 10% - ainda pendente
            return {
                'status': 'pending',
                'request_id': request_id,
                'order_id': order_id,
                'message': 'Aguardando confirmação do cliente'
            }
        elif rand < 0.85:  # 75% - pago com sucesso
            return {
                'status': 'paid',
                'request_id': request_id,
                'order_id': order_id,
                'transaction_id': f'TXN_{uuid.uuid4().hex[:8].upper()}',
                'paid_at': datetime.now().isoformat(),
                'message': 'Pagamento confirmado com sucesso'
            }
        elif rand < 0.95:  # 10% - rejeitado pelo cliente
            return {
                'status': 'rejected',
                'request_id': request_id,
                'order_id': order_id,
                'message': 'Pagamento rejeitado pelo cliente'
            }
        else:  # 5% - expirado
            return {
                'status': 'expired',
                'request_id': request_id,
                'order_id': order_id,
                'message': 'Pedido de pagamento expirou'
            }
    
    def validate_phone_number(self, phone_number):
        """
        Validar número de telemóvel português
        
        Args:
            phone_number (str): Número a validar
            
        Returns:
            bool: True se válido, False caso contrário
        """
        # Remover espaços e caracteres especiais
        clean_number = ''.join(filter(str.isdigit, phone_number))
        
        # Verificar se é número português válido
        if len(clean_number) == 9 and clean_number.startswith('9'):
            return True
        elif len(clean_number) == 12 and clean_number.startswith('351') and clean_number[3] == '9':
            return True
        elif len(clean_number) == 13 and clean_number.startswith('+351') and clean_number[4] == '9':
            return True
        
        return False
    
    def format_phone_number(self, phone_number):
        """
        Formatar número de telemóvel para o formato padrão
        
        Args:
            phone_number (str): Número a formatar
            
        Returns:
            str: Número formatado (+351XXXXXXXXX)
        """
        clean_number = ''.join(filter(str.isdigit, phone_number))
        
        if len(clean_number) == 9:
            return f"+351{clean_number}"
        elif len(clean_number) == 12 and clean_number.startswith('351'):
            return f"+{clean_number}"
        
        return phone_number

