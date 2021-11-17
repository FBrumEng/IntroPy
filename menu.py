# 1 - imports / bibliotecas
# 2 - classes

# 3 - metodos / funções
# def = definition = definição

def print_hi(name):
    print(f'Seja bem vindo, {name}') # depois do Python 3
    print(f'Seja bem vindo,' + name) # antes do Python 3

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triangulo(base, altura):
    return (base * altura)/2

def contagem_progressiva(fim):
    for numero in range(fim): # repetir o bloco de 0 ate o fim
        print(numero)         # exibir o numero

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        contador = numero + 1
        #print(f'{contador} - {nome}')

        if contador < 10:
            print(f'00{contador} - {nome}')
        elif contador < 100:
            print(f'0{contador} - {nome}')
        else:
            print(contador,'-', nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))

def sair():
    print('Obrigado e Volte sempre!')

# def exibir_menu(resposta):
#     opcao = {
#             1:print_hi('Felipe Brum'),
#             2:calcular_area_do_retangulo(8, 9),
#             3:calcular_area_do_quadrado(7),
#             4:calcular_area_do_triangulo(5, 4),
#             5:contagem_progressiva(10),
#             6:apoiar_candidato('Sabado', 10),
#             7:brincar_de_plim(20),
#             8:sair()
#     }
#     return opcao.get(escolha, 'Opção Inválida')

# estrutura de identificação / execução do script
if __name__ == '__main__':

    resposta = 'C'

    while resposta.upper() != 'Z':
        print('###################################')
        print('#                                 #')
        print('#   M E N U   D E   O P Ç Õ E S   #')
        print('#                                 #')
        print('#     1 - Olá Mundo               #')
        print('#     2 - Área do Retângulo       #')
        print('#     3 - Área do Quadrado        #')
        print('#     4 - Área do Triângulo       #')
        print('#     5 - Contagem Progressiva    #')
        print('#     6 - Apoiar Candidato        #')
        print('#     7 - Brincar de PLIM         #')
        print('#                                 #')
        print('#     Z - Sair                    #')
        print('#                                 #')
        print('###################################')

        resposta = input('Digite aqui a sua opção: ')
        print(f'A sua escolha foi: {resposta}')

        if resposta.upper() != 'Z':
            if resposta == '1':
                print_hi('Felipe Brum')
            elif resposta == '2':
                resultado = calcular_area_do_retangulo(4, 6)
                print(f'A área do retangulo é de: {resultado} m²')
            elif resposta == '3':
                resultado = calcular_area_do_quadrado(4)
                print(f'A área do quadrado é de: {resultado} m²')
            elif resposta == '4':
                resultado = calcular_area_do_triangulo(5, 2)
                print(f'A área do triangulo é de: {resultado} m²')
            elif resposta == '5':
                contagem_progressiva(10)
            elif resposta == '6':
                apoiar_candidato('Murphy',13)
            elif resposta == '7':
                brincar_de_plim(7)
            else:
                print('Opção Inválida. Escolha uma opção de 1 a 7.')
        else:
            print('Você saiu. Volte Sempre!')



