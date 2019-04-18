import time
from collections import deque
import random

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
    le = int(n/2)
    for i in range(n):
        a = list(listi)
        allpos.append(a)
        listi.rotate(1)
    
    while True:
        print_list(allpos[le])
        next_one = random.choice([-1,1])
        if le+next_one > n-len(word) - 1:
            le = 0
        elif le-next_one < 0:
            le = n-len(word) - 1
        else:
            le += next_one
        time.sleep(0.01)
        

printword("word",100)