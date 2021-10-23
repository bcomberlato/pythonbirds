"""
Você deve criar uma clsse carro que vai possuir dois atributos compostros por outras duas classes:
1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Metodo acelerar, que deverá incrementar a velocidade de uma unidade
3) Metodo frear, que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferecerá os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste e Oeste
2) Método girar_a_direita
    N
  O   L
    S
    >>>#Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>>motor.acelerar()
    >>> motor.velocidade
    1
    >>>motor.acelerar()
    >>> motor.velocidade
    2
    >>>motor.acelerar()
    >>> motor.velocidade
    3
    >>>motor.frear()
    >>> motor.velocidade
    1
    >>>motor.frear()
    >>> motor.velocidade
    0
    >>>#Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'norte'
    >>> carro.girar_a_direita
    >>> carro.calcular_direcao()
    'leste'
    >>> carro.girar_a_esquerda
    >>> carro.calcular_direcao()
    'norte'
"""