class WeatherObserver:
    def update(self, temperature, humidity):
        pass

class User(WeatherObserver):
    def __init__(self, name):
        self.name = name

    def update(self, temperature, humidity):
        print(f'{self.name} recebeu a atualização do clima: Temperatura = {temperature}°C, Umidade = {humidity}%')

class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity)

    def set_conditions(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.notify_observers()

# Criando instâncias de usuários
user1 = User("João")
user2 = User("Maria")

# Criando uma instância da estação meteorológica
weather_station = WeatherStation()

# Registrando os usuários na estação meteorológica
weather_station.register_observer(user1)
weather_station.register_observer(user2)

# Atualizando as condições climáticas e notificando os usuários
weather_station.set_conditions(30, 60)

# Saída:
# João recebeu a atualização do clima: Temperatura = 30°C, Umidade = 60%
# Maria recebeu a atualização do clima: Temperatura = 30°C, Umidade = 60%
