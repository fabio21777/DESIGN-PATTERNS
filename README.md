# Estudos sobre padrões de projetos

Este é apenas o resumo dos meus estudos iniciais sobre padrões de projeto. Os exemplos serão feitos em Python (estou aprendendo :)). Serão abordados todos os padrões descritos no livro; porém, haverá exemplos em Python apenas daqueles que julguei serem mais impactantes e mais comumente usados no meu dia a dia como programador em Java/JavaScript. As principais fontes de estudo foram [DESIGN PATTERNS -refactoring-guru](https://refactoring.guru/design-patterns) e 'Design Patterns: Elements of Reusable Object-Oriented Software'. Durante o meu estudo, pretendo visitar outros sites e vídeos.

## Introdução

### Padrões Criacionais
Os padrões criacionais se concentram em técnicas de criação de objetos, garantindo que os objetos sejam criados de maneira adequada para a situação. Eles ajudam a gerenciar a criação de objetos, tornando o sistema mais independente de como seus objetos são criados e representados.

1. **Singleton**: Este padrão garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global a essa instância. É útil quando você quer garantir que uma classe controle o acesso aos recursos, como um único ponto de configuração ou um pool de conexões.
2. **Factory Method**: Permite que uma classe delegue a responsabilidade de instanciar seus objetos a subclasses. Isso é útil quando uma classe não pode antecipar o tipo de objetos que precisa criar.
3. **Abstract Factory**: Fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas. É como uma fábrica de fábricas.
4. **Builder**: Separa a construção de um objeto complexo de sua representação, permitindo que o mesmo processo de construção crie diferentes representações. É útil quando um objeto precisa ser criado com muitas opções possíveis de configuração.
5. **Prototype**: Permite criar um objeto totalmente funcional clonando um objeto existente. É útil quando a criação de uma instância é mais cara do que clonar uma existente.

### Padrões Estruturais
Os padrões estruturais se concentram em como os objetos e classes são combinados para formar estruturas maiores. Eles ajudam a garantir que, quando uma parte do sistema muda, o sistema inteiro não precisa ser alterado.

1. **Adapter**: Converte a interface de uma classe em outra interface que o cliente espera. É como um tradutor entre duas interfaces incompatíveis.
2. **Bridge**: Desacopla uma abstração de sua implementação para que ambas possam variar independentemente. É útil quando abstrações e implementações devem ser extensíveis independentemente.
3. **Composite**: Permite tratar objetos individuais e composições de objetos de maneira uniforme. É útil para representar hierarquias de objetos.
4. **Decorator**: Adiciona responsabilidades adicionais a um objeto dinamicamente. É uma alternativa flexível à subclasse para estender a funcionalidade.
5. **Facade**: Fornece uma interface simplificada para um conjunto de interfaces em um subsistema. É como uma interface unificada para um conjunto de operações.
6. **Flyweight**: Usa compartilhamento para suportar eficientemente grandes quantidades de objetos finos. É útil quando muitos objetos compartilham propriedades comuns e podem ser referenciados em vez de replicados.
7. **Proxy**: Fornece um substituto ou espaço reservado para outro objeto controlar o acesso a ele. Pode ser usado para adicionar uma camada entre o cliente e o objeto real.

### Padrões Comportamentais
Os padrões comportamentais se concentram na comunicação entre objetos, como os objetos são feitos para interagir uns com os outros. Eles ajudam a garantir que os componentes do sistema atuem juntos, mantendo a flexibilidade e eficiência.

1. **Chain of Responsibility**: Permite que mais de um objeto processe uma solicitação. A solicitação é passada ao longo de uma cadeia de objetos até que um deles a processe.
2. **Command**: Encapsula uma solicitação como um objeto, permitindo que os usuários parametrizem objetos com operações, enfileirem solicitações e registrem as operações.
3. **Interpreter**: Fornece uma maneira de avaliar sentenças em uma linguagem. É útil para interpretar linguagens de domínio específico.
4. **Iterator**: Fornece uma maneira de acessar os elementos de uma coleção de objetos sequencialmente sem expor sua representação subjacente.
5. **Mediator**: Define um objeto que encapsula como um conjunto de objetos interage. É útil para reduzir as dependências entre classes.
6. **Memento**: Captura e externaliza o estado interno de um objeto sem violar o encapsulamento. É útil para implementar pontos de verificação e desfazer funcionalidades.
7. **Observer**: Define uma dependência um-para-muitos entre objetos para que, quando um objeto muda de estado, todos os seus dependentes sejam notificados e atualizados automaticamente.
8. **State**: Permite que um objeto altere seu comportamento quando seu estado interno muda. É como se o objeto mudasse de classe.
9. **Strategy**: Define uma família de algoritmos, encapsula cada um e os torna intercambiáveis. Permite que o algoritmo varie independentemente dos clientes que o utilizam
10. **Template Method**: Define o esqueleto de um algoritmo em uma operação, adiando alguns passos para as subclasses. Permite que subclasses redefinam certos passos de um algoritmo sem alterar sua estrutura.
11. **Visitor**:Representa uma operação a ser executada nos elementos de uma estrutura de objeto. Permite adicionar novas operações sem alterar as classes dos elementos nos quais opera.

## Explorando mais detalhadamente os padrões de projetos.

### Padrões Criacionais

### Padrões Estruturais

## Padrões Comportamentais
