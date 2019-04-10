'''
# -*- coding: utf-8 -*-
2401_calculadora
Solicitando Boas Contas (SBC) é uma organização de inspeção de calculadoras. Todos os 
fabricantes procuram ter o selo de qualidade da SBC, que faz com que os clientes comprem 
o produto sem preocupação com contas erradas.

Você está encarregado de testar máquinas que fazem apenas operações de multiplicação e 
divisão. Além disso, o termo a ser digitado em cada operação (que dividirá ou multiplicará 
o número atualmente exibido no visor) só pode conter um único dígito.

A calculadora exibe o número 1 quando ligada. Depois disso, o usuário pode digitar um número 
com um único dígito e escolher se esse número deve multiplicar ou dividir o número exibido 
anteriormente; o resultado da operação escolhida é então exibido na calculadora. Pode-se repetir 
esse processo indefinidamente.

Apesar de só podermos entrar com números inteiros de um dígito, o visor da calculadora permite 
exibir números com múltiplos dígitos e até mesmo números fracionários.

Dada uma sequência de operações que foram realizadas nessa calculadora logo depois de ligada, sua 
tarefa é conferir o resultado exibido.

No primeiro caso de teste abaixo, o usuário deseja calcular o resultado da seguinte expressão: 
1 × 2 × 1 × 3. Note que a primeira ocorrência do número 1 vem do fato da calculadora mostrar inicialmente 
1 ao invés de 0.

No segundo caso de teste abaixo, o usuário deseja calcular o resultado da seguinte expressão: 
((1/2)/3) × 6.

Entrada
A primeira e única linha da entrada contém um inteiro N (1 ≤ N ≤ 100 000). Cada uma das próximas N linhas 
contém um dígito e um caractere '*' ou '/', que representam uma operação realizada na calculadora.

Saída
Seu programa deve imprimir uma única linha contendo o resultado que deve ser exibido pela calculadora 
ao final das operações.

=========Result_Test=========
====Input====
3
2 *
1 *
3 *
====Output====
6
'''
n = int(input())

result = 1
for i in range(n):
  enter=input().split()
  dig = int(enter[0])
  carac = str(enter[1])
  if(carac == "*"):
    result = result * dig
  elif(carac == "/"):
    result = result / dig

print("{:.0f}".format(result))

