#Neel Kulkarni 2019

print ("Welcome, hero, you are the only one who can save us now. The evil monster has ravaged this island, killing hundreds. Please stop him quickly")
print ("Now, you must head to the valley of death, goodluck!")

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
        print ("You were spared, now you must look for a place to sleep")
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
