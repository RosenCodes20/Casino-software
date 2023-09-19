import random
print("Welcome to the Slot Machine Game")

symbols=['🍒', '🍉', '🍇', '🍊']
balance=int(input("Enter your initial balance:"))

bet=0

while balance>0:
    print(30*'-')
    print("Current Balance",balance)
    while True:
       bet=int(input("Enter your bet amount (0 to exit):"))
       if bet==0:
        break
       if bet>balance:
        print('Insufficient balance.Please lower bet!:')
       else:
         break
    if bet==0:
        break
    balance-=bet
    print("Spinning the reels.....")
    reel1=random.choice(symbols)
    reel2=random.choice(symbols)
    reel3=random.choice(symbols)
    print(reel1,reel2,reel3)
    if reel1==reel2==reel3:
        winnings=bet*10
        balance+=winnings
        print("Congratulations! You won",winnings,"money!")
    elif reel1==reel2 or reel2==reel3:
        winnings=bet*2
        balance+=winnings
        print("Congratulations! You won", winnings, "money!")
    else:
        print("Sorry!No match.Better luck next time!")
print("Game over.Final balance:",balance)



