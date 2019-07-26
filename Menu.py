#ASCA 2019
from os.path import dirname, basename, isfile, join
import glob
import importlib
import time

#Get all the names of the games in one list called modules
module_paths = glob.glob(join(dirname(__file__), "Games", "*.py"))
module_names = [ basename(f)[:-3] for f in module_paths if isfile(f)]
modules = []

#Create the main menu prompt with all games listed and numbered, and create a list that will hold the actual module objects
menu_prompt = '''Which game would you like to play?
'''
for i in range(len(module_names)):
    menu_prompt = menu_prompt + '<' + str(i+1) + '> ' + module_names[i] + '\n'
    modules.append(None)
menu_prompt = menu_prompt + 'Please enter the number for your game, or press enter to exit.\n>>> '

print('''===============================================
             Welcome to
             ╔═╗╔═╗╔╦╗╔═╗╦ ╦╦ ╦╔╗ 
             ║ ╦╠═╣║║║║╣ ╠═╣║ ║╠╩╗
             ╚═╝╩ ╩╩ ╩╚═╝╩ ╩╚═╝╚═╝
===============================================
''')

#Keep asking the user to play a new game unless they enter invalid input
while True:
    user_in = input(menu_prompt)
    try:
        user_in = int(user_in)
        while user_in > len(modules) or user_in < 1:
            user_in = input("That was not a valid response, please try again.\n>>> ")
            user_in = int(user_in)
    except ValueError:
        user_in = input("Are you sure you want to exit GameHub? (Y/n)\n>>> ")
        if user_in != 'n':
            print("Goodbye for now!")
            break
        continue

    if modules[user_in - 1] == None:
        module = importlib.import_module('Games.' + module_names[user_in - 1])
        modules[user_in - 1] = module
    else:
        importlib.reload(modules[user_in - 1])
    
    time_increments = 22
    total_wait_time = 3
    print('                         ' + ('_'*time_increments))
    print('Time until next restart: ', end = '')
    for i in range(time_increments):
        print('#',end='')
        time.sleep( total_wait_time / time_increments - 0.004 ) #We assume each print takes 4 milliseconds
    print('''
===============================================
                    RESTART
===============================================
''')
