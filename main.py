#import statments
import time
import random
#these are some variables needed in-game
room1_visited = False
room2_visited = False
room3_visited = False
lever1 = ""
lever2 = ""
lever3 = ""
pass1 = str(random.randint(2, 9))
pass2 = str(random.randint(2, 9))
pass3 = str(random.randint(2, 9))
pass4 = str(random.randint(2, 9))
passcode = pass1 + pass2 + pass3 + pass4
sword = random.choice(["shiny", "rusty"])
score = 0
#This function creates a print statment with sleep time in it
def print_sleep(text, wait_time):
    print(text)
    time.sleep(wait_time)
#This function containes the description of the game
def intro():
    print_sleep("Welcome to the ancient Egyptian world, where mysteries await "
                "your discovery.", 2)
    print_sleep("Uncover the secrets of the pharaohs, and unlock the power of "
                "the gods.", 2)
    print_sleep("May Ra's light guide your path and Osiris bless your "
                "journey.", 2)
    print_sleep("Prepare for an unforgettable adventure!", 2)
    print_sleep("In this game you play as a tourist who visited Egypt", 2)
    print_sleep("One day he visited Sakkara temple", 2)
    print_sleep("And he found a secret room", 1)
    print_sleep("Once you enter the room the door behind you locks", 2)
    print_sleep("you find three rooms in front of you ", 2)
    print_sleep("in this game there is a scoring system", 1)
    print_sleep("as well as win and lose conditions", 1)
    print_sleep("", 1)
    intro_answer = ""
    while intro_answer not in ["start"]:
        intro_answer = input("To start the game type in start\n")
        if intro_answer == "start":
            hall()
#This function asks the player if he wants to play again
def play_again():
    choice = ""
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)\n")
        if choice == 'n':
            print_sleep("Thanks for playing!", 2)
            quit()
        elif choice == 'y':
            print_sleep("Great! Restarting the game", 2)  
            reset()
#This function resets all values
def reset():
    global room1_visited
    global room2_visited
    global room3_visited
    global lever1
    global lever2
    global lever3
    global pass1
    global pass2
    global pass3
    global pass4
    global passcode
    global sword
    global score
    room1_visited = False
    room2_visited = False
    room3_visited = False
    lever1 = ""
    lever2 = ""
    lever3 = ""
    pass1 = str(random.randint(2, 9))
    pass2 = str(random.randint(2, 9))
    pass3 = str(random.randint(2, 9))
    pass4 = str(random.randint(2, 9))
    passcode = pass1 + pass2 + pass3 + pass4
    sword = random.choice(["shiny", "rusty"])
    score = 0
    intro()
#This function defines the main room in the game
def hall():
    global sword
    global score
    print_sleep("your score is " + str(score), 1)
    print_sleep("Choose where do you want to go", 2)
    print_sleep("room 1?", 1)
    print_sleep("room 2?", 1)
    print_sleep("Or room 3?", 1)
    room_choice = ""
    while room_choice  not in ["1", "2", "3"]:
        room_choice = input("type 1, 2, or 3\n")
        if room_choice == "1":
            if room1_visited:
                print_sleep("there is nothing to do there", 2)
                hall()
            else:
                room1()
        elif room_choice == "2":
            if room2_visited and sword == "shiny":
                print_sleep("There is nothing to do there.", 2)
                hall()
                
            elif room3_visited and sword == "rusty":
                room2()
                
            elif lever2 == 1:
                print_sleep("There is nothing to do there", 2)
                hall()
            else:
                room2()
    
        elif room_choice == "3":
            if room3_visited:
                hall2()
            else:
                room3()
#This function contains the story of room 1
def room1():
    global lever1
    global room1_visited
    global score
    room1_visited = True
    print_sleep("You enter the room you find a lever and next to it a papyrus", 2)
    print_sleep("you pick the papyrus and read it", 2)
    print_sleep(f"In the {pass1} night with {pass2} moons there is a secret", 2)
    lever1_choice = ""
    while lever1_choice not in ["y", "n"]:
        lever1_choice = input("choose to open the lever or not (y/n)\n")
    if lever1_choice == "y":
        print_sleep("You open the lever and nothing happens so you leave the room", 2)
        lever1 = 1
        score += 10
        hall()
    elif lever1_choice == "n":
        print_sleep("You leave the room and go back to the hall", 2)
        hall()
#This function contains the story of room 2
def room2():
    global room2_visited
    global lever2
    global lever3
    global sword
    global score
    if room3_visited and sword == "rusty":
        print_sleep("now you can upgrade your sword", 2)
        print_sleep("you upgrade it and go back to the large room", 2)
        sword = "shiny"
        score += 10
        hall2()
    else:
        print_sleep("You enter the room and find an Anubis statue, the god of "
                    "death", 2)
        print_sleep("and below the statue you find two levers", 2)
        if sword == "rusty":
            print_sleep("and at the end of the room, there is an upgrade machine", 2)
        print_sleep("type 1 to pull the first lever", 2)
        print_sleep("type 2 to pull the second lever", 2)
        while True:
            levers_choice = input("choose what do you want to do<1,2>\n")
            if levers_choice == "1":
                print_sleep("you pull the first lever and nothing happens", 2)
                lever2 = 1
                score +=  10
            elif levers_choice == "2":
                print_sleep("you pull the second lever and nothing happens", 2)
                lever3 = 1
                score += 10
            if lever2 == 1 and lever3 ==1:
                break 
        print_sleep("so you try to pull both at the same time and it finally works", 2)
        print_sleep("the giant statue starts speaking", 2)
        print_sleep(f"In this night, you will kill {pass3} people and eat {pass4} cats", 2)
        print_sleep("after the statue finishes speaking, a key falls from the ceilling", 2)
        print_sleep("you get confused but you take the key and go back to the hall", 2)
        room2_visited = True
        hall()
#This function contains the story of room 3
def room3():
    global room3_visited
    global score
    if lever1 == 1 and lever2 == 1 and  lever3 == 1:
        print_sleep("You find a door with a passcode, and beside it, a chest.", 2)
        print_sleep(f"You open the chest and find a {sword} sword.", 2)
        score += 10
        print_sleep("You take the sword and check the door.", 2)
        print_sleep("It needs a password.", 1)
        print_sleep("HINT<papyrus and statue>", 2)
        trials = 3
        while True:
            user_passcode = input("Type in the password: ")
            if user_passcode == passcode:
                print_sleep("Correct password.", 2)
                score  += 20
                break
            elif user_passcode != passcode:
                trials -= 1
                score -= 5
                if trials == 0:
                    print_sleep("you have been locked here forever", 2)
                    play_again()
                else:
                    print_sleep(f"Wrong passcode, you have {trials} trial left", 2)
        print_sleep("the door opens and you enter another large room", 2)
        room3_visited = True
        hall2()
    else:
        print_sleep("the room is looked", 2)
        hall()
#This function containes the lake part in the story
def hall2():
    global score
    print_sleep("your score is " + str(score), 1)
    print_sleep("Inside the room, you find a lake with crocodiles in it", 2)
    print_sleep("type 1 to swim in the lake", 2)
    print_sleep("type 2 to go back", 2)
    hall2_choice = ""
    while hall2_choice not in ["1", "2"]:
        hall2_choice = input("what do you want to do?<1,2>\n")
        if hall2_choice == "1":
            if sword == "rusty":
                print_sleep("you swim and try to attack them with the rusty sword but fail and die", 2)
                play_again()
            elif sword == "shiny":
                print_sleep("you swim and attack them and go to the other side of the lake", 2)
                score += 10
                boss()
        elif hall2_choice == "2":
            hall()
#This function contains the code of the boss fight
def boss():
    global score
    print_sleep("your score is " + str(score), 1)
    print_sleep("You continue and find a large door with the eye of horus on it", 2)
    print_sleep("You use the key on the door and it opens", 2)
    print_sleep("inside you find a mommy that is protecting the exit door", 2)
    print_sleep("you attack it with your shiny sword", 1)
    print_sleep("Fervor <1>", 1)
    print_sleep("Vengeance <2>", 1)
    print_sleep("invigorate <3>", 1)
    attack1 = ""
    mommy_health = 150
    while attack1 not in ["1", "2", "3"]:
        attack1 = input ("choose number of attack<1,2,3>\n")
        if attack1 == "1":
            mommy_health -= 70
            score += 25
            print_sleep("mommy health = " + str(mommy_health), 2)
        elif attack1 == "2":
            score += 15
            mommy_health -= 50
            print_sleep("mommy health = " + str(mommy_health), 2)
        elif attack1 == "3":
            mommy_health -= 60
            score += 20
            print_sleep("mommy health = " + str(mommy_health), 2)
    print_sleep("Nice attack!", 1)
    print_sleep("but you still have more to go", 2)
    print_sleep("your score is " + str(score), 1)
    print_sleep("Terror <1>", 1)
    print_sleep("Barrage <2>", 1)
    print_sleep("Fussilade <3>", 1)
    attack2 = ""
    while attack2 not in ["1", "2", "3"]:
        attack2 = input ("choose number of attack<1,2,3>\n")
        if attack2 == "1":
            mommy_health -= 80
            score += 25
            print_sleep("mommy health = " + str(mommy_health), 2)
        elif attack2 == "2":
            score += 20
            mommy_health -= 60
            print_sleep("mommy health = " + str(mommy_health), 2)
        elif attack2 == "3":
            score += 10
            mommy_health -= 50
            print_sleep("mommy health = " + str(mommy_health), 2)
        if mommy_health < 0:
            print_sleep("Finally you kill him", 2)
            End()
        elif  mommy_health > 0:
            print_sleep("Great :)", 1)
            print_sleep("Defile <1>", 1)
            print_sleep("Shiv <2>", 1)
            print_sleep("Ooze <3>", 1)
            attack3 = ""
            while attack3 not in ["1", "2", "3"]:
                attack3 = input ("choose number of attack<1,2,3>\n")
                if attack3 == "1":
                    mommy_health -= 70
                    score += 15
                    if mommy_health < 0:
                        mommy_health = 0
                    print_sleep("mommy health = " + str(mommy_health), 2)
                elif attack3 == "2":
                    score += 5
                    mommy_health -= 55
                    if mommy_health < 0:
                        mommy_health = 0
                    print_sleep("mommy health = " + str(mommy_health), 2)
                elif attack3 == "3":
                    mommy_health -= 60
                    score += 10
                    if mommy_health < 0:
                        mommy_health = 0
                    print_sleep("mommy health = " + str(mommy_health), 2)
    print_sleep("you finally kill him", 1) 
    End()
#This function ends the story
def End():
    print_sleep("You open the exit and escape", 2)
    print_sleep("your final score is " + str(score), 1)
    print_sleep("try again maybe you will get higher score", 1)
    play_again()

intro()
