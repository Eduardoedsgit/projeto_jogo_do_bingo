#Criando o jogo do bingo em Python
#Linguagem Python versão (version) 3.11.5
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
#importando a biblioteca pygame para usar o método mixer para executar sons do jogo
from pygame import mixer

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
#Criando as variáveis que vai guardar todos os resultados das bolas chamadas pelo sistema.
resultados_chamada = []

#variáveis que vai guardar os resultados das pontuações de cada uma das cartelas que forem prennchidas
#cada variável guarda as pontuações de uma cartela específica.
completa_cartela1 = 0
completa_cartela2 = 0
completa_cartela3 = 0
completa_cartela4 = 0
completa_cartela5 = 0
completa_cartela6 = 0
completa_cartela7 = 0
completa_cartela8 = 0
completa_cartela9 = 0
completa_cartela10 = 0

#lista de sons da chamada das bolas do bingo
chamadas_voz = {
                1: 'Audio-bingo\\bola_n1.wav',
                2: 'Audio-bingo\\bola_n2.wav',
                3: 'Audio-bingo\\bola_n3.wav',
                4: 'Audio-bingo\\bola_n4.wav',
                5: 'Audio-bingo\\bola_n5.wav',
                6: 'Audio-bingo\\bola_n6.wav',
                7: 'Audio-bingo\\bola_n7.wav',
                8: 'Audio-bingo\\bola_n8.wav',
                9: 'Audio-bingo\\bola_n9.wav',
                10: 'Audio-bingo\\bola_n10.wav',
                11: 'Audio-bingo\\bola_n11.wav',
                12: 'Audio-bingo\\bola_n12.wav',
                13: 'Audio-bingo\\bola_n13.wav',
                14: 'Audio-bingo\\bola_n14.wav',
                15: 'Audio-bingo\\bola_n15.wav',
                16: 'Audio-bingo\\bola_n16.wav',
                17: 'Audio-bingo\\bola_n17.wav',
                18: 'Audio-bingo\\bola_n18.wav',
                19: 'Audio-bingo\\bola_n19.wav',
                20: 'Audio-bingo\\bola_n20.wav',
                21: 'Audio-bingo\\bola_n21.wav',
                22: 'Audio-bingo\\bola_n22.wav',
                23: 'Audio-bingo\\bola_n23.wav',
                24: 'Audio-bingo\\bola_n24.wav',
                25: 'Audio-bingo\\bola_n25.wav',
                26: 'Audio-bingo\\bola_n26.wav',
                27: 'Audio-bingo\\bola_n27.wav',
                28: 'Audio-bingo\\bola_n28.wav',
                29: 'Audio-bingo\\bola_n29.wav',
                30: 'Audio-bingo\\bola_n30.wav',
                31: 'Audio-bingo\\bola_n31.wav',
                32: 'Audio-bingo\\bola_n32.wav',
                33: 'Audio-bingo\\bola_n33.wav',
                34: 'Audio-bingo\\bola_n34.wav',
                35: 'Audio-bingo\\bola_n35.wav',
                36: 'Audio-bingo\\bola_n36.wav',
                37: 'Audio-bingo\\bola_n37.wav',
                38: 'Audio-bingo\\bola_n38.wav',
                39: 'Audio-bingo\\bola_n39.wav',
                40: 'Audio-bingo\\bola_n40.wav',
                41: 'Audio-bingo\\bola_n41.wav',
                42: 'Audio-bingo\\bola_n42.wav',
                43: 'Audio-bingo\\bola_n43.wav',
                44: 'Audio-bingo\\bola_n44.wav',
                45: 'Audio-bingo\\bola_n45.wav',
                46: 'Audio-bingo\\bola_n46.wav',
                47: 'Audio-bingo\\bola_n47.wav',
                48: 'Audio-bingo\\bola_n48.wav',
                49: 'Audio-bingo\\bola_n49.wav',
                50: 'Audio-bingo\\bola_n50.wav',
                51: 'Audio-bingo\\bola_n51.wav',
                52: 'Audio-bingo\\bola_n52.wav',
                53: 'Audio-bingo\\bola_n53.wav',
                54: 'Audio-bingo\\bola_n54.wav',
                55: 'Audio-bingo\\bola_n55.wav',
                56: 'Audio-bingo\\bola_n56.wav',
                57: 'Audio-bingo\\bola_n57.wav',
                58: 'Audio-bingo\\bola_n58.wav',
                59: 'Audio-bingo\\bola_n59.wav',
                60: 'Audio-bingo\\bola_n60.wav',
                61: 'Audio-bingo\\bola_n61.wav',
                62: 'Audio-bingo\\bola_n62.wav',
                63: 'Audio-bingo\\bola_n63.wav',
                64: 'Audio-bingo\\bola_n64.wav',
                65: 'Audio-bingo\\bola_n65.wav',
                66: 'Audio-bingo\\bola_n66.wav',
                67: 'Audio-bingo\\bola_n67.wav',
                68: 'Audio-bingo\\bola_n68.wav',
                69: 'Audio-bingo\\bola_n69.wav',
                70: 'Audio-bingo\\bola_n70.wav',
                71: 'Audio-bingo\\bola_n71.wav',
                72: 'Audio-bingo\\bola_n72.wav',
                73: 'Audio-bingo\\bola_n73.wav',
                74: 'Audio-bingo\\bola_n74.wav',
                75: 'Audio-bingo\\bola_n75.wav',
                76: 'Audio-bingo\\bola_n76.wav',
                77: 'Audio-bingo\\bola_n77.wav',
                78: 'Audio-bingo\\bola_n78.wav',
                79: 'Audio-bingo\\bola_n79.wav',
                80: 'Audio-bingo\\bola_n80.wav',
                81: 'Audio-bingo\\bola_n81.wav',
                82: 'Audio-bingo\\bola_n82.wav',
                83: 'Audio-bingo\\bola_n83.wav',
                84: 'Audio-bingo\\bola_n84.wav',
                85: 'Audio-bingo\\bola_n85.wav',
                86: 'Audio-bingo\\bola_n86.wav',
                87: 'Audio-bingo\\bola_n87.wav',
                88: 'Audio-bingo\\bola_n88.wav',
                89: 'Audio-bingo\\bola_n89.wav',
                90: 'Audio-bingo\\bola_n90.wav',
                }

#Mensagem de aviso que vai começar o jogo
print('Atenção!! o Jogo vai começar ')
sleep(15)
#laço de repetição para rodar infinitamente com o comando cycle(ciclo) da biblioteca itertools(ferramentas iterativas)
for i in cycle(range(1)):
    # variável criada para pegar a bola da chamada aleatória entre 1 e 90
    bola_chamada = randint(1, 90)
    #Se não existir a bola chamada dentro da variável resultados_chamada, ela adc
    #isso evita de chamar bolas repetidas.
    if bola_chamada not in resultados_chamada:
        # Vai falar as bolas chamadas e mostrar na tela
        print(f'Bola n°: {bola_chamada}')
        #variável que vai pegar os resultados das bolas não repetidas
        no_repet_bola_chamada = bola_chamada
        #cria uma variável que vai pegar as chamadas das bolas não repetidas.
        #iniciando a biblioteca pygame com o método init()
        mixer.init()
        #Lendo o diretório da música com o comando .load()
        #Vai ler o número da chave de acordo com o número da bola_chamada ex se for 1 será número 1
        mixer.music.load(chamadas_voz[bola_chamada])
        #Dando play para a som começar
        mixer.music.play()
        # comando sleep(adormecer) para demorar 7 segundos após o anúncio da bola.
        sleep(10)
        #o comando append(acrescentar) acrescenta o valor de bola_chamada, acumula todos os valores chamados.
        resultados_chamada.append(bola_chamada)
        #imprime todos os resultados das bolas que foram chamadas no jogo
        print(f'Chamadas: {resultados_chamada}')
        #Verificação da primeira cartela
        #Condição para verificar qual cartela dará bingo!!
        #Qual cartela será a campeã!!, Começando com a verificação da primeira cartela
        if no_repet_bola_chamada in cartela1:
            completa_cartela1 += 1
            #verifica se a primeira cartela for toda preenchida, será bingo!.
            if completa_cartela1 == 25:
                print('Bingoooo! cartela n° 1')
                #Para o laço infinito com o comando break
                break
        #Se a bola_chamada estiver dentro da cartela dois, o contador completa_cartela2 incrementa 1
        if no_repet_bola_chamada in cartela2:
            #incrementa 1 na variável completa_cartela2
            completa_cartela2 += 1
            #Se completa_cartela2 == 25, cartela prenchida será bingoo!!
            if completa_cartela2 == 25:
                print('Bingooooo!! Cartela N°: 2')
                break
        if no_repet_bola_chamada in cartela3:
            completa_cartela3 += 1
            if completa_cartela3 == 25:
                print('Bingooo!! Cartela N°: 3')
                break
        if no_repet_bola_chamada in cartela4:
            completa_cartela4 += 1
            if completa_cartela4 == 25:
                print('Bingoooo!! Cartela N°: 4')
                break
        if no_repet_bola_chamada in cartela5:
            completa_cartela5 += 1
            if completa_cartela5 == 25:
                print('Bingoooo!! Cartela N°: 5')
                break
        if no_repet_bola_chamada in cartela6:
            completa_cartela6 += 1
            if completa_cartela6 == 25:
                print('Bingooo!! Cartela N°: 6')
                break
        if no_repet_bola_chamada in cartela7:
            completa_cartela7 += 1
            if completa_cartela7 == 25:
                print('Bingooo!! Cartela N° 7')
                break
        if no_repet_bola_chamada in cartela8:
            completa_cartela8 += 1
            if completa_cartela8 == 25:
                print('Bingooo!! Cartela N° 8')
                break
        if no_repet_bola_chamada in cartela9:
            completa_cartela9 += 1
            if completa_cartela9 == 25:
                print('Bingooo!! Cartela N° 9')
                break
        if no_repet_bola_chamada in cartela10:
            completa_cartela10 += 1
            if completa_cartela10 == 25:
                print('Bingooo!! Cartela N° 10')
                break
