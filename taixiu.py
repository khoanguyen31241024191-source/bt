import random
win_time = 0
lose_time = 0
turn_play = 0
while True:
    turn_play += 1
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    if total > 5:
        a = 'tài'
    else:
        a = 'xỉu'

    money_you_have = int(input('The money you have: '))
    while True:
        money_you_put = int(input('The money you put: '))
        if money_you_put > money_you_have:
            print('Not enough money, please enter a smaller amount.')
        elif money_you_put <= 0:
            print('Please enter a positive amount.')
        else:
            break
    guess = input('What do you guess, tài or xỉu: ')
    guess = guess.lower()
    while True:
        if a == guess:
            win_time += 1
            money_you_have += money_you_put
            print(die1, die2)
            print('You win', 'Now you have', money_you_have)
        else:
            money_you_have -=money_you_put
            print(die1, die2)
            lose_time += 1
            print('You lose', 'Now you have', money_you_have)
        break

    ans_of_player = input('Do you want to play again? (y/n): ')
    ans_of_player = ans_of_player.lower()
    if ans_of_player == 'y':
        continue
    else:
        break

print('you played',turn_play,'turn')
print('you win', win_time,'turn')
print('you lose', lose_time,'turn')
print( 'Now you have:',money_you_have)


