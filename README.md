# Estudos sobre padrões de projetos

Este é apenas o resumo dos meus estudos iniciais sobre padrões de projeto. Os exemplos serão feitos em Python (estou aprendendo :)). Serão abordados todos os padrões descritos no livro; porém, haverá exemplos em Python apenas daqueles que julguei serem mais impactantes e mais comumente usados no meu dia a dia como programador em Java/JavaScript. As principais fontes de estudo foram [DESIGN PATTERNS -refactoring-guru](https://refactoring.guru/design-patterns) e 'Design Patterns: Elements of Reusable Object-Oriented Software'. Durante o meu estudo, pretendo visitar outros sites e vídeos.

## Introdução

### Padrões Criacionais
Os padrões criacionais se concentram em técnicas de criação de objetos, garantindo que os objetos sejam criados de maneira adequada para a situação.

1. **[Singleton](#singleton)**
2. **[Factory Method](#factory-method)**
3. **[Abstract Factory](#abstract-factory)**
4. **[Builder](#builder)**
5. **[Prototype](#prototype)**

### Padrões Estruturais
Os padrões estruturais se concentram em como os objetos e classes são combinados para formar estruturas maiores.

1. **[Adapter](#adapter)**
2. **[Bridge](#bridge)**
3. **[Composite](#composite)**
4. **[Decorator](#decorator)**
5. **[Facade](#facade)**
6. **[Flyweight](#flyweight)**
7. **[Proxy](#proxy)**

### Padrões Comportamentais
Os padrões comportamentais se concentram na comunicação entre objetos.

1. **[Chain of Responsibility](#chain-of-responsibility)**
2. **[Command](#command)**
3. **[Interpreter](#interpreter)**
4. **[Iterator](#iterator)**
5. **[Mediator](#mediator)**
6. **[Memento](#memento)**
7. **[Observer](#observer)**
8. **[State](#state)**
9. **[Strategy](#strategy)**
10. **[Template Method](#template-method)**
11. **[Visitor](#visitor)**


## Explorando mais detalhadamente os padrões de projetos.

### Padrões Criacionais


#### Factory Method

#### Definição
O Factory Method é um padrão de design criacional que fornece uma interface para criar objetos, mas permite que as subclasses alterem o tipo de objetos que serão criados.

#### Intenção
A intenção principal do padrão Factory Method é definir uma interface para criar um objeto, mas deixar as subclasses decidirem qual classe instanciar. O Factory Method permite adiar a instanciação para as subclasses.

#### Estrutura
O padrão Factory Method envolve as seguintes componentes principais:
- **Creator**: Classe abstrata que declara o método de fábrica.
- **ConcreteCreator**: Classe concreta que implementa o método de fábrica e retorna uma instância de ConcreteProduct.
- **Product**: Define a interface dos objetos que o método de fábrica cria.
- **ConcreteProduct**: Implementa a interface Product e é o objeto real que o método de fábrica cria.

#### Como Funciona
1. A classe Creator declara o método de fábrica que retorna um objeto do tipo Product.
2. As subclasses ConcreteCreator implementam esse método para produzir objetos que se conformam com a interface Product.
3. O código que usa o Creator nunca precisa saber a classe concreta do objeto que está sendo criado.

#### Vantagens
- **Flexibilidade**: Permite introduzir novas classes concretas sem alterar o código existente.
- **Desacoplamento**: O código cliente não depende das classes concretas, já que a criação de objetos é feita através de uma interface comum.

#### Exemplo
Imagine uma aplicação de desenho que pode criar diferentes tipos de formas, como círculos, quadrados, etc. Usando o Factory Method, você pode definir uma interface comum para criar uma forma e, em seguida, implementar subclasses específicas para cada tipo de forma. Isso permite adicionar novas formas à aplicação sem modificar o código existente.

#### Conclusão
O padrão Factory Method é uma ferramenta poderosa para promover a organização, flexibilidade e extensibilidade do código. É amplamente utilizado em bibliotecas e frameworks onde a implementação é esperada para ser estendida por aplicações cliente.

#### Exemplo

```python
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

########################## Saida ###########################################
# Service A health check
# Service A message errors
# Service B health check
# Service B message errors
# Service C health check
# Service C message errors

```
##### Referencia
[Factory Method](https://refactoring.guru/design-patterns/factory-method)
[Factory Method - python  ](https://refactoring.guru/design-patterns/factory-method/python/example)
[Um Programador Pleno já deveria saber usar esse Design Pattern (tutorial linha a linha)](https://youtu.be/arAz2Ff8s88)
[Combinação Extremamente Poderosa Para Qualquer Programador (Factory + Injeção de Dependência)](https://youtu.be/uyOJ2jjBtBs)




### Padrões Estruturais

## Padrões Comportamentais
