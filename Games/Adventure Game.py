#Neel Kulkarni 2019

print ("Welcome, hero, you are the only one who can save us now. The evil monster has ravaged this island, killing hundreds. Please stop him quickly")
print ("Now, you must head to the Valley of Death, goodluck!")

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
c = int(input("You have two choices. Go to the lake and fetch some water -> 1. Or you can head on to find shelter before it gets dark -> 2.

if c == 1:
    if x == 1:
        q = 1
        print ("You already have some water, you drink some and decide to foolishly lie down, and you start resting")
    else:
        print ("You start your trek to the lake but it starts getting dark")
        q = 2
else:
    print ("You begin your to the Valley of Death")
    if x == 1:
       w = int(input(print("The extra weight slows you down so you lie down without finding shelter. Do you still wish to throw away you supplies? Yes -> 1. No -> 2.")))
    else:
        print("You find shelter and lie down for the night")
        w = 2

if q == 1
    print ("You awake to find yourself ambushed by a tiger. It eats you."
    game = o
if q == 2
    print ("You get water and somehow make it through the night")


