# Estudos sobre padrões de projetos

Este é apenas o resumo dos meus estudos iniciais sobre padrões de projeto. Os exemplos serão feitos em Python (estou aprendendo :)). Serão abordados todos os padrões descritos no livro; porém, haverá exemplos em Python apenas daqueles que julguei serem mais impactantes e mais comumente usados no meu dia a dia como programador em Java/JavaScript. As principais fontes de estudo foram [DESIGN PATTERNS -refactoring-guru](https://refactoring.guru/design-patterns) e 'Design Patterns: Elements of Reusable Object-Oriented Software'. Durante o meu estudo, pretendo visitar outros sites e vídeos.

## Introdução

### Padrões Criacionais
Os padrões criacionais se concentram em técnicas de criação de objetos, garantindo que os objetos sejam criados de maneira adequada para a situação.

1. **Singleton**
2. **[Factory Method](#factory-method)**
3. **[Abstract Factory](#abstract-factory)**
4. **[Builder](#builder)**
5. **Prototype**

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
##### Referencia
[Factory Method](https://refactoring.guru/design-patterns/factory-method)
[Factory Method - python  ](https://refactoring.guru/design-patterns/factory-method/python/example)
[Um Programador Pleno já deveria saber usar esse Design Pattern (tutorial linha a linha)](https://youtu.be/arAz2Ff8s88)
[Combinação Extremamente Poderosa Para Qualquer Programador (Factory + Injeção de Dependência)](https://youtu.be/uyOJ2jjBtBs)

### Abstract Factory



##### Referencia
[Entenda DEFINITIVAMENTE o padrão Abstract Factory do GOF](https://youtu.be/_EcV-BcJ2-E)
[Abstract Factory Teoria - Padrões de Projeto - Parte 12/45](https://youtu.be/UPSuHqNsNs4)

#### Builder


### O que é:
O padrão Builder é um padrão de projeto de software criacional que permite a construção de objetos complexos passo a passo. Ele separa a construção de um objeto complexo de sua representação, de modo que o mesmo processo de construção possa criar diferentes representações.

### Componentes principais:
1. **Builder**: Interface que define os métodos para construir as partes de um objeto complexo.
2. **ConcreteBuilder**: Implementa a interface Builder e constrói e monta as partes do produto, definindo e mantendo uma representação.
3. **Director**: Constrói um objeto usando a interface Builder.
4. **Product**: Representa o objeto complexo que está sendo construído. ConcreteBuilder constrói a representação interna do produto e define o processo de montagem.

### Por que usar:
1. **Separação de Responsabilidades**: Separa a construção de um objeto complexo de sua representação.
2. **Flexibilidade**: Permite que um objeto seja construído em várias etapas e até mesmo com detalhes variados a cada construção.
3. **Criação de Objetos Complexos**: Facilita a criação de objetos que possuem muitos atributos ou que possuem uma sequência específica de etapas de construção.
4. **Reutilização**: O mesmo processo de construção pode criar diferentes representações.

### Pontos de atenção:
1. **Complexidade Adicional**: Pode introduzir uma complexidade adicional ao código, pois divide a construção em várias classes.
2. **Necessidade**: Não deve ser usado se o objeto que você está tentando criar é simples e não requer uma configuração complexa.


##### Referencia
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

##### Exemplo: Calculadora de Descontos

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

##### Referencia

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
