import time


  

#working on it
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




def in_the_administrative_offices():
    pass
