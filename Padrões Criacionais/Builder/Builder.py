# Product
class Sandwich:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def show(self):
        print("Sanduíche com:", ", ".join(self.ingredients))

# Builder Interface
class SandwichBuilder:
    def add_meat(self):
        pass

    def add_vegetable(self):
        pass

    def add_condiment(self):
        pass

    def get_result(self):
        pass

# ConcreteBuilder
class ChickenSandwichBuilder(SandwichBuilder):
    def __init__(self):
        self.sandwich = Sandwich()

    def add_meat(self):
        self.sandwich.add_ingredient("Frango")

    def add_vegetable(self):
        self.sandwich.add_ingredient("Alface")

    def add_condiment(self):
        self.sandwich.add_ingredient("Maionese")

    def get_result(self):
        return self.sandwich

# ConcreteBuilder
class VeggieSandwichBuilder(SandwichBuilder):
    def __init__(self):
        self.sandwich = Sandwich()

    def add_vegetable(self):
        self.sandwich.add_ingredient("Tomate")
        self.sandwich.add_ingredient("Pepino")

    def add_condiment(self):
        self.sandwich.add_ingredient("Mostarda")

    def get_result(self):
        return self.sandwich

# Director
class SandwichDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_sandwich(self):
        self.builder.add_meat()
        self.builder.add_vegetable()
        self.builder.add_condiment()
        return self.builder.get_result()

# Client
chicken_builder = ChickenSandwichBuilder()
director = SandwichDirector(chicken_builder)
chicken_sandwich = director.make_sandwich()
chicken_sandwich.show()

veggie_builder = VeggieSandwichBuilder()
director = SandwichDirector(veggie_builder)
veggie_sandwich = director.make_sandwich()
veggie_sandwich.show()
