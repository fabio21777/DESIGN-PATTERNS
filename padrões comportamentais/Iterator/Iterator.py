from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next_item(self):
        pass


class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass


class ConcreteAggregate(Aggregate):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def create_iterator(self, iterator_type):
        if iterator_type == 'forward':
            return ForwardIterator(self)
        else:
            return BackwardIterator(self)


class ForwardIterator(Iterator):
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.current_index = 0

    def has_next(self):
        return self.current_index < len(self.aggregate.items)

    def next_item(self):
        if self.has_next():
            item = self.aggregate.items[self.current_index]
            self.current_index += 1
            return item
        else:
            raise StopIteration


class BackwardIterator(Iterator):
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.current_index = len(self.aggregate.items) - 1

    def has_next(self):
        return self.current_index >= 0

    def next_item(self):
        if self.has_next():
            item = self.aggregate.items[self.current_index]
            self.current_index -= 1
            return item
        else:
            raise StopIteration


# Exemplo de uso
if __name__ == "__main__":
    aggregate = ConcreteAggregate()
    aggregate.add_item("Item 1")
    aggregate.add_item("Item 2")
    aggregate.add_item("Item 3")

    print("Iteração para frente:")
    forward_iterator = aggregate.create_iterator('forward')
    while forward_iterator.has_next():
        print(forward_iterator.next_item())

    print("\nIteração para trás:")
    backward_iterator = aggregate.create_iterator('backward')
    while backward_iterator.has_next():
        print(backward_iterator.next_item())
