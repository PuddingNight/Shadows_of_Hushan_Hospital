import time



    









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








def in_the_administrative_offices():
    pass
