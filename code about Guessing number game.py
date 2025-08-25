import random
times = 0
time = 0
win_time = 0
lose_time = 0
turn_play = 0
money_you_have = 100
money_you_put = 50
win = False
while True:
    if money_you_have > 0:
        turn_play += 1
        print( 'Computer think a number from 1 to 100 and you guess it.')
        com_guess = random.randint(1,100)
        print('game has 3 level: 1, 2, 3,\n1: easy.\n2: medium.\n3: hard')
        while True:
            level = int(input(' choose your level you want: '))
            if level == 1:
                times = 10
                print(' you have',times,' to guess number of computer')
                break
            elif level == 2:
                times = 5
                print(' you have',times,' to guess number of computer')
                break
            elif level == 3:
                times = 3
                print(' you have',times, 'to guess number of computer')
                break
            else:
                print('please enter your level again')
                continue
        for time in range(times):
            guess = int(input('Enter your guess in time ' + str(time + 1) + ': '))
            if guess == com_guess and time + 1 <= times:
                win = True
                print('correct')
                print(com_guess)
                break
            else:
                if guess < com_guess:
                    print('Your guess was too low.')
                elif guess > com_guess:
                    print('Your guess was too high.')
                    win = win
        if win == True and time + 1 <= times:
            money_you_have += money_you_put
            win_time += 1
            print('computer guess: ', com_guess)
        else:
            money_you_have -= money_you_put
            lose_time += 1
            print('computer guess: ', com_guess)
            print('--------------------GAME OVER--------------------')
        ans_of_player = input('Do you want to play again? (y/n): ')
        ans_of_player = ans_of_player.lower()
        if ans_of_player == 'y':
            continue
        else:
            break
    else:
        print('you dont have money, Get out of here and come back when you can actually pay!')
        break
print('you played',turn_play,'turn')
print('you win', win_time,'turn')
print('you lose', lose_time,'turn')
print( 'Now you have:',money_you_have)





