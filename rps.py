import random
options = ('rock', 'paper', 'scissors')

def rps(p1, p2):
    pl1 = 'Player 1 won!'
    pl2 = 'Player 2 won!'
    
    beats = {'paper':'rock', 'rock':'scissors', "scissors":'paper'}
    
    print("Human: ", end='')
    print(p1)
    print("Computer: ", end='')
    print(p2)

    if p2 == beats[p1]:
        return pl1
    elif p1 == beats[p2]:
        return pl2
    elif p1 == p2:
        return "Draw"
    
print('Please insert your choice')
p1 = input()

while p1 not in options:
    print('Please insert your choice')
    p1 = input()   

print("-----------------")
p2 = random.choice(options)
print(rps(p1,p2))