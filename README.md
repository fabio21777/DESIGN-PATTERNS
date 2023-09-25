# Estudos sobre padrões de projetos

Este é apenas o resumo dos meus estudos iniciais sobre padrões de projeto. Os exemplos serão feitos em Python (estou aprendendo :)). Serão abordados todos os padrões descritos no livro; porém, haverá exemplos em Python apenas daqueles que julguei serem mais impactantes e mais comumente usados no meu dia a dia como programador em Java/JavaScript. As principais fontes de estudo foram [DESIGN PATTERNS -refactoring-guru](https://refactoring.guru/design-patterns) e 'Design Patterns: Elements of Reusable Object-Oriented Software'. Durante o meu estudo, pretendo visitar outros sites e vídeos.

## Introdução

### [Padrões Criacionais](#padrões-criacionais)


Os padrões criacionais se concentram em técnicas de criação de objetos, garantindo que os objetos sejam criados de maneira adequada para a situação.

1. **[Singleton](#singleton)**
2. **[Factory Method](#factory-method)**
3. **[Abstract Factory](#abstract-factory)**
4. **[Builder](#builder)**
5. **Prototype**

### [Padrões Estruturais](#padrões-estruturais)
Os padrões estruturais se concentram em como os objetos e classes são combinados para formar estruturas maiores.

1. **[Adapter](#adapter)**
2. **[Bridge](#bridge)**
3. **[Composite](#composite)**
4. **[Decorator](#decorator)**
5. **[Facade](#facade)**
6. **[Flyweight](#flyweight)**
7. **[Proxy](#proxy)**

### [Padrões Comportamentais](#padrões-comportamentais)
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




## Padrões Criacionais

### Singleton
### O que é:
O padrão Singleton é um padrão de design criacional que garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global a essa instância. É útil quando você quer garantir que uma classe seja instanciada apenas uma vez, por exemplo, para gerenciar conexões com um banco de dados ou um arquivo de configuração.

### Componentes principais:
1. **Singleton Class (Classe Singleton)**:
   - Uma classe que encapsula sua própria instância e garante que nenhuma outra instância possa ser criada.

### Pontos de Atenção:
1. **Global State**:
   - O padrão Singleton cria um estado global, o que pode ser problemático em sistemas complexos ou multithreaded.

2. **Testabilidade**:
   - Classes Singleton podem ser difíceis de testar devido à dificuldade de isolar o estado global.

3. **Violando o Princípio de Responsabilidade Única**:
   - A classe Singleton tem a responsabilidade de gerenciar sua instância e a lógica de negócios, violando o Princípio de Responsabilidade Única.

4. **Uso Indevido**:
   - O padrão Singleton pode ser usado indevidamente em situações onde não é necessário um controle tão estrito sobre as instâncias.

#### Exemplo

```python
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
```

### Factory Method

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

########################## Saida ###########################################
# Service A health check
# Service A message errors
# Service B health check
# Service B message errors
# Service C health check
# Service C message errors

```

#### Implementação do Factory Method
O padrão Factory Method é implementado através da interface **CreatorMessage** e suas subclasses concretas. A interface define um método abstrato **create_message**, que é o método de fábrica. As subclasses concretas implementam esse método para criar mensagens de erro específicas para cada serviço.

Os serviços (ServiceA/B/C) dependem da interface **CreatorMessage**, e não das classes concretas. Isso permite que os serviços sejam estendidos e modificados independentemente das regras de criação de mensagens de erro.
#### Referencia
[Factory Method](https://refactoring.guru/design-patterns/factory-method)
[Factory Method - python  ](https://refactoring.guru/design-patterns/factory-method/python/example)
[Um Programador Pleno já deveria saber usar esse Design Pattern (tutorial linha a linha)](https://youtu.be/arAz2Ff8s88)
[Combinação Extremamente Poderosa Para Qualquer Programador (Factory + Injeção de Dependência)](https://youtu.be/uyOJ2jjBtBs)

### Abstract Factory



#### Referencia
[Entenda DEFINITIVAMENTE o padrão Abstract Factory do GOF](https://youtu.be/_EcV-BcJ2-E)
[Abstract Factory Teoria - Padrões de Projeto - Parte 12/45](https://youtu.be/UPSuHqNsNs4)

### Builder


#### O que é:
O padrão Builder é um padrão de projeto de software criacional que permite a construção de objetos complexos passo a passo. Ele separa a construção de um objeto complexo de sua representação, de modo que o mesmo processo de construção possa criar diferentes representações.

#### Componentes principais:
1. **Builder**: Interface que define os métodos para construir as partes de um objeto complexo.
2. **ConcreteBuilder**: Implementa a interface Builder e constrói e monta as partes do produto, definindo e mantendo uma representação.
3. **Director**: Constrói um objeto usando a interface Builder.
4. **Product**: Representa o objeto complexo que está sendo construído. ConcreteBuilder constrói a representação interna do produto e define o processo de montagem.

#### Por que usar:
1. **Separação de Responsabilidades**: Separa a construção de um objeto complexo de sua representação.
2. **Flexibilidade**: Permite que um objeto seja construído em várias etapas e até mesmo com detalhes variados a cada construção.
3. **Criação de Objetos Complexos**: Facilita a criação de objetos que possuem muitos atributos ou que possuem uma sequência específica de etapas de construção.
4. **Reutilização**: O mesmo processo de construção pode criar diferentes representações.

#### Pontos de atenção:
1. **Complexidade Adicional**: Pode introduzir uma complexidade adicional ao código, pois divide a construção em várias classes.
2. **Necessidade**: Não deve ser usado se o objeto que você está tentando criar é simples e não requer uma configuração complexa.


#### Exemplo

```python
# Product
class Sandwich:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def show(self):
        print("Sanduíche com:", ", ".join(self.ingredients))

# Builder Interface
class SandwichBuilder:
    def add_meat(self):
        pass

    def add_vegetable(self):
        pass

    def add_condiment(self):
        pass

    def get_result(self):
        pass

# ConcreteBuilder
class ChickenSandwichBuilder(SandwichBuilder):
    def __init__(self):
        self.sandwich = Sandwich()

    def add_meat(self):
        self.sandwich.add_ingredient("Frango")

    def add_vegetable(self):
        self.sandwich.add_ingredient("Alface")

    def add_condiment(self):
        self.sandwich.add_ingredient("Maionese")

    def get_result(self):
        return self.sandwich

# ConcreteBuilder
class VeggieSandwichBuilder(SandwichBuilder):
    def __init__(self):
        self.sandwich = Sandwich()

    def add_vegetable(self):
        self.sandwich.add_ingredient("Tomate")
        self.sandwich.add_ingredient("Pepino")

    def add_condiment(self):
        self.sandwich.add_ingredient("Mostarda")

    def get_result(self):
        return self.sandwich

# Director
class SandwichDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_sandwich(self):
        self.builder.add_meat()
        self.builder.add_vegetable()
        self.builder.add_condiment()
        return self.builder.get_result()

# Client
chicken_builder = ChickenSandwichBuilder()
director = SandwichDirector(chicken_builder)
chicken_sandwich = director.make_sandwich()
chicken_sandwich.show()

veggie_builder = VeggieSandwichBuilder()
director = SandwichDirector(veggie_builder)
veggie_sandwich = director.make_sandwich()
veggie_sandwich.show()
```
#### Codigo
No exemplo implementamos o padrão **Builder** para criar sanduíches, incluindo todos os componentes principais do padrão:

1. **Builder**: Representado pela classe `SandwichBuilder`, que define uma interface para construir partes do sanduíche.
2. **ConcreteBuilder**: Temos dois construtores concretos: `ChickenSandwichBuilder` e `VeggieSandwichBuilder`. Eles implementam a interface `SandwichBuilder` e definem como construir um sanduíche de frango e um sanduíche veggie, respectivamente.
3. **Director**: Representado pela classe `SandwichDirector`, que aceita um `SandwichBuilder` e orquestra a construção do sanduíche.
4. **Product**: Representado pela classe `Sandwich`.

O cliente agora usa o `SandwichDirector` para construir os sanduíches, passando o construtor desejado ao diretor.

#### Referencia
[refactoring - Builder](https://refactoring.guru/design-patterns/builder)
[GOF BUILDER - Entenda de forma FÁCIL e OBJETIVA como ele funciona](https://youtu.be/dbw_BMHEgkY?si=0PW2mqz0XFbuVfMf)
[Design Pattern Builder na Prática](https://youtu.be/W-96z2EjoJ0?si=KUGBuEXcgEDSklNb)
## Padrões Estruturais

### Facade


#### O que é o Padrão Facade?
O padrão Facade fornece uma interface simplificada para um subsistema complexo. Ao fazer isso, ele oculta a complexidade desse subsistema de seus clientes, tornando-o mais fácil de ser utilizado.

#### Componentes principais
1. **Facade:** Esta é a classe principal que fornece métodos simplificados para os clientes. Ela conhece quais classes do subsistema são responsáveis por um pedido e delega esse pedido para os métodos apropriados dessas classes.
2. **Subsistema:** Estas são as classes que compõem o sistema mais complexo que o Facade está simplificando. As classes do subsistema realizam o trabalho real, mas o padrão Facade encapsula essa complexidade para tornar as coisas mais simples para o cliente.

#### Por que usar o Padrão Facade?
1. **Simplificação:** O padrão Facade torna sistemas complexos mais fáceis de serem usados, ao fornecer uma interface mais simples.
2. **Desacoplamento:** Os clientes não precisam conhecer os detalhes internos do subsistema. Isso permite uma separação entre a interface e a implementação.
3. **Flexibilidade:** Se a implementação interna do subsistema mudar, os clientes que usam o Facade provavelmente não serão afetados, desde que a interface do Facade permaneça consistente.
4. **Promove a reutilização:** Um subsistema é mais facilmente reutilizável quando existe uma interface Facade que simplifica sua operação.


#### Exemplo

```python
# Subsistemas
class Stock:
    def check_product_availability(self, product_id):
        # Aqui teríamos uma lógica real para verificar o estoque
        print(f"Verificando disponibilidade do produto {product_id}...")
        return True

class Payment:
    def process_payment(self, user, amount):
        # Lógica real de processamento de pagamento
        print(f"Processando pagamento de {user} no valor de {amount}...")
        return True

class Delivery:
    def organize_delivery(self, user, product_id):
        # Lógica real para organizar a entrega
        print(f"Organizando entrega do produto {product_id} para {user}...")
        return True

# Facade
class OrderFacade:
    def __init__(self):
        self.stock = Stock()
        self.payment = Payment()
        self.delivery = Delivery()

    def allProcess(self, user, product_id, amount):
        if not self.stock.check_product_availability(product_id):
            print("Produto indisponível!")
            return False

        if not self.payment.process_payment(user, amount):
            print("Falha no pagamento!")
            return False

        if not self.delivery.organize_delivery(user, product_id):
            print("Falha na organização da entrega!")
            return False

        print("Pedido realizado com sucesso!")
        return True

    def check_stock(self, product_id):
	    return self.stock.check_product_availability(product_id)

    def process_payment(self, user, amount):
        return self.payment.process_payment(user, amount)

    def organize_delivery(self, user, product_id):
        return self.delivery.organize_delivery(user, product_id)

# Cliente
if __name__ == "__main__":
    order_system = OrderFacade()
    #order_system.allProcess("João", "12345", 100)
    order_system.check_stock("12345")
    order_system.process_payment("João", 100);
    order_system.organize_delivery("João", "12345")

```

#### Código
Caso seja necessário modificar a implementação de **check_product_availability** ou de qualquer outro método, desde que o nome do método não seja alterado, a funcionalidade geral continuará a operar sem problemas. O padrão Facade pode ser entendido como um intermediário na comunicação entre módulos. É semelhante a uma biblioteca que disponibiliza diferentes interfaces (métodos) públicos. Essas interfaces servem como pontos de comunicação para os clientes, simplificando a interação com subsistemas mais complexos por trás dessas interfaces.

#### Ponto de **Atenção**
Esse carinha, o padrão Facade, parece ser bem legal, né? Mas, vamos jogar um cenário aí: se a gente tivesse um subsistema recheado de classes, tipo, centenas delas, nossa facade poderia virar uma verdadeira colossus! Isso poderia nos levar diretinho a criar uma God Class, sabe? Uma daquelas classes que tentam fazer tudo ao mesmo tempo. Isso pode complicar um bocado as coisas quando a gente tenta entender ou manter o código

##### Referencia
[refactoring - Facade](https://refactoring.guru/pt-br/design-patterns/facade)

## Padrões Comportamentais

### strategy

#### O que é o Strategy Pattern?

O **Strategy Pattern** define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. O padrão permite que o algoritmo varie independentemente dos clientes que o utilizam. Em outras palavras, ele permite que você separe um conjunto de algoritmos da classe que os utiliza, para que a classe e os algoritmos possam variar independentemente.

#### Componentes principais do Strategy Pattern:

1. **Strategy (Estratégia)**: Esta é uma interface ou uma classe abstrata usada para definir uma família de algoritmos.
2. **Concrete Strategies (Estratégias Concretas)**: Estas são as implementações específicas da estratégia. Cada uma implementa um algoritmo diferente.
3. **Context (Contexto)**: O Contexto mantém uma referência a uma estratégia e pode alternar entre diferentes estratégias. Ele usa a estratégia para executar uma operação.

#### Por que usar o Strategy Pattern?

1. **Flexibilidade**: O Strategy Pattern permite que você defina uma família de algoritmos e os torne intercambiáveis. Isso significa que você pode alterar o comportamento de um programa em tempo de execução, escolhendo diferentes estratégias.
2. **Separação de Responsabilidades**: O padrão separa o código que usa o algoritmo do código que implementa o algoritmo. Isso torna o código mais modular e fácil de estender.
3. **Evita Condições Múltiplas**: Em vez de usar várias condicionais para escolher qual algoritmo usar, você pode encapsular o algoritmo em uma estratégia e simplesmente mudar a estratégia.

#### Exemplo

#### Exemplo: Calculadora de Descontos

```python
from abc import ABC, abstractmethod

# Estratégia abstrata
class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass

# Estratégia concreta 1: Desconto fixo de $10
class FixedDiscount(DiscountStrategy):

    def apply_discount(self, price: float) -> float:
        return price - 10

# Estratégia concreta 2: Desconto de 10%
class PercentageDiscount(DiscountStrategy):

    def apply_discount(self, price: float) -> float:
        return price * 0.9

# Contexto
class Product:

    def __init__(self, name: str, price: float, discount_strategy: DiscountStrategy):
        self.name = name
        self.price = price
        self.discount_strategy = discount_strategy

    def get_discounted_price(self) -> float:
        return self.discount_strategy.apply_discount(self.price)

# Testando
product1 = Product("Camiseta", 50, FixedDiscount())
print(f"Preço com desconto para {product1.name}: ${product1.get_discounted_price()}")

product2 = Product("Tênis", 100, PercentageDiscount())
print(f"Preço com desconto para {product2.name}: ${product2.get_discounted_price()}")


```

Imagine que você está desenvolvendo um sistema de e-commerce e deseja aplicar diferentes estratégias de desconto aos produtos. Algumas estratégias podem oferecer um desconto fixo, outras um desconto percentual, e assim por diante.

1. **DiscountStrategy (Estratégia de Desconto)**: Esta é a estratégia abstrata que define o método `apply_discount`, que todas as estratégias concretas devem implementar.

2. **FixedDiscount e PercentageDiscount (Descontos Fixo e Percentual)**: Estas são as estratégias concretas que fornecem implementações específicas para o método `apply_discount`. `FixedDiscount` subtrai um valor fixo do preço, enquanto `PercentageDiscount` aplica um desconto percentual.

3. **Product (Produto)**: Esta é a classe contexto. Ela representa um produto que tem um nome, um preço e uma estratégia de desconto. A classe `Product` usa a estratégia de desconto para calcular o preço com desconto através do método `get_discounted_price`.

Ao usar o **Strategy Pattern** neste exemplo, você pode facilmente adicionar novas estratégias de desconto no futuro sem modificar o código existente. Por exemplo, se você quiser adicionar uma estratégia de "compre um, leve o segundo pela metade do preço", basta criar uma nova classe que implemente `DiscountStrategy` e aplicá-la ao produto desejado.

#### Referencia

[Strategy](https://refactoring.guru/design-patterns/strategy)
[Identifique Quando e Como Usar o Design Pattern Strategy na Prática](https://youtu.be/WPdrnuSHAQs)
[Design Pattern Strategy: Entendendo na Prática](https://youtu.be/pxmqkzWPW6E)

### Chain of Responsibility

O padrão Chain of Responsibility permite que uma solicitação seja passada ao longo de uma cadeia de potenciais manipuladores até que um deles lide com a solicitação.

#### Componentes principais:
- **Handler (Manipulador):** Interface que define os métodos que todos os handlers devem implementar.
- **AbstractHandler:** Classe concreta que implementa a lógica padrão para encadear os handlers e passar a solicitação ao longo da cadeia.
- **ConcreteHandlers (Manipuladores Concretos):** Classes que implementam a lógica específica para lidar com as solicitações.

#### Funcionamento:
1. Uma solicitação é passada para o primeiro handler da cadeia.
2. Se o handler pode processar a solicitação, ele faz isso e a cadeia termina.
3. Se o handler não pode processar a solicitação, ele passa para o próximo handler na cadeia.
4. O processo se repete até que um handler processe a solicitação ou até que todos os handlers tenham sido tentados.

#### Exemplo
Imagine um sistema de suporte técnico onde diferentes níveis de suporte lidam com problemas de diferentes complexidades. Se um nível não pode resolver o problema, ele é passado para o próximo nível. No código fornecido, temos três níveis de suporte (`SuporteNivel1`, `SuporteNivel2` e `SuporteNivel3`) que tentam resolver problemas de diferentes complexidades.

```python
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


```
### Template Method

#### O que é o Padrão Template Method?
O padrão Template Method faz parte dos padrões de design comportamentais e define o esqueleto de um algoritmo em uma operação, adiando alguns passos para as subclasses. Ele permite que as subclasses redefinam certas etapas de um algoritmo sem alterar sua estrutura.

#### Componentes Principais:

1. **AbstractClass**:
    - Esta é a classe base que define e implementa o "template method". Este método é composto por uma série de passos para executar o algoritmo. Alguns desses passos podem ser concretos (com uma implementação padrão) e outros podem ser abstratos, deixando para as subclasses a responsabilidade de sua implementação.
    - Contém métodos abstratos (operacionalizações primitivas) que as subclasses devem implementar.

2. **ConcreteClass**:
    - Estas são subclasses da AbstractClass e implementam os métodos abstratos deixados indefinidos na classe base.
    - Fornecem a implementação específica para os passos abstratos do algoritmo.

#### Por que usar?

1. **Promove a Reutilização de Código**: Ao isolar as partes invariáveis de um algoritmo na classe base e deixar as partes variáveis para as subclasses, evita-se a duplicação de código.
2. **Flexibilidade**: Oferece um framework onde as subclasses podem definir como algumas etapas do algoritmo devem ser realizadas, sem alterar a estrutura geral do algoritmo.
3. **Inversão de Controle**: Ao contrário de usar herança direta, onde as subclasses podem inadvertidamente alterar partes do algoritmo, o Template Method garante que a estrutura do algoritmo permaneça inalterada, enquanto permite que as subclasses mudem apenas as partes que precisam ser personalizadas.


#### Exemplo

```python

class AbstractRecipe:
    """Classe abstrata que define a estrutura do método template."""

    def execute(self):
        """Método template que define a sequência de passos."""
        self.prepare()
        self.cook()
        self.finalize()
        self.common_method()

    def prepare(self):
        """Preparação dos ingredientes. Deve ser implementado por subclasses."""
        raise NotImplementedError

    def cook(self):
        """Processo de cozimento. Deve ser implementado por subclasses."""
        raise NotImplementedError

    def finalize(self):
        """Finalização da receita. Deve ser implementado por subclasses."""
        raise NotImplementedError

    def common_method(self):
        """Método comum para todas as subclasses."""
        print("Desfrute da sua refeição!")

class SpaghettiRecipe(AbstractRecipe):
    """Subclasse que implementa os métodos abstratos para uma receita de espaguete."""

    def prepare(self):
        print("Preparando os ingredientes para o espaguete.")

    def cook(self):
        print("Cozinhando o espaguete em água fervente.")

    def finalize(self):
        print("Finalizando com molho e queijo.")

class SoupRecipe(AbstractRecipe):
    """Subclasse que implementa os métodos abstratos para uma receita de sopa."""

    def prepare(self):
        print("Preparando os ingredientes para a sopa.")

    def cook(self):
        print("Fervendo os ingredientes.")

    def finalize(self):
        print("Finalizando com temperos e servindo quente.")

if __name__ == "__main__":
    print("Receita de Espaguete:")
    recipe1 = SpaghettiRecipe()
    recipe1.execute()

    print("\nReceita de Sopa:")
    recipe2 = SoupRecipe()
    recipe2.execute()
```


#### Por que não usar?

1. **Limitações na Personalização**: Enquanto o Template Method permite que as subclasses alterem partes do algoritmo, elas ainda estão limitadas à estrutura definida na classe base. Se uma subclasse precisar de uma sequência radicalmente diferente de operações, o Template Method pode não ser o melhor padrão a ser usado.
2. **Pode Levar a Muitas Subclasses**: Se cada variação do algoritmo exigir uma nova subclasse, pode-se acabar com muitas subclasses pequenas que são difíceis de gerenciar.
3. **Acoplamento**: Como as subclasses dependem da classe base, qualquer alteração na classe base pode ter efeitos colaterais nas subclasses, levando a problemas de manutenção.

Em resumo, enquanto o padrão Template Method é poderoso e útil em muitos cenários, é importante considerar as necessidades específicas do sistema e os trade-offs envolvidos antes de decidir usá-lo.

### Command

O padrão **Command** é um padrão de design comportamental que transforma uma solicitação em um objeto autônomo que contém informações sobre a solicitação. Isso permite que os parâmetros sejam passados, enfileirados, registrados ou executados em diferentes momentos.

#### O que é:
O padrão Command encapsula uma solicitação como um objeto, permitindo que os usuários parametrizem clientes com diferentes solicitações, enfileirem solicitações, registrem o log de solicitações e suportem operações reversíveis.

#### Componentes Principais:
1. **Command**: Declara uma interface para executar uma operação.
2. **ConcreteCommand**: Define um vínculo entre o objeto Receiver e a ação. Implementa o método `execute` invocando a(s) operação(ões) correspondente(s) no Receiver.
3. **Client**: Cria um objeto ConcreteCommand e define seu receptor.
4. **Invoker**: Solicita que o comando seja executado.
5. **Receiver**: Sabe como realizar as operações associadas a uma solicitação. Qualquer classe pode atuar como Receiver.

#### Por que usar:
- **Desacoplamento**: Separa objetos que invocam operações dos objetos que realmente executam essas operações.
- **Flexibilidade**: Permite que comandos sejam enfileirados, revertidos ou registrados.
- **Extensibilidade**: Novos comandos podem ser adicionados sem alterar o código existente.

#### Exemplo

```python
# Receiver
class Database:
    def __init__(self):
        self.data = []

    def insert_record(self, record):
        self.data.append(record)
        print(f"Registro '{record}' inserido.")

    def delete_record(self, record):
        if record in self.data:
            self.data.remove(record)
            print(f"Registro '{record}' deletado.")
        else:
            print(f"Registro '{record}' não encontrado.")

# Command Interface
class Command:
    def execute(self):
        pass

# ConcreteCommand
class InsertCommand(Command):
    def __init__(self, database, record):
        self.database = database
        self.record = record

    def execute(self):
        self.database.insert_record(self.record)

# ConcreteCommand
class DeleteCommand(Command):
    def __init__(self, database, record):
        self.database = database
        self.record = record

    def execute(self):
        self.database.delete_record(self.record)

# Invoker
class DatabaseInvoker:
    def __init__(self, command):
        self.command = command

    def call(self):
        self.command.execute()

# Client
db = Database()
insert_cmd = InsertCommand(db, "Registro1")
delete_cmd = DeleteCommand(db, "Registro1")

invoker = DatabaseInvoker(insert_cmd)
invoker.call()

invoker = DatabaseInvoker(delete_cmd)
invoker.call()

```
#### Código

- **Database**: É o `Receiver`, responsável por realizar as operações reais de inserir e deletar registros.
- **Command**: É a interface que declara o método `execute`.
- **InsertCommand** e **DeleteCommand**: São os `ConcreteCommands` que encapsulam a ação a ser executada.
- **DatabaseInvoker**: É o `Invoker` que invoca o comando.
- **Client**: Cria os comandos e os invoca através do invoker.

#### Pontos de atenção:
- **Complexidade**: Pode aumentar a complexidade do código ao introduzir várias classes e objetos.
- **Overhead**: Cada comando é uma classe separada, o que pode resultar em um overhead se houver muitos comandos simples.
- **Reversão**: Nem todos os comandos são reversíveis. Se a funcionalidade de desfazer for necessária, é preciso implementar cuidadosamente.

Ao usar o padrão Command, é importante garantir que o sistema permaneça claro e não se torne excessivamente complexo com a introdução de muitos comandos específicos.

#### Referencias
[refactoring guru Command](https://refactoring.guru/pt-br/design-patterns/command)


### Padrão de Design Iterator

#### O que é?
O padrão Iterator, conforme definido pelo GoF, fornece uma maneira de acessar os elementos de uma coleção de objetos sequencialmente sem expor sua representação subjacente. Ele encapsula os detalhes da iteração, permitindo que os clientes percorram a coleção sem conhecer sua estrutura interna.

#### Estrutura
- **Iterator**: Define uma interface para acessar e percorrer elementos.
- **ConcreteIterator**: Implementa a interface do Iterator e mantém a posição de iteração atual na coleção.
- **Aggregate**: Define uma interface para criar um objeto Iterator.
- **ConcreteAggregate**: Implementa a interface do Aggregate e retorna uma instância do ConcreteIterator.

#### Onde Usar?
1. Quando você quer fornecer uma maneira uniforme de acessar diferentes estruturas de coleções.
2. Quando você quer permitir o acesso sequencial a uma coleção sem expor seus detalhes internos.
3. Quando você quer fornecer múltiplas formas de percorrer uma coleção complexa.

#### Pontos de Atenção
1. A complexidade adicional: Implementar o padrão Iterator pode adicionar uma camada extra de complexidade ao seu código.
2. Manter a sincronização com a coleção: É importante garantir que o iterador esteja sincronizado com a coleção, especialmente se a coleção pode ser modificada durante a iteração.
3. Performance: Dependendo da implementação, pode haver uma ligeira degradação no desempenho, especialmente se o iterador realizar operações complexas durante a iteração.


#### Exemplo

```python
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

```
#### codigo

- `Iterator` e `Aggregate` são classes abstratas que definem as interfaces para os iteradores e agregados, respectivamente.
- `ConcreteAggregate` é uma coleção de itens que pode criar dois tipos de iteradores: `ForwardIterator` e `BackwardIterator`.
- `ForwardIterator` é um iterador que percorre os itens na coleção `ConcreteAggregate` da frente para trás.
- `BackwardIterator` é um iterador que percorre os itens na coleção `ConcreteAggregate` de trás para frente.



#### Referencias
[refactoring guru iterator](https://refactoring.guru/design-patterns/iterator)

### Mediator

#### O que é:

O padrão Mediator é um padrão de design comportamental que visa reduzir as conexões entre classes ou objetos múltiplos, centralizando as comunicações externas. Isso ajuda a diminuir a dependência mútua entre classes, promovendo um acoplamento mais fraco e um código mais limpo e modular.

#### Componentes Principais:

1. **Mediator Interface**: Define a interface para a comunicação entre objetos colegas (Colleague Objects).
2. **Concrete Mediator**: Implementa a interface do mediator e coordena a comunicação entre objetos colegas. Ele conhece e mantém um rastreamento de seus colegas.
3. **Colleague Classes**: Classes que comunicam-se entre si através do mediator, em vez de se comunicarem diretamente umas com as outras.

#### Por que usar:

1. **Redução de Acoplamento**: Ajuda a reduzir o acoplamento entre classes, facilitando a manutenção e a expansão do sistema.
2. **Centralização da Comunicação**: Centraliza a comunicação, facilitando o rastreamento e a gestão das interações entre objetos.
3. **Promove a Reutilização de Objetos**: Ao desacoplar os objetos, promove a reutilização de objetos, já que eles não estão diretamente interligados.
4. **Simplicidade na Organização de Objetos**: Simplifica a organização de objetos e relações, tornando o sistema mais compreensível e gerenciável.
5. **Flexibilidade na Definição de Comunicações**: Permite uma maior flexibilidade na definição de como os objetos se comunicam, facilitando ajustes e modificações futuras.

#### codigo

```python
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

```
#### Referencias
[refactoring guru mediator](https://refactoring.guru/design-patterns/mediator)


### Observer

#### O que é:
O padrão Observer é um padrão de design comportamental que define uma dependência um-para-muitos entre objetos, de forma que, quando o estado de um objeto (sujeito) muda, todos os seus dependentes (observadores) são automaticamente notificados e atualizados. Este padrão é amplamente utilizado para implementar sistemas distribuídos e reativos.

#### Componentes principais:
1. **Sujeito (Subject)**: O objeto que mantém uma lista de seus observadores e notifica-os automaticamente de quaisquer mudanças de estado, geralmente por meio de um dos seus métodos.
   
2. **Observador (Observer)**: A interface ou classe abstrata que define os métodos de notificação que devem ser implementados pelos observadores concretos.

3. **Observador Concreto (Concrete Observer)**: Classes que implementam a interface do observador e respondem às notificações do sujeito.

#### Pontos de atenção:
1. **Notificações em Cascata**: Mudanças no sujeito podem causar uma série de notificações, o que pode resultar em atualizações complexas e potencialmente ineficientes.
   
2. **Desempenho**: Se houver muitos observadores ou as operações de atualização forem complexas, pode haver problemas de desempenho.

3. **Manutenção da Lista de Observadores**: O sujeito precisa gerenciar a lista de observadores de forma eficaz, permitindo adições e remoções dinâmicas.

4. **Acoplamento**: Embora o padrão promova a separação de preocupações, pode haver um certo nível de acoplamento entre o sujeito e os observadores, já que os observadores precisam ser notificados sobre as mudanças no sujeito.

#### Exemplo

``` python
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

```
### State

### O que é:
O padrão State é um padrão de design comportamental que permite a um objeto alterar seu comportamento quando seu estado interno muda. Isso é como se o objeto mudasse de classe. Esse padrão é útil quando um objeto tem comportamentos que dependem do seu estado, e deve ser capaz de mudar seu comportamento em tempo de execução de acordo com o novo estado.

### Componentes Principais:
1. **Interface de Estado (State Interface)**:
   - Define uma interface para encapsular o comportamento associado a um estado particular do objeto Contexto.
   
2. **Classes de Estado Concretas (Concrete State Classes)**:
   - Implementam a interface de Estado e fornecem a implementação específica para os comportamentos do estado.
   
3. **Contexto (Context)**:
   - Mantém uma referência ao estado atual e pode mudar para diferentes estados. O contexto passa a si mesmo para os estados para permitir que o estado acesse seus dados e métodos.

### Pontos de Atenção:
1. **Manutenção**:
   - O padrão State pode resultar em muitas classes de estado concreto, o que pode ser difícil de manter e entender.
   
2. **Transições de Estado**:
   - As transições entre estados devem ser claramente definidas e controladas para evitar comportamentos inesperados.
   
3. **Encapsulamento**:
   - O padrão State pode violar o princípio do encapsulamento ao expor estados específicos. É importante garantir que o encapsulamento seja mantido tanto quanto possível.

4. **Dependências**:
   - Se os estados precisarem comunicar-se entre si ou com o contexto, isso pode introduzir dependências que podem ser difíceis de gerenciar.

5. **Performance**:
   - Se houver muitas transições de estado em um curto período de tempo, isso pode afetar a performance do sistema.

O padrão State é uma maneira eficaz de modelar sistemas com comportamentos complexos e estados, mas deve ser usado com cuidado, especialmente em sistemas com um grande número de estados e transições.

### Codigo
```python 
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

```
### Visitor 

### O que é:
O padrão Visitor é um padrão de design comportamental que permite adicionar operações adicionais em objetos sem ter que modificá-los. Isso é útil quando você tem uma estrutura de objetos estável com operações que podem mudar frequentemente.

### Componentes Principais:
1. **Visitor (Visitante)**:
   - Uma interface ou classe abstrata que declara um método de visita para cada tipo de elemento concreto na estrutura do objeto.

2. **ConcreteVisitor (Visitante Concreto)**:
   - Classes que implementam a interface Visitor e fornecem a implementação específica para os métodos de visita.

3. **Element (Elemento)**:
   - Uma interface ou classe abstrata que declara um método de aceitação (`accept`) que aceita um objeto visitor como argumento.

4. **ConcreteElement (Elemento Concreto)**:
   - Classes que implementam a interface Element e fornecem a implementação específica para o método de aceitação.

5. **ObjectStructure (Estrutura de Objeto)**:
   - Uma classe que agrupa os elementos concretos e permite que os visitantes visitem os elementos.

### Pontos de Atenção:
1. **Acoplamento**:
   - O padrão Visitor pode introduzir um acoplamento forte entre os elementos e os visitantes, o que pode ser problemático se a estrutura do objeto ou os visitantes mudarem frequentemente.

2. **Quebra de Encapsulamento**:
   - Os visitantes precisam acessar os dados internos dos elementos, o que pode quebrar o encapsulamento.

3. **Complexidade**:
   - O padrão pode se tornar complexo se a estrutura do objeto tiver muitos tipos de elementos ou se muitas operações diferentes forem necessárias.

4. **Extensibilidade**:
   - Adicionar novos tipos de elementos pode ser difícil, pois isso requer a modificação de todas as classes de visitantes existentes para adicionar novos métodos de visita.

### Codigo 

```python 
from abc import ABC, abstractmethod

class AnimalVisitor:
    def visit(self, animal):
        pass

class SoundVisitor(AnimalVisitor):
    def visit(self, animal):
        animal.make_sound()

class FeedVisitor(AnimalVisitor):
    def visit(self, animal):
        animal.eat()

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def accept(self, visitor):
        visitor.visit(self)

class Dog(Animal):
    def make_sound(self):
        print("Au au!")

    def eat(self):
        print("O cachorro está comendo.")

class Cat(Animal):
    def make_sound(self):
        print("Miau!")

    def eat(self):
        print("O gato está comendo.")

# Criando animais
dog = Dog()
cat = Cat()

# Criando visitantes
sound_visitor = SoundVisitor()
feed_visitor = FeedVisitor()

# Fazendo os animais emitirem sons
dog.accept(sound_visitor)  # Output: Au au!
cat.accept(sound_visitor)  # Output: Miau!

# Alimentando os animais
dog.accept(feed_visitor)  # Output: O cachorro está comendo.
cat.accept(feed_visitor)  # Output: O gato está comendo.
 
```
