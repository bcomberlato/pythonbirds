"""
    >>> Pessoa.olhos
    2
"""
class Pessoa:
    olhos = 2

    def __init__(self,*filhos , nome = None, idade = 27):
        self.idade = idade
        self.nome = nome
        self.filhos = (list(filhos))

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_classe = super().cumprimentar()
        return f'{cumprimentar_classe}. Aperto de mão'
class Mutante(Pessoa):
    olhos = 3
    pass



if __name__ == '__main__':

    renzo = Mutante(nome='Renzo')
    luciano = Homem(renzo, nome='Luciano')
    luciano.sobrenome = 'Ramalho'
    #print(Pessoa.cumprimentar(p))
    #print(id(p))
    #print(p.cumprimentar()) mais usual
    for filho in luciano.filhos:
        print(filho.nome)
    print(Pessoa.olhos)
    print(renzo.olhos)
    print(luciano.olhos)
    print(luciano.sobrenome)
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa,Homem))
    print(isinstance(luciano,Pessoa))
    print(isinstance(luciano,Homem))
    print(renzo.olhos)
    print(renzo.cumprimentar())
    print(luciano.cumprimentar())