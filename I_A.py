NO_GOOD_MOVE = -1
import random

def get_move(coins,maxmove):
    ntaken = findGoodMove(coins,maxmove)
    if (ntaken == NO_GOOD_MOVE):
        num = random.randint(1,maxmove)
        #print("Retire %r monedas" %(num))
        return num
    else:
        #print("Retire %r monedas" %(ntaken))
        return ntaken

def findGoodMove(coins,maxmove):
    #print("Estoy Pensando")
    limit = min(coins,maxmove)
    for i in range(1,limit+1):
        if (isBadposition(coins - i,maxmove)) : return i
    return NO_GOOD_MOVE

def isBadposition(coins,maxmove):
    if coins == 1 : return True
    return findGoodMove(coins,maxmove) == NO_GOOD_MOVE
