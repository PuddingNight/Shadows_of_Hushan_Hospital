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
"""

entering_Hospital_lobby_text = """
You step inside the hospital lobby and are immediately hit by the smell of decay and mildew.\n
The air is thick with dust and the floorboards creak underfoot.\n
The only sound is the distant sound of water dripping, echoing off the empty walls.\n
To your right, you notice a door leading to the toilets.\n
The door is slightly ajar, and you catch a glimpse of something moving in the shadows inside.\n
You can't shake the feeling that you're being watched.\n
To your left, you see a long corridor leading to the main entrance.\n
The corridor is lined with old posters and faded photographs, showing smiling doctors and nurses from a bygone era.\n
The pictures are now faded and torn, adding to the eerie atmosphere of the place.\n
Straight ahead of you, you notice a staff-only door.\n
It's rusted shut, and you can see through the gap that the hallway beyond is completely dark.\n
Next to the staff door, you notice a set of stairs that lead to the first floor.\n
In the middle of the room, there is a large reception desk.\n
The wood is old and there are piles of dusty papers and broken equipment scattered about.\n
As you stand there, taking in your surroundings, you can't help but feel a sense of dread.\n
The hospital is old and abandoned, and it feels like something terrible is lurking just around the corner.\n
"""

return_to_front_hospital_trough_main_entrance_text = """
You stand in front of the abandonned hospital.\n
The main entrance is a busted double door, hanging off its hinges, creaking eerily in the wind.\n
You can hear the faint rustle of leaves and the distant sound of creaking metal coming from inside the building.")\n
"""

glowing_window_text = """
You cautiously approach the window, peering inside the dimly lit room.\n
You can see a set of toilets, covered in dust and cobwebs.\n
As you're about to turn away, you notice something strange.\n
There's a faint glow coming from behind one of the stalls.\n
You can't quite make out what it is, but it's definitely something out of the ordinary.\n
"""


continue_exploring_outside_text ="""
You continue exploring the exterior of the hospital, searching for another way inside.\n
As you make your way around the side of the building, you spot a small window on the first floor that looks like it's been broken.\n
You notice a small pile of debris nearby that looks like it could be used to climb up and reach the window.\n
"""

entering_the_toilets_from_window_text = """
You carefully enter the bathroom, keeping an eye out for any signs of danger\n
You can see a door half open that leads to what seems to be a big room.\n
The sound of the wind whistles calmly through throughout the building.\n
Your eyes start to get used to darkness and you gather up the courage to find out what is this glow.\n
As you get closer to the glowing object, you realize it's a small music box.\n
It's covered in strange symbols and glyphs, and it seems to be emanating a faint energy."\n
You notice a small worn latch that keeps the box shut.\n
"""

opening_the_music_box_text = """
You cautiously open the music box, revealing its contents.\n
Inside, you find a small, ancient-looking artifact.\n
As you pick it up, you feel a strange sensation coursing through your body.\n
Suddenly, you're overcome with a vision of a person screaming and begging.\n
The vision is so vivid and intense that you feel like you're actually there, experiencing the terror and pain of the person in the vision.\n
When the vision ends, you find yourself back in the abandoned hospital, clutching the music box tightly.\n
You carefully tuck the music box into your bag.\n
"""

#Starting the program

#leads to arriving_hospital()
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

#Coming for intro() leads to :
# going_through_main_entrance() 
# exploring_outside()
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

#coming from arriving_hospital leads to :
# entering_hospital_lobby
def going_through_main_entrance():
    typewritter(going_through_main_entrance_text)
    time.sleep(1)
    entering_Hospital_lobby()
    


#Coming from arriving_hospital. leads to :
# glowing_window()
# continue_exploring_outside()
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


#coming from exploring_outside() leads to :
# entering_the_toilets_from_window()
# continue_exploring_outside()
def glowing_window():
    typewritter(glowing_window_text)
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Investigate the glow.")
        time.sleep(2)
        print("2. Continue exploring the exterior of the hospital.")
        time.sleep(2)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            entering_the_toilets_from_window()
            break
        elif choice == "2":
            continue_exploring_outside()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)

#Coming from glowing_window() leads to :
# opening_the_music_box() !!!!!!!!!!!!!!!! Need to add it !!!!!!!!!!!!
# entering_Hospital_lobby()
# continue_exploring_outside()
def entering_the_toilets_from_window():
    typewritter(entering_the_toilets_from_window_text)
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Open the box.")
        time.sleep(2)
        print("2. Leave the box alone and continue through the door.")
        time.sleep(2)
        print("3. Leave the box alone and go back outside from the window.")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            opening_the_music_box()
            break
        elif choice == "2":
            entering_Hospital_lobby()
            break
        elif choice == "3":
            print("You decide to hop back outside, you feel that something is not right.")
            time.sleep(4)
            continue_exploring_outside()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)

#coming from entering_the_toilets_from_the_window() or entering_toilets_from_door() Leads to :
#  to define !!!!!!!!!!!!!!!! Need to add it !!!!!!!!!!!!
def opening_the_music_box():
    typewritter(opening_the_music_box_text)
    time.sleep(1)
# to finish

#coming from exploring_outside() or glowing_window() Leads to :
# climbing_through_the_window() !!!!!!!!!!!!!!!! Need to add it !!!!!!!!!!!!
# return_to_main_entrance() !!!!!!!!!!!!!!!! Need to add it !!!!!!!!!!!!
def continue_exploring_outside():
    typewritter(continue_exploring_outside_text)
    time.sleep(1)
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Climb up to the window.")
        time.sleep(2)
        print("2. Keep searching for another way inside.")
        time.sleep(2)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            climbing_through_the_window()
            break
        elif choice == "2":
            return_to_main_entrance()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)





#Coming form going_through_main_entrance() leads to :
# return_to_front_hospital_trough_main_entrance()
# entering_staff_only() !!!!!!!!!!!!!!!! Need to add it !!!!!!!!!!!!
# sairs_first_floor() !!!!!!!!!!!!!!!! Need to add it !!!!!!!!!!!!
# Entering_the_toilets_from_door() !!!!!!!!!!!!!!!! Need to add it !!!!!!!!!!!!
def entering_Hospital_lobby():
    typewritter(entering_Hospital_lobby_text)
    time.sleep(1)
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Go outside from the main Entrance.")
        time.sleep(2)
        print("2. Try to open the staff only door.")
        time.sleep(2)
        print("3. Take the stairs for the first floor.")
        time.sleep(2)
        print("4. Go to the toilets of the lobby.")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You decide to leave the lobby through the main door.")
            time.sleep(2)
            return_to_front_hospital_trough_main_entrance()
            break
        elif choice == "2":
            print("You slowly pass through the main reception desk.")
            time.sleep(2)
            print(
                "A chill runs down your spine, you now stand in front of the door reserved for the staff.")
            time.sleep(2)
            print(
                "You put your hand on the door knob and feel something moist as you push it down.")
            entering_staff_only()
            break
        elif choice == "3":
            print(
                "You can feel the cold sweat on your forehead dripping down your black hair.")
            time.sleep(3)
            print("The stairs still are in a good condition.")
            time.sleep(2)
            print("while you are climbing the stairs, you can feel a presence near you.")
            time.sleep(2)
            stairs_first_floor()
            break
        elif choice == "4":
            print("You push slowly the door leading to the toilets of the lobby.")
            time.sleep(2)
            entering_the_toilets_from_door()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


#Comming from the lobby leads to going_through_the_main_entrance or exploring outside
def return_to_front_hospital_trough_main_entrance():
    typewritter(return_to_front_hospital_trough_main_entrance_text)
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





#dummy intro launch that needs to be moved.
intro()