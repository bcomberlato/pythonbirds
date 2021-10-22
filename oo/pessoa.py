class Pessoa:
    olhos = 2

    def __init__(self,*filhos , nome = None, idade = 27):
        self.idade = idade
        self.nome = nome
        self.filhos = (list(filhos))

    def cumprimentar(self):
        return f'Olá{id(self)}'

if __name__ == '__main__':

    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
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