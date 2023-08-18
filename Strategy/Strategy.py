from abc import ABC, abstractmethod


# Estratégia abstrata
class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass

# Estratégia concreta 1: Desconto fixo de $10
class FixedDiscount(DiscountStrategy):

    def apply_discount(self, price: float) -> float:
        return price - 10

# Estratégia concreta 2: Desconto de 10%
class PercentageDiscount(DiscountStrategy):

    def apply_discount(self, price: float) -> float:
        return price * 0.9

# Contexto
class Product:

    def __init__(self, name: str, price: float, discount_strategy: DiscountStrategy):
        self.name = name
        self.price = price
        self.discount_strategy = discount_strategy

    def get_discounted_price(self) -> float:
        return self.discount_strategy.apply_discount(self.price)

# Testando
product1 = Product("Camiseta-desconto-fixo", 50, FixedDiscount())
print(f"Preço com desconto para {product1.name}: ${product1.get_discounted_price()}")

product2 = Product("Camiseta-desconto-porcentagem", 50, PercentageDiscount())
print(f"Preço com desconto para {product2.name}: ${product2.get_discounted_price()}")
