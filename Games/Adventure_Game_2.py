#Helen Kota 2019
def run():
    '''runs game'''
    answer = input('You have just been whisked away to a faraway island. A lady wearing a fancy dress is walking toward you. Walk away(1) or stay(2). ')

    if answer == '1':
        print('Suddenly, a big portal opens in front of you and you come back to Earth.You live a normal life. MISSION FAILED!')
    elif answer == '2':
        answer = input('The lady says that a precious gem has been stolen from the island. She wants you to find it. What do you say? Yes(1), or No(2). ')
    if answer == '1':
        answer == input('She gives you a choice of supplies. Rope(1) or Flintstone(2)')
        if answer == '1':
            answer = input('You take the rope and proceed. Suddenly, a dragon with a diamond attacks you. Fight(1) or run(2)?')
            if answer == '1':
                print('You fight the dragon, but he is too strong. He kills you. MISSION FAILED!')
            if answer == '2':
                input('You run away.')
            
        if answer == '2':
            print('You take the flint  and proceed. You do not realize, but the flint falls out of your pocket and rubs on a stone. A fire starts. MISSION FAILED!')  
            
    elif answer == '2':
        print('The lady waves her hand. Suddenly, a big portal opens in front of you and you come back to Earth.You live a normal life. MISSION FAILED!') 
run()
