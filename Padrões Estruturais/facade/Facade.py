# Subsistemas
class Stock:
    def check_product_availability(self, product_id):
        # Aqui teríamos uma lógica real para verificar o estoque
        print(f"Verificando disponibilidade do produto {product_id}...")
        return True

class Payment:
    def process_payment(self, user, amount):
        # Lógica real de processamento de pagamento
        print(f"Processando pagamento de {user} no valor de {amount}...")
        return True

class Delivery:
    def organize_delivery(self, user, product_id):
        # Lógica real para organizar a entrega
        print(f"Organizando entrega do produto {product_id} para {user}...")
        return True

# Facade
class OrderFacade:
    def __init__(self):
        self.stock = Stock()
        self.payment = Payment()
        self.delivery = Delivery()

    def allProcess(self, user, product_id, amount):
        if not self.stock.check_product_availability(product_id):
            print("Produto indisponível!")
            return False

        if not self.payment.process_payment(user, amount):
            print("Falha no pagamento!")
            return False

        if not self.delivery.organize_delivery(user, product_id):
            print("Falha na organização da entrega!")
            return False

        print("Pedido realizado com sucesso!")
        return True

    def check_stock(self, product_id):
	    return self.stock.check_product_availability(product_id)
 
    def process_payment(self, user, amount):
        return self.payment.process_payment(user, amount)
    
    def organize_delivery(self, user, product_id):
        return self.delivery.organize_delivery(user, product_id)
    
# Cliente
if __name__ == "__main__":
    order_system = OrderFacade()
    #order_system.allProcess("João", "12345", 100)
    order_system.check_stock("12345")
    order_system.process_payment("João", 100);
    order_system.organize_delivery("João", "12345")
