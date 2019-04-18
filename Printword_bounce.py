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
    turn = "right"
    for i in range(n):
        a = list(listi)
        allpos.append(a)
        listi.rotate(1)
    
    while True:
        print_list(allpos[i])
        if turn == "right":
            if i+1 > n-len(word) - 1:
                turn = "left"
            else:
                i += 1
        elif turn == "left":
            if i-1 < 0:
                turn = "right"
            else:
                i -= 1
        time.sleep(0.01)
        

printword("Words",150)