class Pessoa:
    def __init__(self, nome = None, idade = 27):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá{id(self)}'
if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) #mais usual
    print(p.nome)
    p.nome="Bruno"
    p.idade = 27
    print(p.idade)
