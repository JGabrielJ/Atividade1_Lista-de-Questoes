def dormir(dia_semana: bool, feriado: bool) -> bool:
    """
    dia_semana é True para dias na semana
    feriado é True nos feriados

    Você pode ficar dormindo quando é feriado ou não é dia da semana.
    Retorne True ou False conforme você vá dormir ou não.
    """

    return True if feriado or not dia_semana else False


def alunos_problema(a_sorri: bool, b_sorri: bool) -> bool:
    """
    temos dois alunos a e b
    a_sorri e b_sorri indicam se a e b sorriem

    Temos problemas quando ambos estão sorrindo ou ambos não estão sorrindo
    Retorne True quando houver problemas
    """

    return True if (a_sorri and b_sorri) or (not a_sorri and not b_sorri) else False


def soma_dobro(a: int, b: int) -> int:
    """
    Dados dois números inteiros, retorne sua soma.
    Porém, se os números forem iguais, retorne o dobro da soma.
    soma_dobro(1, 2) -> 3
    soma_dobro(2, 2) -> 8
    """

    return (a + b) * 2 if a == b else a + b


def diff21(n: int) -> int:
    """
    Dado um inteiro n, retorne a diferença absoluta entre n e 21
    Porém, se o número for maior que 21, retorne o dobro da diferença absoluta.
    diff21(19) -> 2
    diff21(25) -> 8
    dica: abs(x) retorna o valor absoluto de x
    """

    return abs(n - 21) * 2 if n > 21 else abs(n - 21)


def papagaio(falando: bool, hora: int = 0) -> bool:
    """
    Temos um papagaio que fala alto.
    hora é um parâmetro entre 0 e 23
    Temos problemas se o papagaio estiver falando antes da 7 ou depois das 20
    """

    return True if falando and (hora < 7 or hora > 20) else False


def dez(a: int, b: int) -> bool:
    """
    Dados dois inteiros a e b,
    retorne True se um dos dois é 10 ou a soma é 10
    """

    return True if a == 10 or b == 10 or a + b == 10 else False


def dista10(n: int) -> bool:
    """
    Seja um inteiro n,
    retorne True se a diferença absoluta entre n e 100 ou n e 200
    for menor ou igual a 10
    dista10(93) -> True
    dista10(90) -> True
    dista10(89) -> False
    """

    return True if abs(n - 100) <= 10 or abs(n - 200) <= 10 else False


def apaga(s: str, n: int) -> str:
    """
    Seja uma string s e um inteiro n,
    retorne uma nova string sem a posição n
    apaga('kitten', 1) -> 'ktten'
    apaga('kitten', 4) -> 'kittn'
    """

    string = [l for l in s]; string.pop(n)
    return ''.join(string)


def troca(s: str) -> str:
    """
    Seja uma string s,
    se s tiver tamanho <= 1 retorna ela mesma.
    Caso contrário, troca a primeira e última letra
    troca('code') -> 'eodc'
    troca('a') -> 'a'
    troca('ab') -> 'ba'
    """

    if s != '':
        string = [l for l in s]
        string[0], string[-1] = string[-1], string[0]

    return s if len(s) <= 1 else ''.join(string)


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos, total = 0, 0


def test(obtido, esperado):
    global acertos, total

    total += 1
    if obtido != esperado:
        prefixo = 'Falhou.'
    else:
        prefixo = 'Passou.'
        acertos += 1

    print (f'{prefixo} Esperado: {repr(esperado)} \tObtido: {repr(obtido)}')


def main():
    print('Oba! Hoje vou ficar dormindo!')
    test(dormir(False, False), True)
    test(dormir(True, False), False)
    test(dormir(False, True), True)
    test(dormir(True, True), True)

    print('\nAlunos problema')
    test(alunos_problema(True, True), True)
    test(alunos_problema(False, False), True)
    test(alunos_problema(True, False), False)
    test(alunos_problema(False, True), False)

    print('\nSoma dobro')
    test(soma_dobro(1, 2), 3)
    test(soma_dobro(3, 2), 5)
    test(soma_dobro(2, 2), 8)
    test(soma_dobro(-1, 0), -1)
    test(soma_dobro(0, 0), 0)
    test(soma_dobro(0, 1), 1)

    print('\nDiff21')
    test(diff21(19), 2)
    test(diff21(10), 11)
    test(diff21(21), 0)
    test(diff21(22), 2)
    test(diff21(25), 8)
    test(diff21(30), 18)

    print('\nPapagaio')
    test(papagaio(True, 6), True)
    test(papagaio(True, 7), False)
    test(papagaio(False, 6), False)
    test(papagaio(True, 21), True)
    test(papagaio(False, 21), False)
    test(papagaio(True, 23), True)
    test(papagaio(True, 20), False)

    print('\nDez')
    test(dez(9, 10), True)
    test(dez(9, 9), False)
    test(dez(1, 9), True)
    test(dez(10, 1), True)
    test(dez(10, 10), True)
    test(dez(8, 2), True)
    test(dez(8, 3), False)
    test(dez(10, 42), True)
    test(dez(12, -2), True)

    print('\nDista 10')
    test(dista10(93), True)
    test(dista10(90), True)
    test(dista10(89), False)
    test(dista10(110), True)
    test(dista10(111), False)
    test(dista10(121), False)
    test(dista10(0), False)
    test(dista10(5), False)
    test(dista10(191), True)
    test(dista10(189), False)
    test(dista10(190), True)
    test(dista10(200), True)
    test(dista10(210), True)
    test(dista10(211), False)
    test(dista10(290), False)

    print('\nApaga')
    test(apaga('kitten', 1), 'ktten')
    test(apaga('kitten', 0), 'itten')
    test(apaga('kitten', 2), 'kiten')
    test(apaga('kitten', 4), 'kittn')
    test(apaga('Hi', 0), 'i')
    test(apaga('Hi', 1), 'H')
    test(apaga('code', 0), 'ode')
    test(apaga('code', 1), 'cde')
    test(apaga('code', 2), 'coe')
    test(apaga('code', 3), 'cod')
    test(apaga('chocolate', 8), 'chocolat')

    print('\nTroca letras')
    test(troca('code'), 'eodc')	    
    test(troca('a'), 'a')
    test(troca('ab'), 'ba')
    test(troca('abc'), 'cba')
    test(troca(''), '')
    test(troca('Chocolate'), 'ehocolatC')
    test(troca('nythoP'), 'Python')
    test(troca('hello'), 'oellh')


if __name__ == '__main__':
    main()
    print(f'\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {float(acertos * 10) / total:.1f}')

    if total == acertos:
        print('Parabéns, seu programa rodou sem falhas!')
