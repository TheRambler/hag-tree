from os import system
import time, sys, random

mood_level=0
is_tree=0

events = ['lawn1', 'flowers1']
success=0

print("You are an old woman. A very old woman. How old? No one knows. Except you. You think you were born in 2010... BCE.")
print("You find yourself in a quaint town.")
while 1:
    if mood_level<=mood_angry.mood_level_req:
        if mood_level>=mood_happy.mood_level_req:
            mood="Happy"
        else:
            mood="Angry"
    else:
        mood="Fine"
    if mood=="Fine":
        system("color "+mood_fine.mood_color)
        is_tree=0
    if mood=="Happy":
        system("color "+mood_happy.mood_color)
        is_tree=0
    if is_tree==2:
        if mood=="Angry": system("color "+mood_angry.mood_color)
    print("You are...")
    print(mood)
    if mood=="Angry":
        if is_tree==2:
            if mood_level<=-35:
                print("YOU CAN'T DO IT! YOU CAN'T DO THIS ANYMORE! TREEEEEEE MOOOOOODE!")
                is_tree=1
            elif mood_level<=-25:
                print("Grrr... Bits of your skin are turning into bark.")
            elif mood_level<=-15:
                print("Using your calming techniques, you are not turning into a tree.")
            print("You feel anger welling inside of you.")
            mood_level=mood_level-3
        else:
            is_tree=1
            print("Oh no! You are a tree because you are angry! Say rampage to unleash your potential! Or... say notree if you want to hold on to your humanity.")
    if is_tree==1:
        system("color 2c")
        if mood_level>mood_angry.mood_level_req:
            is_tree=0
    event = random.choice(events)
    event = eval(event)
    print(event.event_statement)
    command = raw_input("What do you do? ")
    if command=="1":
        print(event.outcome_1)
        exec(event.outcome_1_effect)
        success=1
    if command=="2":
        print(event.outcome_2)
        exec(event.outcome_2_effect)
        success=1
    if is_tree==1:
        if command=="rampage":
            print("yess.... yes.... YOU WILL SQUISH ALL THE INFERIORS! *sounds of squishing ensue*")
            is_tree=1
            success=1
            time.sleep(1)
        if command=="notree":
            print("No... Not here, not now. NOT NOW. I CAN'T BE A TREE!")
            is_tree=2
            success=1
            time.sleep(1)
    if command=="set_mood_angry":
        mood_level=-20
        success=1
    if command=="set_mood_happy":
        mood_level=20
        success=1
    if command=="set_mood_fine":
        mood_level=0
        success=1
    if command=="check_mood":
        print(mood_level)
        success=1
    if command=="exit":
        system("color 07")
        sys.exit("Exited with code 0")
    if mood_level>0: mood_level=mood_level-1
    if mood_level<0: mood_level=mood_level+1
    if success==0:
        print("Oops! I don't know how to do that!")
    success=0
    time.sleep(1)
    event=events
