# Interface de Estado
class State:
    def insert_coin(self, machine):
        pass

    def eject_coin(self, machine):
        pass

    def turn_crank(self, machine):
        pass

# Estados Concretos
class NoGumball(State):
    def insert_coin(self, machine):
        print("Sem goma: Inserção de moeda não permitida.")

    def eject_coin(self, machine):
        print("Sem goma: Não há moeda para ejetar.")

    def turn_crank(self, machine):
        print("Sem goma: Girar a manivela não é permitido.")

class HasGumball(State):
    def insert_coin(self, machine):
        print("Moeda inserida. Gire a manivela para obter uma goma.")
        machine.set_state(CoinInserted())

    def eject_coin(self, machine):
        print("Nenhuma moeda inserida para ejetar.")

    def turn_crank(self, machine):
        print("Nenhuma moeda inserida. Insira uma moeda primeiro.")

class CoinInserted(State):
    def insert_coin(self, machine):
        print("Moeda já inserida.")

    def eject_coin(self, machine):
        print("Moeda ejetada.")
        machine.set_state(HasGumball())

    def turn_crank(self, machine):
        print("Goma entregue.")
        machine.set_state(NoGumball())

# Contexto
class GumballMachine:
    def __init__(self):
        self.state = NoGumball()

    def set_state(self, state):
        self.state = state

    def insert_coin(self):
        self.state.insert_coin(self)

    def eject_coin(self):
        self.state.eject_coin(self)

    def turn_crank(self):
        self.state.turn_crank(self)

# Teste
machine = GumballMachine()
machine.insert_coin()  # Output: Sem goma: Inserção de moeda não permitida.
machine.set_state(HasGumball())
machine.insert_coin()  # Output: Moeda inserida. Gire a manivela para obter uma goma.
machine.turn_crank()   # Output: Goma entregue.
