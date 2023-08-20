'''
Projeto Jogo do Bingo
Autor: Eduardo Machado de Souza
Inicio projeto: 20/08/2023

'''
#canto das importações de bibliotecas da linguagem python
#importando a biblioteca de tempo
import time;



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
cartela2.append(int(14));
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

print('\n');
print(62*'~');
print('              JOGO DO BINGO EM DESENVOLVIMENTO!!');
print(62*'~');