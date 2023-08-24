'''
Projeto Jogo do Bingo
Autor: Eduardo Machado de Souza
Inicio projeto: 20/08/2023

'''
#canto das importações de bibliotecas da linguagem python
#importando a biblioteca de tempo
from time import sleep;
#importando a biblioteca de esolha aleatoria de um número do tipo inteiro.
from random import randint;



#cria uma lista de ítens para ser inserido
cartela1 = list();
#atribui valores na variável lista criada. append(acrescentar).
cartela1.append(int(12));
cartela1.append(int(3));
cartela1.append(int(1));
cartela1.append(int(5));
cartela1.append(int(6));
cartela1.append(int(29));
cartela1.append(int(20));
cartela1.append(int(17));
cartela1.append(int(28));
cartela1.append(int(25));
cartela1.append(int(40));
cartela1.append(int(42));
cartela1.append(int(36));
cartela1.append(int(31));
cartela1.append(int(38));
cartela1.append(int(60));
cartela1.append(int(57));
cartela1.append(int(58));
cartela1.append(int(49));
cartela1.append(int(56));
cartela1.append(int(75));
cartela1.append(int(72));
cartela1.append(int(68));
cartela1.append(int(69));
cartela1.append(int(65));

#Cartela 2------------------------------
#Criando a lista de cartela2 variável lista
cartela2 = list();
#adc valores na variável lista criada chamada cartela2
cartela2.append(int(15));
cartela2.append(int(8));
cartela2.append(int(2));
cartela2.append(int(5));
cartela2.append(int(9));
cartela2.append(int(16));
cartela2.append(int(27));
cartela2.append(int(23));
cartela2.append(int(30));
cartela2.append(int(19));
cartela2.append(int(35));
cartela2.append(int(39));
cartela2.append(int(33));
cartela2.append(int(41));
cartela2.append(int(40));
cartela2.append(int(59));
cartela2.append(int(51));
cartela2.append(int(53));
cartela2.append(int(48));
cartela2.append(int(47));
cartela2.append(int(67));
cartela2.append(int(68));
cartela2.append(int(74));
cartela2.append(int(66));
cartela2.append(int(64));


#cartela número 3-----------------
#criando a variavels lista cartela3
cartela3 = list();
#adc dados na variavellista3 do tipo inteiro (int).
cartela3.append(int(3));
cartela3.append(int(14));
cartela3.append(int(9));
cartela3.append(int(11));
cartela3.append(int(8));
cartela3.append(int(29));
cartela3.append(int(28));
cartela3.append(int(30));
cartela3.append(int(18));
cartela3.append(int(27));
cartela3.append(int(41));
cartela3.append(int(35));
cartela3.append(int(31));
cartela3.append(int(42));
cartela3.append(int(45));
cartela3.append(int(56));
cartela3.append(int(49));
cartela3.append(int(47));
cartela3.append(int(57));
cartela3.append(int(53));
cartela3.append(int(75));
cartela3.append(int(67));
cartela3.append(int(69));
cartela3.append(int(70));
cartela3.append(int(62));

#Cartela número 4------------------
#criando a variável lista cartela4
cartela4 = list();
#Acrescentando dados na variável lista chamada cartela4
cartela4.append(int(8));
cartela4.append(int(15));
cartela4.append(int(4));
cartela4.append(int(10));
cartela4.append(int(7));
cartela4.append(int(27));
cartela4.append(int(16));
cartela4.append(int(26));
cartela4.append(int(30));
cartela4.append(int(19));
cartela4.append(int(41));
cartela4.append(int(38));
cartela4.append(int(33));
cartela4.append(int(43));
cartela4.append(int(35));
cartela4.append(int(53));
cartela4.append(int(46));
cartela4.append(int(47));
cartela4.append(int(48));
cartela4.append(int(60));
cartela4.append(int(65));
cartela4.append(int(62));
cartela4.append(int(64));
cartela4.append(int(71));
cartela4.append(int(66));


#Cartela número 5 ----------------------
#Criando a variável lista cartela 5
cartela5 = list();
#Acrescentando dados di tipo intieor na variável cartela5
cartela5.append(int(12));
cartela5.append(int(14));
cartela5.append(int(7));
cartela5.append(int(8));
cartela5.append(int(2));
cartela5.append(int(19));
cartela5.append(int(22));
cartela5.append(int(24));
cartela5.append(int(16));
cartela5.append(int(23));
cartela5.append(int(40));
cartela5.append(int(42));
cartela5.append(int(38));
cartela5.append(int(41));
cartela5.append(int(39));
cartela5.append(int(50));
cartela5.append(int(54));
cartela5.append(int(49));
cartela5.append(int(59));
cartela5.append(int(57));
cartela5.append(int(62));
cartela5.append(int(75));
cartela5.append(int(61));
cartela5.append(int(63));
cartela5.append(int(74));


#Cartela n° 6 ----------------------------------------
#criando avariável lista chamada cartela6.
cartela6 = list();

cartela6.append(int(13));
cartela6.append(int(10));
cartela6.append(int(5));
cartela6.append(int(1));
cartela6.append(int(15));
cartela6.append(int(24));
cartela6.append(int(17));
cartela6.append(int(23));
cartela6.append(int(29));
cartela6.append(int(18));
cartela6.append(int(31));
cartela6.append(int(37));
cartela6.append(int(42));
cartela6.append(int(36));
cartela6.append(int(45));
cartela6.append(int(46));
cartela6.append(int(51));
cartela6.append(int(55));
cartela6.append(int(48));
cartela6.append(int(53));
cartela6.append(int(73));
cartela6.append(int(67));
cartela6.append(int(61));
cartela6.append(int(68));
cartela6.append(int(63));

#Certela n° 7 ---------------------------------------------
#Criando a variável lista chamada cartela7
cartela7 = list();

#acrescentando valores na variável lista chamada cartela7
cartela7.append(int(2));
cartela7.append(int(14));
cartela7.append(int(5));
cartela7.append(int(10));
cartela7.append(int(6));
cartela7.append(int(26));
cartela7.append(int(28));
cartela7.append(int(30));
cartela7.append(int(25));
cartela7.append(int(22));
cartela7.append(int(41));
cartela7.append(int(43));
cartela7.append(int(37));
cartela7.append(int(34));
cartela7.append(int(32));
cartela7.append(int(47));
cartela7.append(int(50));
cartela7.append(int(55));
cartela7.append(int(46));
cartela7.append(int(58));
cartela7.append(int(71));
cartela7.append(int(68));
cartela7.append(int(70));
cartela7.append(int(63));
cartela7.append(int(66));


#Cartela de n° 8 ----------------------------------------

#Criando a variável do tipo lista chamada cartela8
cartela8 = list();

#Acrescentando valores inteiros na variável lista chamada cartela8.
cartela8.append(int(1));
cartela8.append(int(7));
cartela8.append(int(13));
cartela8.append(int(2));
cartela8.append(int(12));
cartela8.append(int(21));
cartela8.append(int(23));
cartela8.append(int(17));
cartela8.append(int(25));
cartela8.append(int(19));
cartela8.append(int(45));
cartela8.append(int(38));
cartela8.append(int(32));
cartela8.append(int(33));
cartela8.append(int(39));
cartela8.append(int(54));
cartela8.append(int(59));
cartela8.append(int(52));
cartela8.append(int(58));
cartela8.append(int(46));
cartela8.append(int(69));
cartela8.append(int(71));
cartela8.append(int(63));
cartela8.append(int(64));
cartela8.append(int(61));


#Cartela de n° 9 ------------------------------------
#Criando a variável do tipo lista chamdao cartela9
cartela9 = list();
#Acrescentando os valores do tipo inteiro na variável cartela9
cartela9.append(int(13));
cartela9.append(int(7));
cartela9.append(int(3));
cartela9.append(int(4));
cartela9.append(int(15));
cartela9.append(int(21));
cartela9.append(int(30));
cartela9.append(int(26));
cartela9.append(int(16));
cartela9.append(int(23));
cartela9.append(int(35));
cartela9.append(int(40));
cartela9.append(int(36));
cartela9.append(int(32));
cartela9.append(int(41));
cartela9.append(int(51));
cartela9.append(int(59));
cartela9.append(int(49));
cartela9.append(int(46));
cartela9.append(int(58));
cartela9.append(int(73));
cartela9.append(int(67));
cartela9.append(int(68));
cartela9.append(int(66));
cartela9.append(int(65));


#Cartela de n° 10 -------------------------------------
#Criando a variável do tipo lista chamada cartela10
cartela10 = list();
#Acrescentando valores na variável do tipo lista chamada cartela10
cartela10.append(int(9));
cartela10.append(int(7));
cartela10.append(int(4));
cartela10.append(int(6));
cartela10.append(int(1));
cartela10.append(int(25));
cartela10.append(int(21));
cartela10.append(int(20));
cartela10.append(int(29));
cartela10.append(int(22));
cartela10.append(int(45));
cartela10.append(int(32));
cartela10.append(int(31));
cartela10.append(int(42));
cartela10.append(int(38));
cartela10.append(int(57));
cartela10.append(int(56));
cartela10.append(int(46));
cartela10.append(int(49));
cartela10.append(int(47));
cartela10.append(int(72));
cartela10.append(int(64));
cartela10.append(int(67));
cartela10.append(int(65));
cartela10.append(int(68));



for i in range(90):


    print('Atenção se prepare para os números');
    sleep(15);
    #A máquina escolhe um número aleatório.
    numero_sorteado = randint(1, 90);
    #mostra na tela o número sorteado
    print('Número: {}'.format(numero_sorteado));
    #cira uma variável de tipo lista para acrescentar os números sorteados
    lista_num_sorteados = list();
    #Acrescenta os valores dos números sorteados na varilavel lista_num_sorteados.
    lista_num_sorteados.append(int(numero_sorteado));






print('\n');
print(62*'~');
print('              JOGO DO BINGO EM DESENVOLVIMENTO!!');
print(62*'~');

