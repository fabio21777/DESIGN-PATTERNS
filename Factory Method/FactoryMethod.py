# Exemplo do padrão Factory Method
# Descrição do problema - suponha que você tem varias entidades que podem ter dados persistidos em um banco de dados
# porém algum dados são persistidos com alguma inconsistência, por exemplo, o campo que deveria estar preenchido e não está
# ou com a mudança de um regra de negocio o campo que deveria ser preenchido com um valor passa a ser preenchido com outro algum similar
# um  health check é uma forma de verificar se os dados estão consistentes, porém cada entidade tem sua regra de negocio para verificar


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
		print ("Service A message errors")

class CreatorMessageServiceB(CreatorMessage):
	def create_message(self):
		print ("Service B message errors")

class CreatorMessageServiceC(CreatorMessage):
	def create_message(self):
		print ("Service C message errors")

class ServiceA(HealthCheck):
	def health_check(self, creator_message: CreatorMessage):
		print("Service A health check")
		creator_message.create_message()

class ServiceB(HealthCheck):
	def health_check(self, creator_message: CreatorMessage):
		print("Service B health check")
		creator_message.create_message()

class ServiceC(HealthCheck):
	def health_check(self, creator_message: CreatorMessage):
		print("Service C health check")
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






