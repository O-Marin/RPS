import random
import pylab

options = ('rock', 'paper', 'scissors')

c1Wins = 0
c2Wins = 0
draws = 0

def rps(c1, c2):
    beats = {'paper':'rock', 'rock':'scissors', "scissors":'paper'}
    if c2 == beats[c1]:
        global c1Wins
        c1Wins += 1
    elif c1 == beats[c2]:
        global c2Wins
        c2Wins += 1
    elif c1 == c2:
        global draws
        draws += 1

    return c1Wins, c2Wins, draws

records = {}

trials = [100,200,300,400,500]
for i in trials:
    for j in range(i):
        rps(random.choice(options), random.choice(options))
    print(c1Wins,c2Wins,draws)
    records[i] = (c1Wins,c2Wins,draws)

print(records)


f = open('texto.txt', 'w')
f.write(records)


