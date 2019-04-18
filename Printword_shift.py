import time
from collections import deque


def print_list(li):
    for i in range(len(li)):
        if li[i] == None:
            print(" ",end="")
        else:
            print(li[i],end="")
    print()

def printword(word,n):
    listi  = deque([word[i] for i in range(len(word))] + [None for i in range(n-len(word))])
    allpos = []
    i = 0
    for i in range(n):
        a = list(listi)
        allpos.append(a)
        listi.rotate(1)
    
    while True:
        print_list(allpos[i])
        if i+1 > n - 1:
            i = 0
        else:
            i += 1
        time.sleep(0.005)
        

    
        




printword("Nique ta mere",150)