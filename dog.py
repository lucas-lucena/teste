from random import random

class cachorro():
        def __init__(self, nome, raca, idade):
            self.nome = nome
            self.raca = raca
            self.idade = idade

        def desc(self):
            return f'{self.nome} é um cachorro da raça {self.raca}'
        def bark(self):
            return 'Wolf wolf'
        
        def sit(self):
            return 'O cachorro sentou'
        
        def lay(self):
            return 'O cachorro deitou'

cachorro1 = cachorro('Harry','Maltês',10)
print(cachorro1.desc())

print('Agora vamos montar um cachorro!')
dog2_nome = input('Qual o nome do seu cachorro? \n')
dog2_raca = input('Qual a raça do seu cachorro? \n')
dog2_idade= input('Qual a idade do seu cachorro? \n')

cachorro2 = cachorro(dog2_nome, dog2_raca, dog2_idade)
print(cachorro2.desc())
print(cachorro2.bark())

