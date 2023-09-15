class Mediator:
    def __init__(self):
        self._colleagues = []

    def add_colleague(self, colleague):
        self._colleagues.append(colleague)

    def send(self, message, sender):
        for colleague in self._colleagues:
            if colleague != sender:
                colleague.receive(message)


class Colleague:
    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name
        mediator.add_colleague(self)

    def send(self, message):
        print(f"{self._name} enviou: {message}")
        self._mediator.send(message, self)

    def receive(self, message):
        print(f"{self._name} recebeu: {message}")


class Developer(Colleague):
    def receive(self, message):
        print(f"Desenvolvedor {self._name} recebeu: {message}")


class Tester(Colleague):
    def receive(self, message):
        print(f"Tester {self._name} recebeu: {message}")


# Exemplo de uso
if __name__ == "__main__":
    mediator = Mediator()

    dev1 = Developer(mediator, "Dev1")
    dev2 = Developer(mediator, "Dev2")
    tester1 = Tester(mediator, "Tester1")
    tester2 = Tester(mediator, "Tester2")

    dev1.send("O novo recurso foi implementado.")
    tester1.send("O novo recurso passou em todos os testes.")
