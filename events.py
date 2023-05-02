import time


def intro_scene():
    print("You are Luo Mei Ling, a Chinese PhD student studying parapsychology in the United States.")
 #   time.sleep(5)
    print("You've always been fascinated by the paranormal and psychology, which led you to pursue a career in parapsychology.")
 #   time.sleep(7)
    print("You've studied under some of the top researchers in the field, and you've gained a reputation as one of the most promising young parapsychologists in the country.")
 #   time.sleep(10)
    print("Recently, you received word that your mother in Hushan, China has fallen ill. You felt compelled to return to your hometown to be with her, and to see if there's anything you can do to help.")
 #   time.sleep(12)
    print("You haven't been back to Hushan since you were a child, but you remember it as a bustling mining town nestled in the mountains.")
 #   time.sleep(10)
    print("As you arrive in Hushan, you're struck by how much has changed.")
 #   time.sleep(7)
    print("The town is almost deserted now, with most of the shops and businesses closed down.")
  #  time.sleep(6)
    print("The streets are empty, and the few people you see give you a wide berth. You can't help but feel a sense of unease, like something isn't right.")
 #   time.sleep(9)
    print("Ever since you were young, you've had strange visions that have fascinated you with the paranormal and psychology.")
 #   time.sleep(8)
    print("Some of these visions are disturbing, violent, or take you to strange, nonsensical places with impossible architecture.")
 #   time.sleep(9)
    print("You've tried to ignore them over the years, but they've only become more frequent and intense.")
 #   time.sleep(8)
    print("It's been a few days since you arrived in Hushan, and you've been having strange dreams about the hospital on the mountain.")
 #   time.sleep(10)
    print("You remember it as a place where you went as a child when you were sick, but now it's abandoned and decrepit.")
 #   time.sleep(7)
    print("The dreams are always the same - you're wandering through the dark halls of the hospital, and there's a sense of impending doom.")
 #   time.sleep(10)
    print("One night, you're lying in bed, trying to sleep, when you hear a creepy voice that sounds like your father's voice.")
  #  time.sleep(9)
    print("Your father passed away many years ago, and you haven't thought about him in a long time.")
 #   time.sleep(7)
    print("The voice begs you to go find him in the hospital, as he needs your help.")
  #  time.sleep(6)
    print("You're not sure if it's a dream or if you're really hearing his voice, but you feel a strong urge to investigate.")
 #   time.sleep(9)

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
    print("The hospital looms before you, its imposing brick facade rising up into the sky.")
    time.sleep(3)
    print("It's a two-story building, with the windows on the ground floor all boarded up.")
    time.sleep(4)
    print("The windows on the upper floors are all shattered, and the ivy that once covered the building has grown wild and unchecked.")
    time.sleep(6)
    print("The wood is old and warped, and some of the boards have fallen away, revealing the dark, empty interior beyond.")
    time.sleep(5)
    print("You can't help but think how different it looks from when you were a child.")
    time.sleep(3)
    print("Back then, the hospital was a place of comfort and healing.")
    time.sleep(4)
    print("Now, it's a place of decay and abandonment.")
    time.sleep(4)
    print("The only sound is the rustle of leaves and the occasional creak of metal.")
    time.sleep(3)
    print("There's a strange, almost palpable feeling of unease that seems to hang in the air.")
    time.sleep(5)
    print("The main entrance is a busted double door, hanging off its hinges, creaking eerily in the wind.")
    time.sleep(5)
    print("You can hear the faint rustle of leaves and the distant sound of creaking metal coming from inside the building.")
    time.sleep(5)

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
            print(
                "The doors groan as you push them open, revealing a dark and ominous interior.")
            time.sleep(3)
            going_through_main_entrance()
            break
        elif choice == "2":
            exploring_outside()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def exploring_outside():
    print("You decide to explore the exterior of the hospital first, hoping to find another way in.")
    time.sleep(4)
    print("You walk around the building, taking in the overgrown courtyard and the twisted, rusted metal of what used to be a playground.")
    time.sleep(6)
    print("As you round the corner, you catch a glimpse of something moving in the shadows.")
    time.sleep(3)
    print("Your heart races as you try to determine if it's just your imagination playing tricks on you, or if there's something else out there with you.")
    time.sleep(8)
    print("As you're exploring the exterior of the hospital, you suddenly take notice of a window that's not boarded up like the rest of the windows.")
    time.sleep(8)
    print("It's on the ground floor, and there's a faint light coming from within the room.")
    time.sleep(4)
    print("You can't help but feel drawn to it, like it's calling out to you somehow.")
    time.sleep(4)
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


def glowing_window():
    print("You cautiously approach the window, peering inside the dimly lit room.")
    time.sleep(4)
    print("You can see a set of toilets, covered in dust and cobwebs.")
    time.sleep(4)
    print("As you're about to turn away, you notice something strange.")
    time.sleep(3)
    print("There's a faint glow coming from behind one of the stalls.")
    time.sleep(4)
    print("You can't quite make out what it is, but it's definitely something out of the ordinary.")
    time.sleep(4)

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


def continue_exploring_outside():
    print("You continue exploring the exterior of the hospital, searching for another way inside.")
    time.sleep(4)
    print("As you make your way around the side of the building, you spot a small window on the first floor that looks like it's been broken.")
    time.sleep(5)
    print("You notice a small pile of debris nearby that looks like it could be used to climb up and reach the window.")
    time.sleep(5)

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


def return_to_main_entrance():
    print("You decide to keep searching for another way inside.")
    time.sleep(4)
    print("As you continue your search, you can't shake the feeling that you're being watched.")
    time.sleep(4)
    print("After a long walk, you almost broke your ankle due to some unseen holes in the ground.")
    time.sleep(4)
    print("Nature had time to claim the outskirts of the hospital. You cannot continue any further.")

    while True:
        print("You have to chose wich entrance you wish to take.")
        time.sleep(2)
        print("1. Try to climb up the window that leads to the first floor")
        time.sleep(2)
        print("2. Investigate on the glowing window.")
        time.sleep("2")
        print("3. The main entrance might be a safer option.")
        time.sleep("2")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            climbing_through_the_window()
            break
        elif choice == "2":
            glowing_window()
            break
        elif choice == "3":
            going_through_main_entrance()
            break
        else:
            print("Invalid choice. Please enter a valid number.")


def climbing_through_the_window():
    print("You carefully stack the debris and manage to climb up to the window.")
    time.sleep(4)
    print("As you peer inside, you see what looks like a dark office stretching off into the distance.")
    time.sleep(4)
    print("You can see rotten chairs, empy files and papers scattered all over the floor. A fait smell of iron floats in the air.")
    time.sleep(4)
    print("You take a deep breath and climb through the broken window, entering the hospital through the side entrance.")
    time.sleep(4)
    in_the_administrative_offices()


def entering_the_toilets_from_window():
    print("You carefully enter the bathroom, keeping an eye out for any signs of danger.")
    time.sleep(4)
    print("You can see a door half open that leads to what seems to be a big room.")
    time.sleep(4)
    print("The sound of the wind whistles calmly through throughout the building.")
    time.sleep(4)
    print("your eyes start to get used to darkness and you gather up the courage to find out what is this glow.")
    time.sleep(6)
    print("As you get closer to the glowing object, you realize it's a small music box.")
    time.sleep(4)
    print("It's covered in strange symbols and glyphs, and it seems to be emanating a faint energy.")
    time.sleep(5)
    print("You notice a small worn latch that keeps the box shut.")
    time.sleep(4)

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


def entering_Hospital_lobby():

    print("You step inside the hospital lobby and are immediately hit by the smell of decay and mildew.")
    time.sleep(5)
    print("The air is thick with dust and the floorboards creak underfoot.")
    time.sleep(5)
    print("The only sound is the distant sound of water dripping, echoing off the empty walls.")
    time.sleep(5)
    print("To your right, you notice a door leading to the toilets.")
    time.sleep(4)
    print("The door is slightly ajar, and you catch a glimpse of something moving in the shadows inside.")
    time.sleep(6)
    print("You can't shake the feeling that you're being watched.")
    time.sleep(4)
    print("To your left, you see a long corridor leading to the main entrance.")
    time.sleep(4)
    print("The corridor is lined with old posters and faded photographs, showing smiling doctors and nurses from a bygone era.")
    time.sleep(6)
    print("The pictures are now faded and torn, adding to the eerie atmosphere of the place.")
    time.sleep(5)
    print("Straight ahead of you, you notice a staff-only door.")
    time.sleep(4)
    print("It's rusted shut, and you can see through the gap that the hallway beyond is completely dark.")
    time.sleep(6)
    print("Next to the staff door, you notice a set of stairs that lead to the first floor.")
    time.sleep(4)
    print("In the middle of the room, there is a large reception desk.")
    time.sleep(4)
    print("The wood is old and there are piles of dusty papers and broken equipment scattered about.")
    time.sleep(6)
    print("As you stand there, taking in your surroundings, you can't help but feel a sense of dread.")
    time.sleep(5)
    print("The hospital is old and abandoned, and it feels like something terrible is lurking just around the corner.")
    time.sleep(6)

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


def return_to_front_hospital_trough_main_entrance():
    print("You stand in front of the abandonned hospital.")
    time.sleep(3)
    print("The main entrance is a busted double door, hanging off its hinges, creaking eerily in the wind.")
    time.sleep(5)
    print("You can hear the faint rustle of leaves and the distant sound of creaking metal coming from inside the building.")
    time.sleep(5)

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
            print(
                "The doors groan as you push them open, revealing a dark and ominous interior.")
            time.sleep(3)
            going_through_main_entrance()
            break
        elif choice == "2":
            exploring_outside()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def entering_staff_only():
    pass


def stairs_first_floor():
    pass


def entering_the_toilets_from_door():
    print("You now stand still in the middle of the bathroom.")
    time.sleep(4)
    print("Some mold is growing on the walls and you can hear the faint sound of something crawling under the floor.")
    time.sleep(6)
    print("Your suddently realise that an object, hidden under one of the stalls is glowing slowly.")
    time.sleep(5)
    print("You decide to inspect the object.")
    time.sleep(3)
    print("As you get closer to the glowing object, you realize it's a small music box.")
    time.sleep(4)
    print("It's covered in strange symbols and glyphs, and it seems to be emanating a faint energy.")
    time.sleep(5)
    print("You notice a small worn latch that keeps the box shut.")
    time.sleep(4)

    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Open the box.")
        time.sleep(2)
        print("2. Leave the box alone and go through the door.")
        time.sleep(2)
        print("3. Leave the box alone and go outside from the window.")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            opening_the_music_box()
            break
        elif choice == "2":
            entering_Hospital_lobby()
            break
        elif choice == "3":
            print(
                "You decide to hop through the window as you feel that something is not right.")
            time.sleep(4)
            continue_exploring_outside()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def opening_the_music_box():
    print("You cautiously open the music box, revealing its contents.")
    time.sleep(4)
    print("Inside, you find a small, ancient-looking artifact.")
    time.sleep(3)
    print("As you pick it up, you feel a strange sensation coursing through your body.")
    time.sleep(4)
    print("Suddenly, you're overcome with a vision of a person screaming and begging.")
    time.sleep(5)
    print("The vision is so vivid and intense that you feel like you're actually there, experiencing the terror and pain of the person in the vision.")
    time.sleep(6)
    print("When the vision ends, you find yourself back in the abandoned hospital, clutching the music box tightly.")
    time.sleep(5)
    print("You're not sure what just happened, but you know that this artifact is important, and that it holds the key to uncovering the secrets of Hushan Hospital.")
    time.sleep(5)
    print("You carefully tuck the music box into your bag.")
# to finish


def going_through_main_entrance():
    pass


def in_the_administrative_offices():
    pass
