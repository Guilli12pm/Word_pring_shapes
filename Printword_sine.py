import time
from collections import deque
import math

def sine(x):
    return math.sin(x)

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
    x = 0
    le = int(len(listi)/1.7) - 20
    for i in range(n):
        a = list(listi)
        allpos.append(a)
        listi.rotate(1)
    
    while True:
        print_list(allpos[le - int(sine(x)*n/(2+len(word)/10))])
        #print(i + int(sine(x)*(n/2.3)))
        if x > 2*math.pi:
            x = 0
        else:
            x += 0.01
        time.sleep(0.005)


printword("Word stuff",150)
        
        