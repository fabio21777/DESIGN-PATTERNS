from abc import ABC, abstractmethod


# Interface Handler (AbstractHandler)
class Handler(ABC):
    @abstractmethod
    def set_proximo(self, handler):
        pass

    @abstractmethod
    def lidar_com_solicitacao(self, request):
        pass

# Classe concreta que implementa comportamentos padrões entre os handlers
class AbstractHandler(Handler):
    _proximo_handler = None

    def set_proximo(self, handler):
        self._proximo_handler = handler
        # Retornando handler para permitir encadeamento
        return handler

    def lidar_com_solicitacao(self, request):
        if self._proximo_handler:
            return self._proximo_handler.lidar_com_solicitacao(request)
        return "Não foi possível resolver o problema. :´("

# ConcreteHandlers
class SuporteNivel1(AbstractHandler):
    def lidar_com_solicitacao(self, request):
        if request == "Problema Nível 1":
            return f"Suporte Nível 1 resolveu o {request}"
        else:
            return super().lidar_com_solicitacao(request)

class SuporteNivel2(AbstractHandler):
    def lidar_com_solicitacao(self, request):
        if request == "Problema Nível 2":
            return f"Suporte Nível 2 resolveu o {request}"
        else:
            return super().lidar_com_solicitacao(request)

class SuporteNivel3(AbstractHandler):
    def lidar_com_solicitacao(self, request):
        if request == "Problema Nível 3":
            return f"Suporte Nível 3 resolveu o {request}"
        else:
            return super().lidar_com_solicitacao(request)

# Uso
suporte = SuporteNivel1()
suporte.set_proximo(SuporteNivel2()).set_proximo(SuporteNivel3())

print(suporte.lidar_com_solicitacao("Problema Nível 1"))
print(suporte.lidar_com_solicitacao("Problema Nível 2"))
print(suporte.lidar_com_solicitacao("Problema Nível 3"))
print(suporte.lidar_com_solicitacao("Problema Nível 4"))
