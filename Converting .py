import time

def typewritter(string):
    for char in string: 
        print(char, end="", flush=True)
        time.sleep(0.04)
        if char == "\n": 
            time.sleep(0.08)
    print("\n")




intro_text = """
You are Luo Mei Ling, a Chinese PhD student studying parapsychology in the United States.\n
You've always been fascinated by the paranormal and psychology, which led you to pursue a career in parapsychology.\n
You've studied under some of the top researchers in the field, and you've gained a reputation as one of the most promising young parapsychologists in the country.\n
Recently, you received word that your mother in Hushan, China has fallen ill. You felt compelled to return to your hometown to be with her, and to see if there's anything you can do to help.\n
You haven't been back to Hushan since you were a child, but you remember it as a bustling mining town nestled in the mountains\n
As you arrive in Hushan, you're struck by how much has changed.\n
The town is almost deserted now, with most of the shops and businesses closed down.\n
The streets are empty, and the few people you see give you a wide berth. You can't help but feel a sense of unease, like something isn't right.\n
Ever since you were young, you've had strange visions that have fascinated you with the paranormal and psychology.\n
Some of these visions are disturbing, violent, or take you to strange, nonsensical places with impossible architecture.\n
You've tried to ignore them over the years, but they've only become more frequent and intense.\n
It's been a few days since you arrived in Hushan, and you've been having strange dreams about the hospital on the mountain.\n
You remember it as a place where you went as a child when you were sick, but now it's abandoned and decrepit.\n
The dreams are always the same - you're wandering through the dark halls of the hospital, and there's a sense of impending doom.\n
One night, you're lying in bed, trying to sleep, when you hear a creepy voice that sounds like your father's voice.\n
Your father passed away many years ago, and you haven't thought about him in a long time.\n
The voice begs you to go find him in the hospital, as he needs your help.\n
You're not sure if it's a dream or if you're really hearing his voice, but you feel a strong urge to investigate.\n
"""

arriving_at_hospital_text = """
The hospital looms before you, its imposing brick facade rising up into the sky.\n
It's a two-story building, with the windows on the ground floor all boarded up.\n
The windows on the upper floors are all shattered, and the ivy that once covered the building has grown wild and unchecked.\n
The wood is old and warped, and some of the boards have fallen away, revealing the dark, empty interior beyond.\n
You can't help but think how different it looks from when you were a child.\n
Back then, the hospital was a place of comfort and healing.\n
Now, it's a place of decay and abandonment.\n
The only sound is the rustle of leaves and the occasional creak of metal.\n
There's a strange, almost palpable feeling of unease that seems to hang in the air.\n
The main entrance is a busted double door, hanging off its hinges, creaking eerily in the wind.\n
You can hear the faint rustle of leaves and the distant sound of creaking metal coming from inside the building.\n
"""

exploring_outside_text = """
You decide to explore the exterior of the hospital first, hoping to find another way in.\n
You walk around the building, taking in the overgrown courtyard and the twisted, rusted metal of what used to be a playground.\n
As you round the corner, you catch a glimpse of something moving in the shadows.\n
Your heart races as you try to determine if it's just your imagination playing tricks on you, or if there's something else out there with you.\n
As you're exploring the exterior of the hospital, you suddenly take notice of a window that's not boarded up like the rest of the windows.\n
It's on the ground floor, and there's a faint light coming from within the room.\n
You can't help but feel drawn to it, like it's calling out to you somehow.\n
"""

going_through_main_entrance_text = """
You cautiously approach the main entrance, careful not to step on any broken glass or loose debris.\n
The doors groan and creak as you push them open, revealing a dark and ominous interior.\n
As your eyes adjust to the dim light, you can make out a large reception desk.\n
You realize that you find yourself in the lobby of the hospital.\n
To your left, a door, half closed shakes slowly with faints gusts of wind.\n
Behind the reception desk, you can see the beggining of flight of stairs.\n
To your right, you notice a door marked 'Staff Only.'\n
The air is thick with the smell of wet wood, and there's a sense of foreboding that seems to permeate every inch of the space.\n
You steel yourself and take a step forward, unsure of what horrors might lie ahead.\n
"""



#Starting the program

def intro():
    typewritter(intro_text)
    time.sleep(1)
    while True:
        user_input = input(
            "When you're ready to continue, enter \"Continue\": ")
        if user_input.lower() == "continue":
            print("Your journey beggins !")
            time.sleep(2)
            arriving_hospital()
            break
        else:
            print("Invalid input, please check you entered \"Continue\"")

 


def arriving_hospital():
    typewritter(arriving_at_hospital_text)
    time.sleep(1)
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Go through the main entrance.")
        time.sleep(2)
        print("2. Explore the exterior.")
        time.sleep(2)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You cautiously approach the main entrance, taking care not to step on any broken glass or loose debris.")
            time.sleep(4)
            print("The doors groan as you push them open, revealing a dark and ominous interior.")
            time.sleep(3)
            going_through_main_entrance()
            break
        elif choice == "2":
            exploring_outside()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def going_through_main_entrance():
    typewritter(going_through_main_entrance_text)
    time.sleep(1)
    #add the choices there. or maybe the lobby
    pass



def exploring_outside():
    typewritter(exploring_outside_text)
    time.sleep(1)
    while True:
        print("What do you want to do ?")
        time.sleep(2)
        print("1. Take a look through the window")
        time.sleep(2)
        print("2. Continue exploring outside")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            glowing_window()
            break
        elif choice == "2":
            continue_exploring_outside()
            break
        else:
            print("Invalid choice. please enter a valid number.")
            time.sleep(2)

intro()