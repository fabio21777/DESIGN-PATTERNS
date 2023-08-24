from abc import ABC, abstractmethod


# Interface Handler (AbstractHandler)
class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle_request(self, request):
        pass

# Concrete class that implements default behaviors between handlers
class AbstractHandler(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        # Returning handler to allow chaining
        return handler

    def handle_request(self, request):
        if self._next_handler:
            return self._next_handler.handle_request(request)
        return "Não foi possível resolver o problema. :´("

# ConcreteHandlers
class SupportLevel1(AbstractHandler):
    def handle_request(self, request):
        if request == "Problema Nível 1":
            return f"Suporte Nível 1 resolveu o {request}"
        else:
            return super().handle_request(request)

class SupportLevel2(AbstractHandler):
    def handle_request(self, request):
        if request == "Problema Nível 2":
            return f"Suporte Nível 2 resolveu o {request}"
        else:
            return super().handle_request(request)

class SupportLevel3(AbstractHandler):
    def handle_request(self, request):
        if request == "Problema Nível 3":
            return f"Suporte Nível 3 resolveu o {request}"
        else:
            return super().handle_request(request)

# Usage
support = SupportLevel1()
support.set_next(SupportLevel2()).set_next(SupportLevel3())

print(support.handle_request("Problema Nível 1"))
print(support.handle_request("Problema Nível 2"))
print(support.handle_request("Problema Nível 3"))
print(support.handle_request("Problema Nível 4"))
