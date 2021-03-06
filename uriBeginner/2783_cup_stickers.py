'''
# -*- coding: utf-8 -*-
====2783_cup_stickers====
In Soccer World Cup year, the official album of cards is always a great success among children and also among adults.
For those who do not know, the album contains spaces numbered from 1 to N to paste the cards; each sticker, also numbered
from 1 to N, is a small photo of a player from one of the selections that will play the World Cup. The goal is to paste all
the cards in the respective spaces in the album, in order to complete the album (that is, leave no space without the corresponding sticker).

Some stickers are stamped and are rarer, harder to get. The stickers are sold in closed envelopes, so the buyer is not buying
the stickers he is buying, and may happen to buy a sticker that has already pasted on the album.

To help users, the company that sells the album and stickers wants to create an application that allows them to easily manage
the missing pieces to complete the album and is asking for their help.

Given the total number of spaces and stickers in the album (N), the list of stamped cards and a list of already purchased cards
(which may contain repeated stickers), your task is to determine how many stamped stickers are missing to complete the album.

Input
The first line contains three integers N (1 ≤ N ≤ 100), C (1 ≤ C ≤ N / 2) and M (1 ≤ M ≤ 300) respectively indicating the number
of cards (and spaces) of the album, the number of stamps stamped on the album and the number of cards already purchased. The second
line contains C distinct integers Xi indicating the stamps stamped on the album. The third line contains M integers Yi (1 ≤ Xi, Yi ≤ N)
indicating the cards already purchased.

Output
Your program should to produce an integer representing the number of the sitckers stamped that are missing to complete the album

=========Result_Test=========
====Input====
10 2 5
4 7
7 1 2 8 3
====Output====
1
'''
enterNCM = input().split()
totalN = int(enterNCM[0])
totalC = int(enterNCM[1])
totalM = int(enterNCM[2])

enterFigC = input().split()
vetC =[]
for i in range(totalC):
    vetC.append(int(enterFigC[i]))

enterFigM = input().split()
vetM = []
for i in range(totalM):
    vetM.append(int(enterFigM[i]))

missingC = totalC
for i in range(len(vetM)):
    for x in range(len(vetC)):
        if(vetM[i] == vetC[x]):
            missingC = missingC - 1

print(missingC)
'''
#Best Script
totalN,totalC,totalM = map(int,input().split())
vetC = list(map(int,input().split()))
vetM = list(map(int,input().split()))
missingC = 0
for i in vetC:
    if(i not in vetM):
        missingC+=1
print(missingC)
'''
