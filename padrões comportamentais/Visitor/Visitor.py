class AnimalVisitor:
    def visit(self, animal):
        pass

class SoundVisitor(AnimalVisitor):
    def visit(self, animal):
        animal.make_sound()

class FeedVisitor(AnimalVisitor):
    def visit(self, animal):
        animal.eat()

class Animal:
    def accept(self, visitor):
        visitor.visit(self)

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

    def eat(self):
        print("Dog is eating.")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

    def eat(self):
        print("Cat is eating.")

# Criando animais
dog = Dog()
cat = Cat()

# Criando visitantes
sound_visitor = SoundVisitor()
feed_visitor = FeedVisitor()

# Fazendo os animais emitirem sons
dog.accept(sound_visitor)  # Output: Woof!
cat.accept(sound_visitor)  # Output: Meow!

# Alimentando os animais
dog.accept(feed_visitor)  # Output: Dog is eating.
cat.accept(feed_visitor)  # Output: Cat is eating.
