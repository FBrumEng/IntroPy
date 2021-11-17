# 1 - imports / bibliotecas


# 2 - classes


# 3 - metodos / funções
# def = definition = definição

def print_hi(name):
    print(f'Seja bem vindo, {name}')  # depois do Python 3
    print(f'Seja bem vindo,' + name)  # antes do Python 3


def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento


def calcular_area_do_quadrado(lado):
    return lado ** 2


def calcular_area_do_triangulo(base, altura):
    return (base * altura) / 2


def contagem_progressiva(fim):
    for numero in range(fim):  # repetir o bloco de 0 ate o fim
        print(numero)  # exibir o numero


def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        contador = numero + 1
        # print(f'{contador} - {nome}')

        if contador < 10:
            print(f'00{contador} - {nome}')
        elif contador < 100:
            print(f'0{contador} - {nome}')
        else:
            print(contador, '-', nome)


def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))


def exibir_dia_da_semana_if(numero):
    print('Execução com if')
    if numero == 1:
        print('O dia é Segunda')
    elif numero == 2:
        print('O dia é Terça')
    elif numero == 3:
        print('O dia é Quarta')
    elif numero == 4:
        print('O dia é Quinta')
    elif numero == 5:
        print('O dia é Sexta')
    elif numero == 6:
        print('O dia é Sabado')
    elif numero == 7:
        print('O dia é Domingo')
    else:
        print('Numero de dia inválido. Digite um numero de 1 a 7')


def exibir_dia_da_semana_match(numero):
    print('Execução com match')
    match numero:
        case 1:
            print('O dia é Segunda')
        case 2:
            print('O dia é Terça')
        case 3:
            print('O dia é Quarta')
        case 4:
            print('O dia é Quinta')
        case 5:
            print('O dia é Sexta')
        case 6:
            print('O dia é Sabado')
        case 7:
            print('O dia é Domingo')
        case _:
            print('Número de dia inválido. Digite um número de 1 a 7')



def brincar_de_para_ou_continua():
    resposta = 'C'  # C aqui significa que contina

    while resposta.upper() == 'C':
        resposta = input('Digite P para parar ou C para continuar:')

    print('Voce decidiu parar com a brincadeira!!')


if __name__ == '__main__':
    print_hi('Brum')

    # chamar a função de calculo da area do retangulo
    resultado = calcular_area_do_retangulo(3, 4)
    print(f'A área do retângulo é de: {resultado} m²')

    # chamar a função de calculo da area do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f'A área do quadrado é de: {resultado} m²')

    # chamar a função de calculo da area do triangulo
    resultado = calcular_area_do_triangulo(6, 7)
    print(f'A área do triangulo é de: {resultado} m²')

    # executar uma contagem progressiva
    contagem_progressiva(10)

    # executar o nome do candidato varias vezes
    apoiar_candidato('Faker', 100)

    # brincar de plim
    brincar_de_plim(100)

    # exemplo de dia da semana com if - elif - else
    exibir_dia_da_semana_if(6)

    # exemplo de dia da semana com
    exibir_dia_da_semana_match(5)

    # exemplo com while - para ou continua
    brincar_de_para_ou_continua()
