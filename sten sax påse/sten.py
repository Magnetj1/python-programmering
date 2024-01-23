import random

game = 0 
player1 = 0
pc = 0 

while game < 3:
    p1 = int (input ("1 = sten, 2 = sax, 3 = påse, bdw its a best out of 3! are you better than the code?"))
    p2 = random.randint(1,3)
    
    if p1 == p2:
        print ("Tie")
        game += 1 
    if p1 == 1 and p2 == 2:
        player1 += 1
        game += 1
        print ("Player wins")
    if p1 == 1 and p2 == 3:
        pc += 1 
        game +=1
        print ("PC wins")
    if p1 == 2 and p2 == 3:
        player1 += 1 
        game += 1
        print ("Player wins")
    if p1 == 2 and p2 == 1:
        pc += 1 
        game += 1
        print ("PC wins")

    if game == 3:
        if pc == player1:
            print("TIE, woah you trash!")
        if player1 > pc:
            print("Player wins the game, bdw you still arent better than the code its a game of chance you bafon! ")
        else:
            print ("Pc wins the game, sadly you arent better than the code.... big L THATS TO EZ!")
    