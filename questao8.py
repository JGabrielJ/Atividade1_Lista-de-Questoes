def media_anual(temperaturas: list) -> list:
    '''Receba uma lista com as temperaturas médias de cada mês
    e devolva uma lista com os números correspondentes aos meses que 
    possuem temperatura superior à média anual.'''

    media = sum(temperaturas) / len(temperaturas)
    return [mes for mes in range(0, len(temperaturas)) if temperaturas[mes] > media]


def maiores_13(idades: list, alturas: list) -> list:
    '''Esta função recebe as idades e alturas de diversas pessoas, em duas
    listas separadas e de igual comprimento.
    Calcule a média das alturas e retorne as alturas daqueles que possuem
    'idades' maior que 13 e altura inferior a média da turma.'''

    media = sum(alturas) / len(alturas)
    return [alturas[i] for i in range(0, len(alturas)) if idades[i] > 13 and alturas[i] < media]


def media_saltos_lista(saltos: list) -> float:
    '''Receba uma lista com os saltos de um atleta e calcule a média dos
    seus saltos, sabendo que o melhor e o pior saltos são desconsiderados.'''

    saltos.remove(max(saltos)); saltos.remove(min(saltos))
    return sum(saltos) / len(saltos)


def lista_de_primos(inicio: int, fim: int) -> list:
    '''Retorne uma lista de primos entre os valores informados,
    incluindo os limites.'''

    count: int = 0
    primos: list = []

    for n in range(inicio, fim + 1):
        for div in range(1, n + 1):
            if n % div == 0:
                count += 1
        
        if count == 2:
            primos.append(n)

        count = 0

    return primos


def fibonacci(n: int) -> list:
    '''Retorne uma lista com os n primeiros valores da série de Fibonacci.
    Fibonacci = 1, 1, 2, 3, 5, 8, 13, ...'''

    f: int = 1
    fibo: list = []
    for _ in range(1, n + 1):
        fibo.append(f)
        if len(fibo) >= 2:
            f = fibo[-1] + fibo[-2]

    return fibo


def altera_salarios(salarios: list) -> list:
    '''Calcule o aumento de salário de acordo com a seguinte tabela:

    - até 1 Salário Mínimo (inclusive): aumento de 20%
    - de 1 até 2 Salários Mínimos (inclusive): aumento de 15%
    - de 2 até 5 Salários Mínimos (inclusive): aumento de 10%
    - acima de 5 Salários Mínimos: aumento de 5%

    Salário mínimo para referência: R$ 724,00
    Retorna a lista com os salários alterados
    '''

    novos_salarios: list = []

    for salario in salarios:
        if salario <= 724.00:
            salario += salario * 20 / 100
        elif salario <= 724.00 * 2:
            salario += salario * 15 / 100
        elif salario <= 724.00 * 5:
            salario += salario * 10 / 100
        else:
            salario += salario * 5 / 100

        novos_salarios.append(salario)
    
    return novos_salarios


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

    print(f'{prefixo} Esperado: {repr(esperado)} \tObtido: {repr(obtido)}')


def main():
    print('Meses acima da média:')
    test(media_anual([20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]), [])
    test(media_anual([25, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]), [0])
    test(media_anual([23, 25, 26, 24, 21, 22, 26, 24, 25, 22, 23, 19]), [1, 2, 3, 6, 7, 8])
    test(media_anual([19, 20, 21, 20, 17, 18, 19, 20, 22, 21, 20]), [1, 2, 3, 7, 8, 9, 10])
    test(media_anual([21, 22, 23, 21, 22, 22, 23, 21, 23, 22, 21, 23, 21]), [1, 2, 4, 5, 6, 8, 9, 11])

    print('Alturas abaixo da média:')
    test(maiores_13([13, 13, 14], [1.7, 1.7, 1.5]), [1.5])
    test(maiores_13([13, 13, 14, 13], [1.7, 1.7, 1.5, 1.6]), [1.5])
    test(maiores_13([14, 20], [1.6, 2]), [1.6])
    test(maiores_13([10, 7, 13, 15, 20, 21],[1.7, 1.21, 1.65, 2, 1.9, 1.5]), [1.5])
    test(maiores_13([14, 15, 16, 17, 18, 30], [1.9, 1.89, 1.85, 1.95, 2, 1.99]), [1.9, 1.89, 1.85])
    test(maiores_13([10, 9, 90, 9, 13, 14, 15], [1.25, 1.3, 1.7, 1.41, 1.5, 1.55, 1.7]), [])

    print('Média dos saltos em lista:')
    test(media_saltos_lista([10, 10, 10, 10, 10]), 10)
    test(media_saltos_lista([9, 9.1, 8, 7, 6.9]), 8)
    test(media_saltos_lista([1, 1, 3, 5, 5]), 3)
    test(media_saltos_lista([10, 10, 9.9, 10, 10]), 10)

    print('Lista de primos:')
    test(lista_de_primos(0, 1), [])
    test(lista_de_primos(5, 10), [5, 7])
    test(lista_de_primos(10, 20), [11, 13, 17, 19])
    test(lista_de_primos(0, 21), [2, 3, 5, 7, 11, 13, 17, 19])
    test(lista_de_primos(43, 102), [43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101])

    print('Fibonacci:')
    test(fibonacci(1), [1])
    test(fibonacci(2), [1, 1])
    test(fibonacci(3), [1, 1, 2])
    test(fibonacci(4), [1, 1, 2, 3])

    print('Aumenta salários:')
    test(altera_salarios([500, 724.0, 725.00, 1448.00, 1449.00, 3620.00, 3621.00, 4000.00]), 
        [600.0, 868.8, 833.75, 1665.2, 1593.9, 3982.0, 3802.05, 4200.0])


if __name__ == '__main__':
    main()
    print(f'\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {float(acertos * 10) / total:.1f}')

    if total == acertos:
        print('Parabéns, seu programa rodou sem falhas!')
