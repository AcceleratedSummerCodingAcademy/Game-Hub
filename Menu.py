#ASCA 2019
from os.path import dirname, basename, isfile, join
import glob
import importlib
import time

#Get all the names of the games in one list called modules
module_paths = glob.glob(join(dirname(__file__), "Games", "*.py"))
modules = [ basename(f)[:-3] for f in module_paths if isfile(f)]

#Create the main menu prompt with all games listed and numbered
menu_prompt = '''Which function would you like to test?
'''
for i in range(len(modules)):
    menu_prompt = menu_prompt + '<' + str(i+1) + '> ' + modules[i] + '\n'
menu_prompt = menu_prompt + 'Please enter the number for your game, or press enter to exit.\n>>> '

while True:
    user_in = input(menu_prompt)
    try:
        user_in = int(user_in)
    except ValueError:
        print("Goodbye for now!")
        break

    importlib.import_module('Games.' + modules[user_in - 1])
    
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
