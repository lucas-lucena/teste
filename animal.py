class Animal():
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def desc(self):
        return f'{self.nome} é um animal da especie {self.especie}'

class Passaro(Animal):
    def __init__(self, nome, especie, cor):
        super().__init__(nome, especie)
        self.cor = None

    def desc(self):
        return f'{self.nome} é um passaro da espécie {self.especie} e é da cor {self.cor}'

class Peixe(Animal):
    def __init__(self, nome, especie):
        super().__init__(nome, especie)
    def desc(self):
        return f'{self.nome} é um peixe da especie {self.especie} e vive em um cardume'


bird = Passaro('Bento', 'João de Barro', 'Cinza')
print(bird.desc())
print(type(bird))

fish = Peixe('Blue', 'Bagre')
print(fish.desc())
print(type(fish))

dog = Animal('Mel', 'Goldren retriever')
print(dog.desc())
print(type(dog))
