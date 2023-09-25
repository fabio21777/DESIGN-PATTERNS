from datetime import datetime

class DateConverterSingleton:
    _instance = None  # Atributo privado para armazenar a única instância

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()  # Cria uma instância se não existir
        return cls._instance  # Retorna a instância existente

    def __init__(self):
        if DateConverterSingleton._instance is not None:
            raise Exception("Esta classe é um Singleton! Use o método get_instance para obter a instância.")

    def convert_to_brazilian(self, date):
        return date.strftime("%d/%m/%Y")

    def convert_to_american(self, date):
        return date.strftime("%Y-%m-%d")

    def convert_to_european(self, date):
        return date.strftime("%d.%m.%Y")

# Teste
date_converter = DateConverterSingleton.get_instance()

# Convertendo uma data para diferentes formatos
date = datetime.now()
print(date_converter.convert_to_brazilian(date))  # Output: 25/09/2023 (ou a data atual)
print(date_converter.convert_to_american(date))   # Output: 2023-09-25 (ou a data atual)
print(date_converter.convert_to_european(date))   # Output: 25.09.2023 (ou a data atual)