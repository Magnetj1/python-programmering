total_sum = 0
win = 0
win2 = 0
while total_sum < 21:
    player_2 = int(input("player 1 will you add 1 2 or 3 to the total?"))
    total_sum += player_2
    if player_2 > 3 or player_2 < 1:
        print("DONT CHEAT PLAYER 1!!!!")
        total_sum = 200000
    else:
         win2 = total_sum
    if total_sum > 21:
        print("YOU BOTH LOSE!!!")
        break
    if win2 == 21:
        print("PLAYER 1 WINS!")
        break
    player_1 = int(input("player 2 will you add 1 2 or 3 to the total?"))
    total_sum += player_1
    if player_1 == 1 or 2 or 3:
        win = total_sum
    if player_1 > 3 or player_1 < 1:
        print("DONT CHEAT PLAYER 2!!!!")
        total_sum = 200000
    if total_sum > 21:
        print("YOU BOTH LOSE!!!")
        break
    if win == 21:

        print("PLAYER 2 WINS!")
        break
