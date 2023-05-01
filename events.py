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
        user_input = input("When you're ready to continue, enter \"Continue\": ")
        if user_input.lower() == "continue":
            print("Your journey beggins !")
            time.sleep(2)
            arriving_hospital()
            break
        else:
            print("Invalid input, please check you entered \"Continue\"")



def arriving_hospital():
    print("You arrive at the hospital and look up at the towering, foreboding structure before you.")
    time.sleep(4)
    print("The main entrance is a busted double door, hanging off its hinges, creaking eerily in the wind.")
    time.sleep(5)
    print("The windows on the upper floors are all shattered, and the ivy that once covered the building has grown wild and unchecked.")
    time.sleep(6)
    print("You can hear the faint rustle of leaves and the distant sound of creaking metal coming from inside the building.")
    time.sleep(5)
    
    while True:
        directions = ["Main Entrance", "Explore the Exterior"]
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
            break
        elif choice == "2":
            print("You decide to explore the exterior of the hospital first, hoping to find another way in.")
            time.sleep(4)
            print("You walk around the building, taking in the overgrown courtyard and the twisted, rusted metal of what used to be a playground.")
            time.sleep(6)
            print("As you round the corner, you catch a glimpse of something moving in the shadows.")
            time.sleep(3)
            print("Your heart races as you try to determine if it's just your imagination playing tricks on you, or if there's something else out there with you.")
            time.sleep(8)
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)