from sys import exit

def pink_room():
    print("You find sign:")
    print("\tSolve this mathmatical equation\n")
    print("\t234(2360 + 6345 x 8231 - 20868 / 467655) \n")
    print("* hint - the answer isn't a number, are you really gonna do the equation? (yes or no) *")

    choice = input("> ")


    if "yes" in choice:
        print("Ha nerd.")
        print("* gets knocked out *")
        start()
    elif "no" in choice:
        dead("I can't deal with your stupidity")
    else: 
        pink_room()

def up():
    print("After 10 mins of climbing, you end up in another room")
    print("You see: ")
    print(""" \tChoose your destiny\n""")
    print("And underneath are two buttons: ")
    print("\t red button")
    print("\tgreen button \n")
    print("Which do you click?\n")
    room_unlocked = False 

    while True: 
        choice = input("> ")

        if choice == "red":
            dead("The button expoldes the hidden bomb at the bottom")
        elif choice == "green" and not room_unlocked:
            print("A door opens behind you but has two paths.")
            print("Which do you take?")
            print("- left")
            print("- right\n")
            room_unlocked = True 
        elif choice == "left" and room_unlocked:
            dead("You follow the path to a dead end and an anvil falls from the sky and you die.")
        elif choice == "right" and room_unlocked:
            pink_room()
        else:
            print("Not a choice, make one.")

def down():  
    print("\nYou enter a new room. There is a math equation on the wall.")
    print("""There is a sign that says: """) 
    print(""" "Solve the equation to be free" \n""")
    print("\t  5 x 6 / 3 x 21 ")
    print("\t What's the answer?\n")

    choice = input ("> ")
    how_much = int(choice)

    if how_much == 210:
        print("Nice, you're free this one time, you win!")
        exit(0)
    else: 
        dead("You're dumb. HAHA")
        

def dead(why):
    print(why, ", Good job?")
    exit(0)

def start():
    print("You wake up groggy in a room and see a ladder.")
    print("The ladder leads 'up' or 'down'")
    print("Which way do you take? \n ")

    choice = input("> ")

    if choice == "up":
        up()
    elif choice == "down":
        down()
    else:
        dead("The platform beneth you drops you down to death")

start()            