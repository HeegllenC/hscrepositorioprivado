# class Pessoa :
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade #construindo a pessoa(objeto)

#     def cumprimentar(self):
#         print(f"Ola, meu nome é {self.nome} e eu tenho {self.idade} anos.")


# Otto = Pessoa(nome = "Otto",idade = 25) #chamando o objeto criado
# print(Otto.cumprimentar()) #chamar como funçao


class Carro:
    def __init__(self,marca: str,modelo : str, ano: int ):
         self.marca = marca
         self.modelo = modelo #construindo a pessoa(objeto)
         self.ano = ano


    def ligar_motor (self):
        print(f"O motor do {self.marca} {self.modelo} {self.ano} foi ligado.")

    def desligar_motor (self):
        print(f"O motor do {self.marca} {self.modelo} {self.ano} foi desligado.")

carro3 = Carro(marca="Tesla", modelo="Y", ano=2025)
carro3.ligar_motor()
carro3.desligar_motor()
