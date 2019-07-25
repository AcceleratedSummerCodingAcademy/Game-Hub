#Neel Kulkarni 2019

print ("Welcome, hero, you are the only one who can save us now. The evil monster has ravaged this island, killing hundreds. Please stop him quickly")
print ("Now, you must head to the Valley of Death, I have given you a sword to fight enemies, goodluck!")

x = int(input("Before going, would you like to get water and food? Yes -> 1. No -> 2."))

if x == 1:
    print ("You get a bottle of water and some canned food and leave")
else:
    print ("You leave without getting supplies")

print ("While crossing the hollow bridge, a couple of goblins ambush you")

n = int(input("Do you choose to fight -> 1. Or run -> 2?"))

if n == 1:
    print ("The goblins are too strong, you end up getting badly hurt, but something lures the goblins away, sparing you, but rendering you vulnerable")
    print ("You need to drink water")
    if x == 1:
        print ("You were spared, leaving some water, now you must look for a place to sleep")
    elif x == 2:
        print ("You didn't get your drink. Game over")
        game = o
else:
    print ("You begin to run away")
    if x == 2:
        print ("You run away safely")
    elif x == 1:
        print ("The food and water slow you down, the goblins catch up. Game over")
        game = o

print ("Now you are crossing the valley of shame")
c = int(input("You have two choices. Go to the lake and fetch some water -> 1. Or you can head on to find shelter before it gets dark -> 2."))

if c == 1:
    if x == 1:
        q = 1
        print ("You already have some water, you drink some and decide to foolishly lie down, and you start resting")
    elif x == 2:
        print ("You start your trek to the lake but it starts getting dark")
        q = 2
else:
    print ("You begin your to the Valley of Death")
    if x == 1:
       w = int(input(print("The extra weight slows you down so you lie down without finding shelter. Do you still wish to throw away your supplies somewhere in the distance? Yes -> 1. No -> 2.")))
    else:
        print("You find shelter and lie down for the night")
        w = 2

if q == 1:
    print ("You awake to find yourself well... alive!")
elif q == 2:
    print ("You get water and somehow make it through the night")

if w == 2:
    print("You wake and suddenly feel the urge for water, but upon realizing you don't have any, you begin to feel wierd and...")
    game = o
elif w == 1:
    print("Wow, surprisingly, you made it through the night. Your decision to keep supplies spared you, you think as you drink the refreshing water")

print("You finally make it to the arc of wisdom")
if q == 1:
    print ("The God of Thunder, the one who sent you on this quest reminds you to not be mindless")
else:
    print ("You have almost reached the Valley of Death")

print ("You are ambushed by the three musketeers, the most dangerous gunmen in the island")

e = int(input("Do you wish to fight back -> 1 , or make a run for it -> 2?"))

if e == 1:
    if w == 1:
        print ("You start running, but one musketeer shoots you. Well, what do you know? The bullet stops upon the supplies in your backpack")
    elif q == 2:
        print ("You start running, but one of the musketeers shoots you.")
        game = o
else:
    if w == 1:
        print ("Your supplies make your fighting sluggish, you die.")
        game = o
    elif q == 2:
        print ("You successfully fight of the musketeers")

print ("You reach the valley and open the Gates of Death")
print ("You are greeted by the God of Thunder, the one who sent you on this quest")

a = int(input("He lunges at you, do you wish do dodge -> 1, or counter with your sword -> 2?"))

if a == 2:
    print ("You roll, but you messed it up while jumping. Basically, you sprained your ankle, but thankfully, you're alive")
else:
    if q == 1:
        print ("You countered his attack, rendering him defensless")
        print ("He suddenly remembered your mindlessness, and in that moment, stabs you in a flash.")
        game = o
    else:
        print ("You countered his attack, rendering him defensless")

if a == 2:
    v = int(input("He comes at you, do you decide to dodge -> 1, or counter ->"))
else:
    print("You finish him, you win!")
    game = win

if v == 1:
    print ("Dodge his attack, and his lighting sword gets stuck in the ground, and you decide to finish him. You win!")
    game = win
elif v == 2:
    print ("You try to couner his attack, but fail, getting yourself killed.")
    game = o
        
    
