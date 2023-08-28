
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