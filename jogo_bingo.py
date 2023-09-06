#Criando o jogo do bingo em Python
#Autor: Eduardo Machado
#Data de iniciado: 05/09/2023
#Portfólio: edudigitalsystems.blogspot.com
#E-mail: edudigitalsystems@gmail.com


#importanto todas as bibliotecas usadas no jogo
#random é para gerar números aleatorios e randint() é o método para gerar números
# inteiros aleatórios
from random import randint
#O cycle(ciclo) gera um looping for infinito, é da biblioteca itertools(ferramentas iterativas).
from itertools import cycle
#importando a biblioteca time para usar o comando sleep que conta tempo para uma mensagem passar sleep(adormecer)
from time import sleep

#variáveis do tipo lista sendo criada
#Obs: o jogo só vai ler as catelas se estiverem com números inteiros positivo
#aqui a lista das variáveis das cartelas não serão lidas por terem números que
#não existem nas cartelas, que são negativos. os números aleatórios só saem positivos.
cartela1, cartela2, cartela3, cartela4, cartela5 = [-1], [-1], [-1], [-1], [-1]
cartela6, cartela7, cartela8, cartela9, cartela10 = [-1], [-1], [-1], [-1], [-1]


#variável que vai pegar a quantidade de cartelas que vai entrar no jogo.
quantidade_cartelas = int(input('Quantidade total de cartelas: '))

#laço que vai repetir de acordo com o número de cartelas digitado pelo usuário
#Ex:se for digitado 4, então serão 4 cartelas a serem cadastradas
for i in range(quantidade_cartelas):
    #variável criada para pegar os números das cartelas.
    num_cartela = int(input('N° da cartela: '))
    #condicção para ver qual cartela foi escolhida pelos jogadores.
    if num_cartela == 1:
        # colocando(populando) os números da cartela1 na variável escolhida chamada cartela1.
        # variável do tipo lista sendo criada chamada cartela1 e recebendo os seus números
        cartela1 = [
            12, 3, 1, 5, 6,
            29, 20, 17, 28, 25,
            40, 42, 36, 31, 38,
            60, 57, 58, 49, 56,
            75, 72, 68, 69, 65
        ]
        print(cartela1)
    # condicção para ver qual cartela foi escolhida pelos jogadores.
    #se o número da cartela digitada for 2 então coloca os dados da cartela 2 na variável cartela2.
    if num_cartela == 2:
        # colocando os dados na cartela2
        # variável do tipo lista sendo criada
        cartela2 = [
            15, 8, 2, 5, 9,
            16, 27, 23, 30, 19,
            35, 39, 33, 41, 40,
            59, 51, 53, 48, 47,
            67, 68, 74, 66, 64
        ]
        print(cartela2)
    if num_cartela == 3:
        cartela3 = [
            3, 14, 9, 11, 8,
            29, 28, 30, 18, 27,
            41, 35, 31, 42, 45,
            56, 49, 47, 57, 53,
            75, 67, 69, 70, 62,
        ]
        print(cartela3)
    if num_cartela == 4:
        cartela4 = [
            8, 15, 4, 10, 7,
            27, 16, 26, 30, 19,
            41, 38, 33, 43, 35,
            53, 46, 47, 48, 60,
            65, 62, 64, 71, 66
        ]
        print(cartela4)
    if num_cartela == 5:
        cartela5 = [
            12, 14, 7, 8, 2,
            19, 22, 24, 16, 23,
            40, 42, 38, 41, 39,
            50, 54, 49, 59, 57,
            62, 75, 61, 63, 74,
        ]
        print(cartela5)
    if num_cartela == 6:
        cartela6 = [
            13, 10, 5, 1, 15,
            24, 17, 23, 29, 18,
            31, 37, 42, 36, 45,
            46, 51, 55, 48, 53,
            73, 67, 61, 68, 63
        ]
        print(cartela6)
    if num_cartela == 7:
        cartela7 = [
            2, 14, 5, 10, 6,
            26, 28, 30, 25, 22,
            41, 43, 37, 34, 32,
            47, 50, 55, 46, 58,
            71, 68, 70, 63, 66
        ]
        print(cartela7)
    if num_cartela == 8:
        cartela8 = [
            1, 7, 13, 2, 12,
            21, 23, 17, 25, 19,
            45, 38, 32, 33, 39,
            54, 59, 52, 58, 46,
            69, 71, 63, 64, 61
        ]
        print(cartela8)
    if num_cartela == 9:
        cartela9 = [
            13, 7, 3, 4, 15,
            21, 30, 26, 16, 23,
            35, 40, 36, 32, 41,
            51, 59, 49, 46, 58,
            73, 67, 68, 66, 65
        ]
        print(cartela9)
    if num_cartela == 10:
        cartela10 = [
            9, 7, 4, 6, 1,
            25, 21, 20, 29, 22,
            45, 32, 31, 42, 38,
            57, 56, 46, 49, 47,
            72, 64, 67, 65, 68
        ]
        print(cartela10)
#Criando a variável que vai guardar todos os resultados das bolas chamadas pelo sistema.
resultados_chamada = []
#Mensagem de aviso que vai começar o jogo
print('Atenção!! o Jogo vai começar ')
sleep(7)
#laço de repetição para rodar infinitamente com o comando cycle(ciclo)
for i in cycle(range(1)):
    # variável criada para pegar a bola chamada aleatória entre 1 e 90
    bola_chamada = randint(1, 90)
    #Se não existir a bola chamada dentro da variável resultados_chamada ela adc
    #isso evita de chamar bolas repetidas.
    if bola_chamada not in resultados_chamada:
        # Vai falar as bolas chamadas e mostrar na tela
        print('Bola n°: {}'.format(bola_chamada))
        # comando sleep(adormecer) para demorar 7 segundos após o anúncio da bola.
        sleep(7)
        #o comando append(acrescentar) acrescenta o valor de bola_chamada, acumula todos os valores chamados.
        resultados_chamada.append(bola_chamada)
        #imprime todos os resultados das bolas que foram chamadas no jogo
        print('Chamadas: {}'.format(resultados_chamada))
