#Max Kampel 2019
import random
player_moves = 0
bot_moves = 0
while player_moves < 36 and bot_moves < 36:
    user_input=input("Roll the dice? Y/N: ")
    if user_input == "Y":
        x = random.randint(1,6)
        if x == 1:
            print('''
  o
''')
        elif x == 2:
            print('''o

    o''')
        elif x == 3:
            print ('''o
  o
    o''')
        elif x == 4:
            print('''o    o

o    o''')
        elif x == 5:
            print ('''o   o
  o
o   o''')
        elif x == 6:
            print('''o    o
o    o
o    o''')
        print("You rolled a " + str(x))
        player_moves = player_moves + x
        y = random.randint(1,6)
        if y == 1:
            print('''
  o
''')
        elif y == 2:
            print('''o

    o''')
        elif y == 3:
            print ('''o
  o
    o''')
        elif y == 4:
            print('''o    o

o    o''')
        elif y == 5:
            print ('''o   o
  o
o   o''')
        elif y == 6:
            print('''o    o
o    o
o    o''')
        print("Your opponent rolled a " + str(y))
        bot_moves = bot_moves + y
    elif user_input == "N":
        y = random.randint(1,6)
        if y == 1:
            print('''
  o
''')
        elif y == 2:
            print('''o

    o''')
        elif y == 3:
            print ('''o
  o
    o''')
        elif y == 4:
            print('''o    o

o    o''')
        elif y == 5:
            print ('''o   o
  o
o   o''')
        elif y == 6:
            print('''o    o
o    o
o    o''')
        print("Your opponent rolled a " + str(y))
        bot_moves = bot_moves + y
    else:
        print ("Unknown input")
    print("Player Score: " + str(player_moves))
    print('#'*player_moves)
    print("Bot Score: " + str(bot_moves))
    print('#'*bot_moves)
if player_moves >= 36 and bot_moves >= 36:
    print("It's a tie!")
elif player_moves >= 36:
    print("You win!")
elif bot_moves >= 36:
    print("You lose!")
