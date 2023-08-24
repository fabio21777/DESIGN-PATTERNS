from abc import ABC, abstractmethod

# metodo abstrato para que os serviços implementem o health check

class HealthCheck(ABC):
	@abstractmethod
	def health_check(self):
		pass

# classe abstrata que implementa a criação das mensagens de erro do health check

class CreatorMessage(ABC):
	@abstractmethod
	def create_message(self):# factory_method
		pass

# classe abstrata que implementa a criação dos serviços

class CreatorMessageServiceA(CreatorMessage):
	def create_message(self):
		print ("Serviço A mensagem de erro")

class CreatorMessageServiceB(CreatorMessage):
	def create_message(self):
		print ("Serviço B mensagem de erro")

class CreatorMessageServiceC(CreatorMessage):
	def create_message(self):
		print ("Serviço C mensagem de erro")

class ServiceA(HealthCheck):
	def health_check(self, creator_message: CreatorMessage):
		print("Serviço A verificando saúde")
		creator_message.create_message()

class ServiceB(HealthCheck):
	def health_check(self, creator_message: CreatorMessage):
		print("Serviço B verificando saúde")
		creator_message.create_message()

class ServiceC(HealthCheck):
	def health_check(self, creator_message: CreatorMessage):
		print("Serviço C verificando saúde")
		creator_message.create_message()


if __name__ == "__main__":
	service_a = ServiceA()
	service_b = ServiceB()
	service_c = ServiceC()

	creator_message_service_a = CreatorMessageServiceA()
	creator_message_service_b = CreatorMessageServiceB()
	creator_message_service_c = CreatorMessageServiceC()

	service_a.health_check(creator_message_service_a)
	service_b.health_check(creator_message_service_b)
	service_c.health_check(creator_message_service_c)
