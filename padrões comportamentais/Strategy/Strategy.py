from abc import ABC, abstractmethod

# Estratégia de Desconto Abstrata
class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, price: float) -> float:
        """Aplica desconto ao preço fornecido."""
        pass

# Estratégia de Desconto Fixo
class FixedDiscount(DiscountStrategy):

    def apply_discount(self, price: float) -> float:
        """Aplica um desconto fixo de $10 ao preço."""
        return price - 10

# Estratégia de Desconto em Percentagem
class PercentageDiscount(DiscountStrategy):

    def apply_discount(self, price: float) -> float:
        """Aplica um desconto de 10% ao preço."""
        return price * 0.9

# Classe Produto
class Product:

    def __init__(self, name: str, price: float, discount_strategy: DiscountStrategy):
        self.name = name
        self.price = price
        self.discount_strategy = discount_strategy

    def get_discounted_price(self) -> float:
        """Retorna o preço do produto após aplicar o desconto."""
        return self.discount_strategy.apply_discount(self.price)

if __name__ == "__main__":
    # Testando as estratégias de desconto
    product1 = Product("Camiseta Desconto Fixo", 50, FixedDiscount())
    print(f"Preço com desconto para {product1.name}: ${product1.get_discounted_price():.2f}")

    product2 = Product("Camiseta Desconto em Percentagem", 50, PercentageDiscount())
    print(f"Preço com desconto para {product2.name}: ${product2.get_discounted_price():.2f}")
