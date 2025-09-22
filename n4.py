hundreds = 0
fifties = 0
tens = 0
fives = 0
two = 0
ones = 0
x = int(input())
while(x >= 100):
    x-=100
    hundreds+=1
while(x >= 50):
    x-=50
    fifties+=1
while(x >= 10):
    x-=10
    tens+=1
while(x >= 5):
    x-=5
    fives+=1
while(x >= 2):
    x-=2
    two+=1
while(x >= 1):
    x-=1
    ones+=1

print(hundreds, " ", fifties, " ", tens, " ", fives, " ", two, " ", ones)