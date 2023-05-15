import time
import random

# Function that allows the text to be printed out one character at a time


def typewritter(string):
    for char in string:
        print(char, end="", flush=True)
        time.sleep(0.04)
        if char == "\n":
            time.sleep(0.08)
    print("\n")


# inventory that will hold the items the player will find
inventory = []

# function that cheks if the player has an item in their inventory


def check_inventory(item):
    if item in inventory:
        return True
    else:
        return False


# list that tracks the encounters the player had
encounters = []

# function that checks if the player has encountered a ghost


def check_encounters(ghost):
    if ghost in encounters:
        return True
    else:
        return False


# list that tracks the events the player has already experienced
events = []

# general function that checks if the player has experienced an event


def check_events(event):
    if event in events:
        return True
    else:
        return False


# list that tracks the rooms with long descriptions of rooms that the player has already visited
visited_rooms = []

# function that checks if the player has visited a room


def check_visited_rooms(room):
    if room in visited_rooms:
        return True
    else:
        return False


# make an object for the player
class Player:
    def __init__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory


# instantiating the player
player = Player("Luo Mei Ling", 100, inventory)


# class for the morgue killer
class Killer:
    def __init__(self, health, description):
        self.health = health
        self.description = description


# instantiating the morgue killer
creepy_cultist = Killer(100, "A creepy cultist")


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

entering_Hospital_lobby_text_new = """
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

entering_Hospital_lobby_text_old = """
Once again, you find yourself standing in the hospital lobby.\n
The air is thick with dust and the floorboards creak underfoot.\n
far away, the wind howls through the broken windows.\n
"""

return_to_front_hospital_trough_main_entrance_text = """
You stand in front of the abandonned hospital.\n
The main entrance is a busted double door, hanging off its hinges, creaking eerily in the wind.\n
You can hear the faint rustle of leaves and the distant sound of creaking metal coming from inside the building.")\n
"""

glowing_window_text_no_MB = """
You cautiously approach the window, peering inside the dimly lit room.\n
You can see a set of toilets, covered in dust and cobwebs.\n
As you're about to turn away, you notice something strange.\n
There's a faint glow coming from behind one of the stalls.\n
You can't quite make out what it is, but it's definitely something out of the ordinary.\n
"""

glowing_window_text_MB = """
You cautiously approach the window, peering inside the dimly lit room.\n
You can see a set of toilets, covered in dust and cobwebs.\n
Now that the glow of the music box is gone, you can feel a sense of dread.\n
"""

continue_exploring_outside_text = """
You continue exploring the exterior of the hospital, searching for another way inside.\n
As you make your way around the side of the building, you spot a small window on the first floor that looks like it's been broken.\n
You notice a small pile of debris nearby that looks like it could be used to climb up and reach the window.\n
"""

entering_the_toilets_from_window_text_no_MB = """
You carefully enter the bathroom, keeping an eye out for any signs of danger\n
You can see a door half open that leads to what seems to be a big room.\n
The sound of the wind whistles calmly through throughout the building.\n
Your eyes start to get used to darkness and you gather up the courage to find out what is this glow.\n
As you get closer to the glowing object, you realize it's a small music box.\n
It's covered in strange symbols and glyphs, and it seems to be emanating a faint energy."\n
You notice a small worn latch that keeps the box shut.\n
"""

entering_the_toilets_from_window_text_MB = """
You carefully enter the bathroom, keeping an eye out for any signs of danger\n
You can see a door half open that leads to what seems to be a big room.\n
The sound of the wind whistles calmly through throughout the building.\n
"""

opening_the_music_box_text = """
You cautiously open the music box, revealing its contents.\n
Inside, you find a small, ancient-looking artifact.\n
As you pick it up, you feel a strange sensation coursing through your body.\n
Suddenly, you're overcome with a vision of a person screaming and begging.\n
The vision is so vivid and intense that you feel like you're actually there, experiencing the terror and pain of the person in the vision.\n
When the vision ends, you find yourself back in the abandoned hospital, clutching the music box tightly.\n
You carefully tuck the music box into your bag.\n
Your mind is racing with questions, but you know that you need to find what happened in this hospital.\n
"""

standing_in_the_toilets_text = """
You stand in the toilets, trying to decide what to do next.\n
You can hear the faint sound of the forest nearby.\n
The music box inside you bag puts a little pressure against your back.\n
"""

entering_the_toilets_form_door_no_MB = """
You now stand still in the middle of the bathroom.\n
Some mold is growing on the walls and you can hear the faint sound of something crawling under the floor.\n
Your suddently realise that an object, hidden under one of the stalls is glowing slowly.\n
As you get closer to the glowing object, you realize it's a small music box.\n
It's covered in strange symbols and glyphs, and it seems to be emanating a faint energy.\n
You notice a small worn latch that keeps the box shut.\n
"""

entering_the_toilets_from_the_door_MB = """
You push the door carefully, and enter in what looks like the bathroom.\n
Some mold is growing on the walls and you can hear the faint sound of something crawling under the floor.\n
The missing glow of the music box makes this place even more sordid than before.\n
You feel very uncomfortable and you want to leave this place as soon as possible.\n
"""

return_to_the_main_entrance_text = """
You decide to keep searching for another way inside.\n
As you continue your search, you can't shake the feeling that you're being watched.\n
After a long walk, you almost broke your ankle due to some unseen holes in the ground.\n
Nature had time to claim the outskirts of the hospital. You cannot continue any further.\n
"""

climbing_through_the_window_in_text = """
You carefully stack the debris and manage to climb up to the window.\n
As you peek inside, you see what looks like a dark office stretching off into the distance.\n
You can see rotten chairs, empy files and papers scattered all over the floor.\n
You climb through the broken window, entering the hospital through the side entrance.\n
"""

entering_staff_only_text = """
You cautiously approach the staff-only door, your heart pounding in your chest.\n
The rusted metal creaks as you push it open, revealing a dark and foreboding hallway beyond.\n
You take a step forward, and the floorboards groan underfoot.\n
The hallway is musty and stale, with a faint smell of decay that makes your stomach turn.\n
The only sound is the distant drip of water and the faint buzz of white noise coming from somewhere deeper in the hospital.\n
\n
As you make your way down the hallway, you notice a sign pointing to the morgue.\n
The arrow seems to point down a flight of stairs that disappear into the darkness.\n
You can feel your heart racing in your chest as you consider the implications of the sign.\n
The thought of what might be waiting for you down there makes your skin crawl.\n
\n
But as you continue down the hallway, you notice another set of stairs leading even deeper into the bowels of the hospital.\n
The stairs are old and worn, with a railing that looks like it might give way at any moment.\n
You can hear strange noises coming from down below - the sound of shuffling footsteps and muffled whispers.\n
Your palms begin to sweat as you realize that you're not alone in this place, and that whatever is down there might not have your best interests in mind.\n
"""

going_down_the_morgue_new_text = """
You take a deep breath and steel yourself before descending down the stairs towards the morgue.\n
The stairs creak under your weight, and you can feel your heart pounding in your chest as you descend deeper into the bowels of the hospital.\n
The air grows colder and damper, and you can feel a chill running down your spine.\n
\n
As you reach the bottom of the stairs, you find yourself in a dimly lit hallway.\n
The walls are made of rough stone, and the floor is covered in a thick layer of dust.\n
The air is thick with the scent of decay, and you can see cobwebs clinging to the corners of the ceiling.\n
\n
The morgue is at the end of the hallway, and you can see the faint outline of a metal door in the dim light.\n
You can feel your hands shaking as you approach the door, and you take a deep breath before pushing it open.\n
\n
Inside, the room is cold and sterile.\n
The walls are lined with metal cabinets, each one containing a steel gurney with a sheet draped over it.\n
The room is eerily silent, except for the sound of your footsteps echoing off the metal walls.\n
\n
You make your way down the rows of cabinets, your eyes fixed on the gurneys.\n
You can feel a growing sense of unease in the pit of your stomach as you approach the last cabinet.\n
There, on the last gurney, something lies covered by a chunky white sheet.\n
\n
You pounder for a moment, trying to decide if you should pull the sheet to see what lies underneath.\n
\n
As you turn to notice anything else of interest.\n
You notice that in the corner of the room, lies a pile of dust next to a big machine.\n
You stare at it for a moment, trying to figure out what it is.\n
Then it hits you - it's a pile of ashes near the incinerator.\n
You can feel your heart pounding in your chest as you realize what this means.\n
\n
Getting closer, you can feel that the ashes are still warm.\n
You can see a faint glow coming from the incinerator, and you can hear the sound of something moving inside.\n
The incinerator is closed, but you can see a small latch on the side.\n
\n
You now stand still in the middle of the morgue.\n
"""


going_down_the_morgue_visited_text = """
You remember what happened the last time you went down there.\n
You can still feel the sense of dread when you heard the sound of shuffling footsteps and muffled whispers.\n
You reluctantly decide to go back down there.\n
the stairs creak under your weight, and you can feel your heart pounding in your chest as you descend deeper into the bowels of the hospital.\n
You walk down the hallway, and you can feel a chill running down your spine.\n
You now stand still in the middle of the morgue.\n
"""

pulling_the_sheet_text = """
You hesitate for a moment before pulling back the sheet, and what you see makes your blood run cold.\n
Lying there on the gurney is a body - or what used to be a body.\n
The flesh is gray and bloated, and you can see maggots wriggling in the open wounds.\n
\n
You stumble backwards, gagging on the smell.\n
You can feel your stomach churning, and you have to fight the urge to vomit.\n
You turn away from the body, trying to catch your breath.\n
\n
You then notice a small object in the hand of the corpse.\n
You take a step closer, terrified.\n
It appears to be a small journal, and you can see the words "Property of Dr. Zhao Ming" written on the cover.\n
"""


reading_the_journal_morgue_text = """
You decide to read the journal, hoping that it will provide some answers.\n
frightened, you reach for the journal that lies in the hand of the corpse.\n
You start to pull it out, the maggots are falling off the pages.\n
A strong smell of iron and rotten flesh fills the room.\n
You put yoursef together and start reading the journal.\n
an entry catches your attention :\n
\n
\n
Date: June 3, 1975\n
Location: Abandoned hospital in Hushan\n
\n
I arrived at the hospital today after hearing rumors of strange paranormal activity in the area.\n
As a renowned ghost specialist, I couldn't resist the opportunity to investigate these claims for myself.\n
The hospital is old and rundown, with a musty smell that lingers in the air. It's the perfect place for ghosts to hide.\n
\n
As I made my way through the abandoned halls, I couldn't shake the feeling that I was being watched.\n
I could hear faint whispers and footsteps in the distance, but every time I turned around, there was no one there.\n
\n
But my investigation took a chilling turn when I came across a ghostly apparition in one of the rooms.\n
The ghost was pale and trembling, and she told me a horrifying story of being tortured by the hospital staff before her death.\n
She begged me to help her, to make sure that no one ever suffered the same fate as she did.\n
\n
I promised her that I would do everything in my power to uncover the truth and put an end to the horrors that had taken place in this hospital.\n
But as I continued my investigation, I began to realize that there was more to this place than just ghosts.\n
\n
I could feel a presence watching me, following me as I made my way through the hospital.\n 
It was a cold and malevolent presence, unlike any ghost I had ever encountered before.\n
I began to suspect that there was something else in this hospital with me, something that wasn't bound by the laws of the afterlife.\n
\n
Now, as I look back on my time in this hospital, I realize that I was never alone.\n
There was always something else there, something lurking in the shadows.\n
I fear that it's free to prey on anyone who dares to enter this cursed place. I need to warn the villagers.\n
"""

killer_comes_morgue_text = """
You finish reading the journal, your mind is trying to comprehend what could have happened to this "ghost specialist".\n
Strangely, you feel that this poor soul is really similar to you.\n
how could he have died ?\n
The body on the gurney is still there, and you can see that the maggots are still crawling on it.\n
His body is too decomposed to see if he has any wounds.\n
You put the journal into your backpack.\n
Suddenly, you hear a noise from outside the morgue door.\n
\n
It's a sound like footsteps, heavy and deliberate.\n
You quickly realize that someone - or something - is coming down the hallway.\n
\n
Terrified, you realize that you have to take a quick decison.\n
You have two options: you can either hide or prepare to fight.\n
"""

hidding_morgue_text = """
You quickly scan the room for a hiding place. 
Your eyes land on a gurney in the corner of the room.\n
You hurry over and climb inside, pulling the sheet over your body.\n
Your heart is pounding in your chest as you try to steady your breathing, praying that whoever is coming won't find you.
"""

hidding_1_morgue_text = """
You hear the sound of heavy footsteps approaching, each one thudding against the ground like the footfall of a giant beast.\n
The footsteps are slow and deliberate, each one sending a shiver down your spine.\n
You can hear the sound of breathing, heavy and labored, like the breaths of some massive creature.\n
\n
You hold your breath, trying to make yourself as small and inconspicuous as possible.\n
The footsteps grow closer, until they're just a few feet away from your hiding spot.\n
You can hear the creature sniffing the air, trying to catch a whiff of your scent.\n
\n
You pull the sheet tighter around your body, hoping against hope that the creature won't find you.\n
You can feel your heart pounding in your chest, your breath coming in short gasps.\n
\n
Suddenly, the footsteps stop. 
You can hear the creature breathing heavily, as if it's just a few inches away from you.\n
You can feel its hot breath on your face, and you can't help but shudder.\n
\n
And then, just as suddenly as it appeared, the creature turns and walks away.\n
You can hear the sound of its footsteps receding, growing fainter and fainter until they're nothing but a distant echo.\n
\n
You let out a long, ragged breath, feeling the tension slowly leave your body.\n
But even as you lay there, hidden under the sheet, you can hear the sound of something climbing the stairs, leaving the morgue behind.\n
"""

hidding_2_morgue_text = """
You wait until you're absolutely sure that the coast is clear before slowly lifting the sheet off your body and sliding off the gurney.\n 
Your legs feel numb from being in the same position for so long, but you force yourself to move silently towards the door.\n
\n
You pause for a moment, listening carefully for any sign of whatever was here.\n
The only sound is your own breathing and the pounding of your heart in your chest.\n
You take a deep breath and push the door open, relieved to see that the hallway is empty.\n
"""

fighting_morgue_text = """
You start to look around the room for anything you can use as a weapon.\n
Your eyes land on a metal pipe lying on the ground. You pick it up, your hands shaking, and wait for whoever is coming to enter the room.\n
"""

fight_text_1 = """
As soon as the man comes through the door, you swing the pipe with all your might, hitting in the center of his head.\n
A cracking sound fills the room as his skull shatters under the force of the blow.\n
Blood splatters across the floor, he crumples to the ground, unmoving.\n
You take some time to catch your breath and lean against the wall, trying to calm your nerves.\n
You can't believe what just happened, you've never killed anyone before.\n
You close your eyes and try to steady your breathing, unable to stop your hands from shaking.\n
as you open your eyes, the body is gone.\n
"""
fight_text_2 = """
You swing the pipe at the man, but you miss, hitting him in the shoulder instead.\n
He recoils in pain, but quickly recovers and pulls out a knife.\n
In a moment of desperation, he stabs you, and you feel a searing pain in your side.\n
Your blood is pouring out of the wound, and you can feel yourself getting weaker by the second.\n
You collapse to the ground, and witness the man fading away into the darkness.\n
before you lose consciousness, you see the knife in your hand.\n
Was all of this just a dream ?\n
Did you stab yourself ?\n
A voice whispers in your ear:\n
You will now serve with the rest of us.\n
"""

fight_text_3 = """
You swing the pipe at the cultist, but your vision suddenly blurs, and you feel a sense of disorientation.\n
The cultist disappears, and you realize that you were just having an intense hallucination.\n 
Creepy voices whisper in your head, telling you of eldritch entities and dark rituals.\n
You stumble out of the morgue, shaken and confused.:\n
Are you going insane ?\n
You are convinced you need to bring peace to the spirits of this hospital.\n
"""

opening_the_incinerator_text = """
You cautiously approach the incinerator, the rusted metal creaking under your weight. The door is heavy and it takes all your strength to pull it open.\n
The stench of burning flesh hits you like a wave, and you can feel bile rising in your throat.\n
\n
Inside the incinerator, you see the charred remains of what used to be human bodies.\n
Some are nothing more than blackened bones, while others are still smoldering, the flesh melted and twisted beyond recognition.\n
\n
You notice a pile of glowing ashes in the corner of the incinerator.\n
As you approach the pile, you hear a faint whisper in your ear :
\n
"Your time will come soon enough, you will serve the Overseer forever like the rest of us."\n
\n
The ashes seem to glow brighter as you reach out to touch them, and you can feel a strange energy pulsing through your body.\n
You pull your hand back quickly, feeling like you've just made a deal with the devil.\n
\n
As you turn to leave the incinerator, you can't shake the feeling that something is watching you.\n
You glance back over your shoulder, but the incinerator is empty except for the pile of glowing ashes.\n
You are eager to put as much distance as possible between yourself and the horrors you've just witnessed.\n
Although, you feel like the ashes could be useful in the future.\n
"""

standing_in_the_morgue_text = """
You stand in the morgue, unsure of what to do next.\n
"""

getting_the_ashes_text = """
As you pick up the glowing ashes, a whispering voice echoes in your mind.\n
It speaks of ancient eldritch entities, dark rituals, and unspeakable power.\n
The voice promises you the world, but warns you of the price that must be paid.\n
It speaks of endless servitude and the loss of your very soul.\n
The words chill you to the bone, and you feel a sense of dread wash over you as you realize the true nature of the power you hold in your hand.\n
"""

returning_to_staff_only_text = """
You turn away from the morgue and start making your way back to the staff-only door.\n
As you walk you can hear the echo of your footsteps, and strangely enough, a faint piano melody.\n
You can't quite place the tune, but it sounds familiar.\n
When you finally arrive at the door, you stop and take a deep breath.\n
\n
You consider your options:\n 
You could open the door and go back to the lobby.\n
Or you could head back to the morgue.\n
Alternatively, you could descend down the dark stairs, risking whatever dangers lie in the depths of the hospital.\n
"""

going_up_lobby_stairs_text_new = """
You ascend the sairs with anticipation.\n
the stairs have a strange feeling to them, as if they are not quite solid.\n
When you reach the top of the stairs, you step onto a dimly lit hallway.\n
Holes in the upperfloor allow the light of the moon to cast eerie shadows along the walls.\n
\n
You notice signs hanging from the ceiling, indicating the different areas of the hospital.\n
To your left, the administrative offices are marked with a faded sign bearing the hospital's name.\n
To your right, the patients' rooms are labeled with numbers that seem to stretch on endlessly down the hallway.\n
\n
In front of you, another set of stairs leads further up into the unknown depths of the hospital.\n
\n
As you turn to look back down the stairs behind you, a shiver runs down your spine.\n
You fight the urge to flee back down the stairs to the relative safety of the ground floor.\n
But you know that you can't turn back now.\n
You've come too far to give up, and you need to keep moving forward.\n
You set your jaw and steel yourself for what lies ahead.\n
"""

going_up_lobby_stairs_text_old = """
Once again, you climb the stairs leading to the first floor.\n
Once you arrive in the hallway, the atmosphere feels different.\n
You notice that the signs above the doors have shifted, leading to rooms that you don't remember being there before.\n
Something feels off, something is playing tricks on your mind.\n
"""
standing_in_front_of_lobby_stairs_text = """
You stand in front of the stairs leading to the first floor.\n
You can hear the faint sound of a piano playing, coming from somehere under the hospital.\n
You notice signs hanging from the ceiling, indicating the different areas of the hospital.\n
\n
To your left, the administrative offices are marked with a faded sign bearing the hospital's name.\n
To your right, the patients' rooms are labeled with numbers that seem to stretch on endlessly down the hallway.\n
\n
In front of you, another set of stairs leads further up into the unknown depths of the hospital.\n
"""

going_down_lobby_stairs_text_new = """
You descend carefully down the stairs, wary of your every step.\n
On the walls, the wallpaper makes some strange patterns.\n
some of them look like faces, others like hands.\n
You shake your head, trying to clear your mind.\n
"""

going_down_lobby_stairs_text_old = """
You descend the stairs leading to the lobby.\n
The wallpaper seem to be different.\n
As if it was changed while you were not looking.\n
The colors are vivid.\n
"""

going_up_first_floor_stairs_text_new = """
You ascend the staircase to the second floor.\n
The climb seems shorter than the previous one.\n
\n
As you step off the stairs, you're faced with a hallway that stretches out before you.\n
Signs above the doors indicate the different rooms - to your left, the hospital psychiatric ward, straight ahead, the operating rooms and surgical ward, and to your right, the hospital laboratory.\n
\n
This place is awfully quiet.\n
For a short time, you sense a feeling of peace and tranquility.\n
"""

going_up_first_floor_stairs_text_old = """
You climb the stairs leading to the second floor.\n
You are relieved to find the peaceful atmosphere of the second floor.\n
"""

going_down_first_floor_stairs_text_new = """
As strange as it might sound, you feel like you are leaving a comforting place.\n
You descend the stairs leading to the first floor.\n
On your way down, for a short moment, you can hear your mother singing softly.\n
A strong smell of freshly baked cake fills the air, and vanishes, just like it camed.\n
You start to feel frightened.\n
What is this place doing to you ?\n
"""

going_down_first_floor_stairs_text_old = """
You descend the stairs leading to the first floor.\n
leaving the peaceful atmosphere of the second floor behind you.\n
"""

standing_first_floor_stairs_text = """
You stand in front of the stairs leading to the second floor.\n
You are relieved to find the peaceful atmosphere of the second floor.\n
"""

inside_administrative_offices_text_new = """
As you make your way into the administrative office, you can't help but notice the eerie stillness that fills the air.\n
The room is dimly lit, from some holes in the upper floor that let the light of the moon drip down in the office.\n
Some dust lightly flows in the air, and wood creaks under your feet.\n
The walls are lined with shelves, filled with dusty files and papers that haven't been touched in years.\n
\n
You notice a large wooden desk at the center of the room, with a flickering candle casting strange shadows on the walls.\n
Are you alone? Did someone come here?\n
As you approach the desk, you see a pile of documents stacked haphazardly on its surface.\n 
Each one has a strange, secret-looking stamp on it, as if they were not meant to be seen by anyone outside of the hospital.\n
\n
You begin to sift through the documents, your eyes scanning the pages for any useful information.\n
As you do, you come across a series of pictures showing patients before and after their stay in the hospital.\n
The "after" pictures are particularly disturbing, showing the patients weak and emaciated, with haunted eyes that seem to stare right through you.\n
\n
Suddenly, a glowing folder sitting in the corner of the desk catches your eye.\n
It seems to pulse with an otherworldly energy, beckoning you to inspect its contents.\n
You hesitate for a moment, feeling a strange sense of dread in the pit of your stomach.\n
Should you take a look inside?
\n
To your left, an open door lets a small breeze of cold air run throughout the office.\n
"""

inside_administrative_offices_text_old = """
You enter the administrative office.\n
Everything is quiet.\n
Nothing seems to have changed since your last visit.\n
"""

inside_administrative_offices_text_no_folder = """
You can't help but notice that the folder is still humming with an otherworldly energy.\n
"""
inside_administrative_offices_text_folder = """
The rooms semms to be darker than before now that the folder is gone.\n
"""


administrative_office_note = """
Your hands are shaking as you reach for the folder.\n
You open it slowly, and a strange light fills the room.\n
gust of wind blows through the door, and the candle on the desk flickers heavily.\n
\n
Inside the folder, you find a collection of strange and unsettling documents.\n
There are notes on dark rituals and eldritch entities, diagrams of strange symbols, and even a few photographs that defy explanation.\n
The more you read, the more you feel like you're getting a glimpse into a world that shouldn't exist.\n
You realize that you could spend hours poring over the contents of the folder, but something tells you that you shouldn't stay in this room for too long.\n
\n
As you were about to close the folder, you notice a folded note that was hidden between the pages.\n
It is handwritten, and the words are barely legible:\n
\n
"While finishing the ritual cleanup, I heard for the first time the sweet sound of the voice of the Overseer.\n
He led me to untold knowledge, and soon the truths unveiled themselves to me.\n
I swore to him that I would do everything in my power to bring him back to this world.\n
I did everything he asked of me, and he rewarded me with knowledge beyond my wildest dreams.\n
\n
Thirteen years have passed since then, and time has made my body weak.\n
I have grown old, and my health is failing.\n
I fear that i will not live long enough to finally grasp the knowledge that I seek.\n
Knowing and understanding the universe...\n
The old unseen gods that crawls in every corner of it...\n
The explanation of the unexplainable...\n
The rationality of madness.\n
\n
I need to find a way to extend my life, to continue my research...\n
Maybe a deal with the Overseer himself would be enough to grant me the knowledge that I need to buy me more time."\n
\n
You close the folder, and put it back where you found it.\n
You feel like you should leave this place as soon as possible.\n
But you can't help but wonder what the Overseer is, is that just some kind of elaborate hoax?\n
\n
You find yourself staring blankly at the folder, lost in thought.\n
you should get moving.\n
"""


journal_operating_room_text = """
As you open the journal, you realize that it belonged to one of the surgeons who worked in this ward.\n
The entries are filled with detailed descriptions of surgical procedures, some of which are so graphic and disturbing that you can barely bring yourself to read them.\n
\n
But as you continue to flip through the pages, you come across an entry that stands out.\n
\n
"As I continue my research into the possibility of immortality, I have made a remarkable discovery.\n
It seems that the human soul contains a life essence that, when properly extracted, can be transformed into a fluid that has the power to extend one's life.\n
\n
At first, I was skeptical of such a claim. But as I began experimenting with patients in the hospital, I discovered that there was indeed something to this theory.\n
By using a machine of my own design, I was able to extract the souls of patients who had recently passed away and transform them into a glowing fluid that I injected into my own body.\n
\n
The effects were immediate and astounding.\n
I felt rejuvenated, alive with a vitality that I had not experienced in years.\n
The fluid seemed to heal my body, repairing damage and restoring my youth.\n
\n
But I soon discovered a problem.\n
My body consumed the fluid at a faster rate than I was able to produce it.\n
I needed to find a way to extract more souls, to create a greater supply of the fluid.\n
\n
And that's when I had a terrible idea.\n
What if I were to extract the souls of living patients, rather than just the deceased?\n
It seemed like a logical step, a necessary evil in order to continue my research.\n
\n
I began experimenting with the living patients, using a modified version of the machine to extract their souls without killing them.\n
The process was painful for them, but it yielded a greater supply of the life-giving fluid.\n
The operation room became my laboratory, and the patients became my test subjects.\n
\n
As I sit here, writing this note, I am wracked with guilt and horror at what I have done.\n
But at the same time, I cannot deny the power and potential of this discovery.\n
I must continue my research, no matter the cost. And if that means experimenting on the severed heads of patients to find a way to produce more fluid, then so be it.\n
The quest for immortality is not for the faint of heart."\n
\n
You realize that this journal could be the key to uncovering the truth about what happened in this hospital, and you tuck it away in your bag, determined to continue your investigation.\n
"""


journal_laboratory_text = """
You carefully pick up the journal and open it.\n
Flipping through the pages of the journal, you discover that the author was a former doctor of the hospital who became increasingly obsessed with using the power of the occult to extend his life.\n
He describes in great detail the various rituals and experiments he conducted, and the horrific things he did in the name of science.\n
\n
As you read on, you come across a page with a strange symbol scrawled across it in blood-red ink. Beneath it, note reads,\n
\n
"Now is the time to begin my greatest experiment, the culmination of all my research.\n
I have gathered the necessary materials and prepared the rital chamber.\n
It took me weeks to dig this pit in the storage room, but I could conduct my darkest works without fear of interruption.\n
\n
I cannot stop shaking as I write this.\n
I will have to put the ashes of the tortured souls into the pentagram, and then put candles at each point of the star.\n
I'll yell the sentence that the overseer murmured into my mind.\n
I then will dig a hole in the middle of the pentagram, put the machine in it...\n
and...\n
Gods, I'm so nervous.\n
\n\n
...Inject enough of the fluid into my body...\n\n
to be able to cut my own head off...\n
I will then put my head in the machine.\n
It is the only way to be sure that I will be able to survive the ritual.\n

I told Xin my trusted assistant to cover up the hole with dirt.\n
This boy is loyal to me, and I know he will do what I ask of him.\n
I gave him a supply of corpses in the morgue to... "fulfill" his terrible needs...\n
I just hope that the disparition of so many young girls will not be noticed by the authorities.\n
It's amazing that stupidity is often linked to the most perverted of minds.\n
But I digress.\n
\n
I will finally have the time to seek the knowledge I crave.\n
I just need to prepare myself for this trial.\n
\n
Quick, the overseer is urging me to go down to the bowels of the hospital."\n
\n
\n
You slowly close the journal, and put it in your bag.\n
\n
You wonder where this ritual could have taken place.\n
What about those ingredients...?\n
Some ashes... Candles...A sentence...?\n
How does this makes sense...?\n
\n
You decide to put the journal in your bag.\n
"""


climbing_through_the_window_out_text = """
You climb through the window and find yourself on the edge of a small ledge that runs along the side of the building.\n
You look down and see that you are several piled up boxes.\n
You could probably jump down onto them without hurting yourself too badly.\n
You take a deep breath and leap off the ledge, landing on the boxes below.\n
You roll onto the ground and quickly get to your feet.\n
"""

patient_rooms_text_new = """
As you walk down the corridor, you notice that most of the doors are boarded up with wooden planks.\n
Strange messages are scrawled across the planks in what appears to be blood-red paint.\n
You can make out phrases like "TO HELL WITH THIS CURSED PLACE" "DEATH LIVES HERE," and "DO NOT TRUST THE VISIONS"\n
\n
But one door stands out from the rest.\n
It's slightly ajar, and you can hear a faint whispering coming from inside.\n
As you approach the door, the whispering grows louder, until it sounds like a woman's voice.\n
\n
You push the door open and step inside.\n
The room is pitch-black, and you can barely make out the shape of a figure in front of you.\n
As your eyes adjust to the darkness, you realize that it's the body of an old woman.\n
\n
Her face is twisted in agony, and she looks like she's been dead for a long time.\n
Her eyes glow with an otherworldly light, and her voice sounds like it's coming from all around you.\n
\n
"You!" she hisses. "You're not supposed to be here. This place is cursed."\n
\n
You try to back away, but the voices gets lounder and distorted, as if it's coming from inside your head.\n
You feel a sharp pain in your chest, and you fall to the ground, clutching your heart.\n
\n
"I've been trapped here for so long," she continues.\n
"Tortured and tormented by the doctors and nurses."\n
"Each of my figers were cut off, one by one."\n
"How can i play the piano now ?"\n
\n
"but i had a little tresure, a music box that i kept hidden from them."\n
"It was the only thing that kept me sane."\n
"But then they found it."\n
"They ripped my music box away from me, the one thing that brought me comfort in my final moments."\n
\n
She pauses, her voice shaking with rage.\n
\n
"I want it back," she says.\n
"I need to hear its music one last time before I can rest."\n
"Find it for me. There is a piano in the basement of this forsaken place."\n
"Play the music box on the piano, and I will be free."\n
\n
With that, the corpse starts to combust furiously, screaming in agony.\n
\n
You run out of the room, and slam the door shut behind you.\n
You hear the sound of the corpse burning, and then silence.\n
You stand there for a moment, trying to catch your breath.\n
You peer through the keyhole, and see that the room is now completely empty.\n
"""

patient_rooms_text_old = """
You walk down the corridor, passing by the several boarded up doors.\n
You can hear faint whispers coming from behind them, but you ignore them.\n
You reach the end of the corridor, and find yourself in the room where you encountered the pianist ghost.\n
it's totally empty.\n
the cold air makes you shiver.\n
"""


entering_the_psychiatric_ward_next_text = """
As you make your way down the hallway towards the psychiatric ward, you can feel the hairs on the back of your neck standing on end.\n
The air gets colder and colder as you approach the ward, and you can hear strange noises coming from inside.\n
\n
You reach the entrance to the ward, a small window in the door is allowing you to see inside.\n
It's a windowless room, the walls are covered in a cushioned material that decayed over time.\n
In some area, you can see scratches and scuff marks where patients have fought against the walls.\n
\n
You open the door and step inside.\n
The room gets even colder, and you can see your breath in the air.\n
The room is empty, except for a single chair in the middle of the room.\n
Then, you hear a repetitive noise coming from behind you.\n
\n
As you turn around to see what it might be, you see an old man, slamming his head against the wall tha was peeled off.\n
He is bleeding profusely, but he doesn't seem to care.\n
He just keeps slamming his head against the wall, over and over again.\n
\n
Then, he stops, and turns to look at you.\n
His eyes are completely white, and he has a huge grin on his face.\n
He starts to laugh, a deep, guttural laugh that sends chills down your spine.\n
\n
"Welcome to my humble abode !"\n
"I have a samll riddle for you, if you can solve it, i will teach you the sentece that this horrendous doctor used to accomplish his evil deeds."\n
He clears his throat, and begins to speak.\n
\n
"Here is the riddle :"\n
\n
"I am the dream of the ages, the hope of the hopeless, \n
A gift that many desire, but few can cope with. \n
I am a promise of life, beyond mortal bounds, \n
But what I offer is not what it sounds.\n
\n
For those who seek me, I offer a curse,\n
A life unending, with nothing but worse.\n
Eternity is my name, but so is the pain,\n
And those who dare to seek me, must be insane.\n
\n
For with me comes madness, and a hunger unquenched,\n
A thirst for life that can never be drenched.\n
I am the gift that none should ever receive,\n
For those who gain me, forever grieve."\n
\n
What am I ?"\n
"""

entering_the_psychiatric_ward_old_no_clue_text = """
You step back into the psychiatric ward, and find yourself in the same room as before.\n
The spirit is still there, looking deeply into your eyes.\n
\n
"Have you found the answer to my riddle ?"\n
\n
"Here is the riddle :\n
\n
"I am the dream of the ages, the hope of the hopeless,\n
A gift that many desire, but few can cope with.\n
I am a promise of life, beyond mortal bounds,\n
But what I offer is not what it sounds.\n
\n
For those who seek me, I offer a curse,\n
A life unending, with nothing but worse.\n
Eternity is my name, but so is the pain,\n
And those who dare to seek me, must be insane.\n
\n
For with me comes madness, and a hunger unquenched,\n
A thirst for life that can never be drenched.\n
I am the gift that none should ever receive,\n
For those who gain me, forever grieve."\n
\n
What am I ?"\n
"""

entering_the_psychiatric_ward_old_clue_text = """
You step back into the psychiatric ward, and find yourself in the same room as before.\n
The spirit is still there, looking deeply into your eyes.\n
\n
"Your fate is sealed, go accomplish your deed."\n
\n
A force pushes you out of the room, and you find yourself back in the corridor.\n
You step back to the stairs of the second floor.\n
"""

getting_out_of_the_psychiatric_ward_no_clue_text = """
You decide to leave the ghost alone, and head back to the stairs.\n
As soon as you leave the room you can hear the stomping sound of his head against the wall.\n
"""


answering_the_riddle_right_text = """
The ghost's eyes widen as you provide the correct answer to the riddle.\n
"Immortality," he whispers, his voice barely audible.\n
"Yes, that's it. You have proven yourself worthy to know the truth."\n
\n
The ghost then leans in closer, and his voice takes on a more urgent tone.\n
"Listen carefully, for what I'm about to tell you is of utmost importance.\n
The secret incantations you seek are hidden in the words of the ancients, in a language long forgotten by man.\n
But fear not, for I have heard these words before, spoken by the chief doctor himself, hidden away in the storage room."\n
\n
The ghost pauses, and his eyes seem to glaze over as if he's lost in thought.\n
"Repeat after me," he begins, reciting a series of strange syllables and guttural sounds.\n
"These are the words you'll need to invoke the ritual.\n
But beware, for the forces you're about to call upon are not to be trifled with.\n
The chief doctor paid a terrible price for his discovery, and his soul is now forever bound to the darkness of this hospital."\n
\n
The ghost falls silent, his words echoing in the stillness of the room.\n
It's up to you now to decide what to do with this knowledge, and whether you're willing to pay the price for immortality.\n
\n
After some time, you decide to leave the ghost alone, and head back to the stairs.\n
As soon as you leave the room you can hear the stomping sound of his head against the wall.\n
"""

entering_the_surgical_ward_new_text = """
As you step into the surgical ward, the pungent smell of disinfectant and blood fills your nostrils.\n
The floor is sticky with some kind of dark liquid that almost dried up.\n
You can see the outline of a surgical table in the center of the room.\n
Scatted all around the place are various surgical tools, some of which are bent and broken.\n
\n
As you walk further into the room, you begin to feel a sense of unease.\n
It feels as if someone forced on those tools, and used them for some kind of twisted purpose.\n
\n
As you approach one of the surgical tables, you have a sudden vision of a patient writhing in pain, their flesh being cut open by the surgeon's scalpel.\n
You can almost hear their screams echoing through the room.\n
\n
Shaken, you continue to explore the ward, searching for any clues or signs of what happened here.\n
Finally, you spot a small journal tucked away in one of the cabinets. Its cover is stained with blood, and it appears to have been hidden away for some time.\n
\n
Should you read it ? or carry on exploring ?\n
"""

enteting_the_surgical_ward_old_No_Journal_text = """
You step back into the surgical ward, and find yourself in the same room as before.\n
The smell of blood and disinfectant is still strong, and the floor is still sticky with some kind of dark liquid.\n
You can't help but wonder what does this journal contains.\n
\n
Should you read it ? or carry on exploring ?\n
"""

entering_the_surgical_ward_journal_text = """
You step back into the surgical ward, and find yourself in the same room as before.\n
The smell of blood and disinfectant is still strong, and the floor is still sticky with some kind of dark liquid.\n
What horrors could have happened on this operating table ?\n
\n
You rummage through the cabinets, in hopes of finding anything else that could help you.\n
But all you can find are some old surgical tools, and some rotten bandages.\n
You should probably leave this place, before you get sick.\n
\n
"""

entering_the_lab_new_text = """
Entering the laboratory, you're immediately struck by the overwhelming stench of formaldehyde and rot.\n
The shelves that line the walls are cluttered with countless jars, each filled with macabre specimens: organs, brains, limbs, even entire fetuses.\n
Some are labeled with scientific names, others with more sinister-sounding titles.\n
\n
The tables in the center of the room are covered in arcane symbols and a variety of mysterious tools and implements, some of which look like they've been repurposed from surgical equipment.\n
The air is thick with a strange energy, almost as if you're standing in the midst of some otherworldly ceremony.\n
\n
As you begin to explore the room, you notice a collection of books and papers scattered haphazardly about.\n
Some of them are written in ancient languages you can't even begin to decipher, while others are in modern tongues but seem to be discussing unspeakable things.\n
You find instructions for ritual sacrifices, drawings of strange creatures, and detailed descriptions of bizarre ceremonies.\n
\n
Your attention is drawn to a particularly worn-looking journal, hidden beneath a pile of dusty papers.\n
It emanates a gentle glow, as if it's calling out to you.\n
\n
A big pile of candles is sitting on the table, and you can see a lighter next to it.\n
"""

entering_the_lab_No_candles_No_journal_old_text = """
You get into the laboratory. after a quick look around, you only find the candles and the lighter.\n
Some of them have a thick layer of dust on them, but they should still work.\n
After searching around, your attention is drawn to the particularly worn-looking journal, hidden beneath a pile of dusty papers.\n
other than that, you cannot find anything interesting after searching the room.\n
"""

entering_the_lab_journal_no_candles_old_text = """
You get into the laboratory. after a quick look around, the only thing of interest seems to be the candles.\n
The candles are still sitting on the table, and you can see a lighter next to it.\n
\n
From the door, you can hear some strange noises of paper being shuffled around.\n
"""

entering_the_lab_no_journal_candles_old_text = """
You can feel the candles in your bag as you enter the laboratory.\n
After searching around, your attention is drawn to the particularly worn-looking journal, hidden beneath a pile of dusty papers.\n
Nothing else seems to be of interest in this room.\n
"""

entering_the_lab_candles_journal_old_text = """
You get into the laboratory. Here nothing has changed since the last time you were here.\n
You cannot find anything interesting, you've already picked up the candles and read the journal.\n
You should probably leave this place.\n
"""

stanging_in_the_lab_No_candles_No_Journal_text = """
You stand in the middle of the room, surrounded by the strange symbols and arcane tools.\n
The candles are still sitting on the table, and you can see a lighter next to it.\n
After searching around, your attention is drawn to the particularly worn-looking journal, hidden beneath a pile of dusty papers.\n

\n
From the door, you can hear some strange noises of paper being shuffled around.\n
"""

standing_in_the_lab_candles_no_journal_text = """
The candles in your bag start to feel heavy as you stand in the middle of the room, surrounded by the strange symbols and arcane tools.\n
The desk have a big mark on it, where the candles used to be.\n
After searching around, your attention is drawn to the particularly worn-looking journal, hidden beneath a pile of dusty papers.\n
"""

standing_in_the_lab_journal_no_candles_text = """
You still remember the disturbing contents of the journal as you stand in the middle of the room, surrounded by the strange symbols and arcane tools.\n
The candles are still sitting on the table, and you can see a lighter next to it.\n
After searching around, you cannot find anything else interesting.\n
"""

picking_up_the_candles_text = """
You reach out and pick up the candles, their cold wax sending a shiver down your spine.\n
As you hold them in your hand, you notice strange symbols etched into the wax, almost as if they're whispering to you.\n
A faint odor of decay emanates from the candles, filling the air with an unsettling presence.\n
You can't help but feel a sense of unease, but you know these candles may hold the key to your survival.\n
"""

going_down_storage_room_stairs_new_text = """
As you descend the stairs, a sense of foreboding envelops you.\n
Each step seems to echo with a weighty significance, and their sound resonates deep down the stairwell.\n
The dim light from above fades, leaving you in near darkness, with only a faint glow to guide your way.\n
\n
The darkness ahead is suffocating, and the air feels heavy with an unsettling presence.
You can't see far into the depths of the descent, but you can hear faint scurrying sounds running along the walls.\n
\n
The stairs creak beneath your weight, their age and weariness evident.\n
The musty scent of mold and wet earth hits your nostrils, mingling with the dampness that clings to the air.\n
Whispers, like ethereal whispers, brush against your ears, carrying hints of forgotten secrets.\n
\n
The descent feels never-ending, as if you are descending into the depths of the unknown.\n
Your hand brushes against the cool, rough texture of the worn handrail, offering a sliver of stability in this unsettling descent.\n
The sound of your own footsteps seems muffled, drowned out by a sense of anticipation that hangs heavy in the air.\n
\n
As you reach the bottom of the stairs, the dim light reveals a narrow corridor, lined with shelves upon shelves of dusty and forgotten items.\n
The atmosphere feels heavy with a silent history, as if each object holds a story waiting to be unraveled.\n
\n
Ahead, through the clutter and disarray, you catch a glimpse of something peculiar:\n
An old piano, partially covered in a sheet, stands as an enigmatic centerpiece in this forgotten storage room.\n
\n
It beckons to you, its presence both intriguing and unsettling.\n
\n
With each step, the tension grows, the anticipation mounting.\n
You stand at the threshold of this mysterious room, knowing that something awaits you within its shadowed depths.\n
Determination fuels your curiosity as you prepare to uncover the secrets that lie hidden within this forsaken storage room.\n
"""

going_down_storage_room_stairs_old_text = """
As you descend the familiar stairs once more, the air grows heavy with a damp chill.\n
The musty scent of mold and wet earth fills your nostrils, adding to the unsettling atmosphere.\n
Shadows envelop the narrow corridor, obscuring your surroundings in darkness.\n
\n
Among the clutter and disarray, your eyes are drawn to the old piano, partially covered by a worn sheet.\n
Its presence evokes both intrigue and a sense of unease.\n
It stands as a silent sentinel in this forsaken storage room, holding secrets yet to be revealed.\n
\n
You take a moment to steady yourself, knowing that within these shadowed depths lies the key to unraveling the mysteries that haunt this place.\n
With determination, you step forward, ready to confront what awaits you once more in this enigmatic realm.\n
"""

going_up_storage_room_stairs_text = """
You ascend the stairs, each step echoing in the silence of the dimly lit corridor.\n
As you reach the top, you find yourself standing before the staff-only door, its presence imposing and mysterious.\n
The air around you feels heavy, carrying a sense of foreboding that sends a shiver down your spine.\n
\n
You take a moment to steady yourself, wondering where you shoud head next.\n
"""

standing_storage_room_text = """
You now stand in the middle of the storage room, surrounded by shelves upon shelves of dusty and forgotten items.\n
In front of you, partially covered by a worn sheet, is an old piano.\n
"""

standing_storage_room_shelves_text = """
You now stand in the middle of the storage room, the contents of the shelves are scattered all over the floor.\n
In front of you, partially covered by a worn sheet, is an old piano.\n
"""

standing_storage_room_piano_text = """
You now stand in the middle of the storage room, surrounded by shelves upon shelves of dusty and forgotten items.\n
In front of you, the old piano sits silently, its presence both intriguing and unsettling.\n
The music box is still enchassed in the hole on the top of the piano.\n
\n
The pathway in the wall is faitly calling you.\n
"""

standing_storage_room_piano_shelves_text = """
You now stand in the middle of the storage room, the contents of the shelves are scattered all over the floor.\n
In front of you, the old piano sits silently, its presence both intriguing and unsettling.\n
The music box is still enchassed in the hole on the top of the piano.\n
\n
The pathway in the wall is faitly calling you.\n
"""

activating_the_piano_text = """
As you approach the old piano, your attention is fixated on the small hole on its top.\n
It is a seemingly insignificant feature, yet something deep within tells you there is more to it than meets the eye.\n
Instinctively, you reach into your pocket and retrieve the music box you found in the lobby room.\n
\n
Gently, you hold the music box up to the hole, and a sense of anticipation washes over you.\n
As if guided by an unseen force, the music box fits perfectly within the aperture.\n
It is a revelation, a realization that these two objects were meant to be united.\n
\n
With a trembling hand, you begin to turn the small metal handle of the music box.\n
As the familiar melody starts to play, the room seems to come alive with a soft, ethereal glow.\n
The notes resonate through the air, filling the storage room with an otherworldly harmony.\n
\n
As the melody reaches its crescendo, a magical transformation takes place.\n
The piano, once weathered and worn, now radiates with an inner light.\n
It shimmers and vibrates in harmony with the music, as if infused with a newfound vitality.\n
\n
In this surreal moment, you understand the significance of the music box and the piano.\n
They are conduits, linked by a shared history and purpose.\n
The ghost's words echo in your mind, confirming that this ritual was the key to freeing her spirit.\n
\n
A mixture of awe and trepidation fills your heart as you realize the magnitude of what you have uncovered.\n
\n
Suddenly, the music stops, and the piano falls silent.\n
The glow fades, and the piano returns to its former state, as if nothing had happened.\n
\n
You stand there, stunned by what you have witnessed.\n
And then, you hear a faint whisper, a voice calling out to you from the darkness.\n
\n
"Thank you..."\n
\n
The voice is soft and gentle, yet filled with a sense of longing.\n
It is the voice of that ghost, the one you met in the patient room.\n
\n
You turn around, searching for the source of the voice.\n
But there is nothing there, only the empty shelves and the old piano.\n
\n
Suddenly, some shelves begin to shake, as if moved by an unseen force.\n
You watch in awe as they slide apart, revealing a hidden passageway.\n
\n
"There... He went there..."\n
\n
"And then... Darkness..."\n
\n
The voice fades away, leaving you alone in the silence of the storage room.\n
You take a moment to collect your thoughts, wondering what to do next.\n
The passageway beckons to you, its dark depths filled with mystery and intrigue.\n
"""

inspecting_the_piano_text = """
As you approach the old piano, you notice a small hole on its top.\n
It is a seemingly insignificant feature, yet something deep within tells you there is more to it than meets the eye.\n
\n
You take a moment to examine the piano, running your fingers along its weathered surface.\n
It is an old instrument, worn by time and neglect.\n
Yet, there is something about it that draws you in, as if it holds a secret waiting to be revealed.\n
\n
You wonder what this piano could tell you, if only it could speak.\n
Lost in your thoughts, you stay there for a while, pondering the mysteries of this forsaken storage room.\n
\n
After a while, you decide to move on.\n
"""

inspecting_the_piano_ghost_text = """
As you approach the old piano, you notice a small hole on its top.\n
It is a seemingly insignificant feature, yet something deep within tells you there is more to it than meets the eye.\n
\n
You take a moment to examine the piano, running your fingers along its weathered surface.\n
It is an old instrument, worn by time and neglect.\n
Yet, there is something about it that draws you in, as if it holds a secret waiting to be revealed.\n
\n
You then remember the ghost's words, and wonder if this piano could be the key to freeing her spirit.\n
\n
You try to play a few notes, but the piano remains silent.\n
You look around, searching for a clue, but there is nothing here that could help you.\n
\n
After a while, you decide to move on.\n
"""

inspecting_the_piano_music_box_text = """
As you approach the old piano, you notice a small hole on its top.\n
It is a seemingly insignificant feature, yet something deep within tells you there is more to it than meets the eye.\n
\n
You take a moment to examine the piano, running your fingers along its weathered surface.\n
It is an old instrument, worn by time and neglect.\n
Yet, there is something about it that draws you in, as if it holds a secret waiting to be revealed.\n
\n
You then notice that the hole on the top of the piano is the perfect size for the music box you found in the lobby room.\n
\n
You take the music box out of you bag and hold it up to the hole.\n
It fits perfectly, as if it was meant to be.\n
\n
You wonder what will happen if you turn the handle of the music box.\n
Sadly, you can't seem to be able to turn the key, as if it was stuck.\n
\n
There must be more to this piano than meets the eye.\n
After a while, you decide to move on.\n
"""

inspecting_the_storage_room_shelves_text = """
The shelves are filled with various items, ranging from old books to dusty boxes.\n
You take a moment to examine them, wondering what secrets they might hold.\n
\n
Nothing seems out of the ordinary, and the records of the patients are nowhere to be found.\n
You wonder if they were moved to another location, or if they were destroyed.\n
\n
After a while of rummaging through useless junk, you decide to move on.\n
"""

going_through_secret_hole_text = """
With cautious determination, you crawl through the narrow hole in the concrete wall, guided by a mix of trepidation and curiosity.\n
The passage is cramped and claustrophobic, the dampness and coldness of the surroundings sending shivers down your spine.\n
\n
As you emerge on the other side, the sight that greets you fills your heart with dread.\n
The room before you is suffused with an eerie darkness, barely illuminated by faint moonlight filtering through small cracks in the decaying walls.\n
The air hangs heavy with a sense of foreboding, as if the very atmosphere holds a weight of malevolence.\n
\n
Your eyes adjust to the dimness, revealing the ghastly scene that lies within.\n
Dominating the room is a colossal pentagram etched onto the floor, its lines worn and faded with time.\n
Each corner of the pentagram is marked by weathered candles, long since extinguished, their waxy remnants twisted and deformed.\n
\n
The room exudes an oppressive silence, broken only by your own labored breathing.\n
A sense of unease settles upon you as you gaze upon a macabre sight—a pile of skeletal remains, jumbled and scattered haphazardly, as if the remnants of twisted rituals past.\n
These human bones bear witness to dark sacrifices, their presence a haunting reminder of the horrors that unfolded within these walls.\n
\n
You can't help but feel a profound sense of dread and an overwhelming urge to turn away from this place of forbidden rituals.\n
Yet, a nagging curiosity tugs at your being, urging you to explore further, to uncover the truth that lies hidden within the heart of this forbidden chamber.\n
\n
With hesitant steps, you venture deeper into the room, your senses heightened and every nerve on edge.\n
The eerie stillness is only broken by the sound of your own footsteps echoing through the chamber, as if disturbing the restless spirits that linger here.\n
\n
As you stand amidst the desecrated remains and the faded symbols of dark magic, a chilling realization washes over you.\n
You are now entwined in a web of ancient secrets and unspeakable acts.\n
The path ahead is uncertain, and the perils that lie in wait remain unknown.\n
But with every step you take, you inch closer to the heart of the mysteries that haunt Hushan Hospital, and the truth that may set both the living and the dead free.\n
"""

# Starting the program


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


def going_through_main_entrance():
    typewritter(going_through_main_entrance_text)
    time.sleep(1)
    entering_Hospital_lobby()


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


def glowing_window():
    if check_inventory("Music Box") == False:
        typewritter(glowing_window_text_no_MB)
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
    else:
        typewritter(glowing_window_text_MB)
        while True:
            print("What do you want to do?")
            time.sleep(2)
            print("1. Hop through the window.")
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


def entering_the_toilets_from_window():
    if check_inventory("Music Box") == False:
        typewritter(entering_the_toilets_from_window_text_no_MB)
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
                print(
                    "You decide to hop back outside, you feel that something is not right.")
                time.sleep(4)
                continue_exploring_outside()
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)
    else:
        typewritter(entering_the_toilets_from_window_text_MB)
        while True:
            print("What do you want to do?")
            time.sleep(2)
            print("1. Continue through the door.")
            time.sleep(2)
            print("2. Go back outside from the window.")
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                entering_Hospital_lobby()
            elif choice == "2":
                print(
                    "You decide to hop back outside, you feel that something is not right.")
                time.sleep(4)
                continue_exploring_outside()
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)

    typewritter(entering_the_toilets_from_window_text_no_MB)
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


def opening_the_music_box():
    typewritter(opening_the_music_box_text)
    inventory.append("Music Box")
    standing_in_the_toilets()
    time.sleep(1)


def entering_the_toilets_from_door():
    if check_inventory("Music Box") == False:
        typewritter(entering_the_toilets_form_door_no_MB)
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
                print(
                    "You decide to hop back outside, you feel that something is not right.")
                time.sleep(4)
                continue_exploring_outside()
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)
    else:
        typewritter(entering_the_toilets_from_the_door_MB)
        while True:
            print("What do you want to do?")
            time.sleep(2)
            print("1. Continue through the door.")
            time.sleep(2)
            print("2. Go back outside from the window.")
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                entering_Hospital_lobby()
                break
            elif choice == "2":
                print(
                    "You decide to hop back outside, you feel that something is not right.")
                time.sleep(4)
                continue_exploring_outside()
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)


def standing_in_the_toilets():
    typewritter(standing_in_the_toilets_text)
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Go through the door leading deeper to the hospital.")
        time.sleep(2)
        print("2. Go outside through the window.")
        time.sleep(2)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            entering_Hospital_lobby()
            break
        elif choice == "2":
            continue_exploring_outside()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


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
            climbing_through_the_window_in()
            break
        elif choice == "2":
            return_to_main_entrance()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def return_to_main_entrance():
    typewritter(return_to_the_main_entrance_text)
    time.sleep(1)
    while True:
        print("You have to chose wich entrance you wish to take.")
        time.sleep(2)
        print("1. Try to climb up the window that leads to the first floor")
        time.sleep(2)
        print("2. Investigate on the gound floor window.")
        time.sleep("2")
        print("3. The main entrance might be a safer option.")
        time.sleep("2")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You decide to go back to the window that leads to the first floor.")
            time.sleep(2)
            print(
                "You walk back to the place that had stacked debris and a broken window.")
            time.sleep(2)
            climbing_through_the_window_in()
            break
        elif choice == "2":
            print(
                "You decide to go back to the window that wasn't boarded like the others on the ground floor.")
            time.sleep(2)
            print("You walk carefully and manage recall the position of this window.")
            time.sleep(2)
            glowing_window()
            break
        elif choice == "3":
            print("You decide to go through the main entrance.")
            time.sleep(2)
            print("You walk back to the main entrance.")
            time.sleep(2)
            going_through_main_entrance()
            break
        else:
            print("Invalid choice. Please enter a valid number.")


def climbing_through_the_window_in():
    typewritter(climbing_through_the_window_in_text)
    time.sleep(1)
    in_the_administrative_offices()


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


def entering_Hospital_lobby():
    if check_visited_rooms("Hospital lobby") == False:
        typewritter(entering_Hospital_lobby_text_new)
        time.sleep(1)
        visited_rooms.append("Hospital lobby")
        time.sleep(1)
        hospital_lobby_choice()
    else:
        typewritter(entering_Hospital_lobby_text_old)
        time.sleep(1)
        hospital_lobby_choice()


def hospital_lobby_choice():
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
            entering_staff_only()
            break
        elif choice == "3":
            print(
                "You can feel the cold sweat on your forehead dripping down your black hair.")
            time.sleep(3)
            print("The stairs still are in a good condition.")
            time.sleep(2)
            print(
                "while you are climbing the stairs, you can feel a presence following your steps.")
            time.sleep(2)
            # adding the first floor function here !!!!!!!!
            break
        elif choice == "4":
            entering_the_toilets_from_door()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def entering_staff_only():
    typewritter(entering_staff_only_text)
    time.sleep(1)
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Go to the morgue.")
        time.sleep(2)
        print("2. Go down the other dark sairs.")
        time.sleep(2)
        print("3. Go back to the lobby.")
        time.sleep(2)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You decide to go to the morgue.")
            time.sleep(2)
            going_down_the_morgue()
            break
        elif choice == "2":
            print("You decide to go to the storage room.")
            time.sleep(2)
            going_to_the_storage_room()
            break
        elif choice == "3":
            print("You decide to go back to the lobby.")
            time.sleep(2)
            entering_Hospital_lobby()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def going_down_the_morgue():
    if check_visited_rooms("morgue") == False:
        typewritter(going_down_the_morgue_new_text)
        time.sleep(1)
        check_visited_rooms.append("morgue")
        while True:
            print("What do you want to do?")
            time.sleep(2)
            print("1. Investigate on the last gurney that is draped with a white sheet.")
            time.sleep(2)
            print("2. Open the door of the incinerator.")
            time.sleep(2)
            print("3. Go back to the staff only room.")
            time.sleep(2)
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                print("You decide to investigate on the last gurney.")
                time.sleep(2)
                events.append("investigated the body on the last gurney")
                investigating_the_last_gurney()
                time.sleep(2)
                break
            elif choice == "2":
                print("You decide to open the door of the incinerator.")
                time.sleep(2)
                opening_the_incinerator()
                time.sleep(2)
                break
            elif choice == "3":
                print("You decide to go back to the lobby.")
                time.sleep(2)
                returning_to_staff_only()
                time.sleep(2)
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)
    else:
        typewritter(going_down_the_morgue_visited_text)
        time.sleep(1)
        while True:
            if events("investigated the body on the last gurney") == False and check_inventory("Ashes") == False:
                print("What do you want to do?")
                time.sleep(2)
                print(
                    "1. Investigate on the last gurney that is draped with a white sheet.")
                time.sleep(2)
                print("2. Open the door of the incinerator.")
                time.sleep(2)
                print("3. Go back to the staff only room.")
                time.sleep(2)
                choice = input("Enter the number of your choice: ")

                if choice == "1":
                    print("You decide to investigate on the last gurney.")
                    time.sleep(2)
                    investigating_the_last_gurney()
                    break
                elif choice == "2":
                    print("You decide to open the door of the incinerator.")
                    time.sleep(2)
                    opening_the_incinerator()
                    break
                elif choice == "3":
                    print("You decide to go back to the lobby.")
                    time.sleep(2)
                    returning_to_staff_only()
                    time.sleep(2)
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
                    time.sleep(2)
            elif events("investigated the body on the last gurney") == True and check_inventory("Ashes") == False:
                print("What do you want to do?")
                time.sleep(2)
                print("1. Open the door of the incinerator.")
                time.sleep(2)
                print("2. Go back to the staff only room.")
                time.sleep(2)
                choice = input("Enter the number of your choice: ")
                if choice == "1":
                    print("You decide to open the door of the incinerator.")
                    time.sleep(2)
                    opening_the_incinerator()
                    time.sleep(2)
                    break
                elif choice == "2":
                    print("You decide to go back to the lobby.")
                    time.sleep(2)
                    returning_to_staff_only()
                    time.sleep(2)
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
                    time.sleep(2)
            elif events("investigated the body on the last gurney") == False and check_inventory("Ashes") == True:
                print("What do you want to do?")
                time.sleep(2)
                print(
                    "1. Investigate on the last gurney that is draped with a white sheet.")
                time.sleep(2)
                print("2. Go back to the staff only room.")
                time.sleep(2)
                choice = input("Enter the number of your choice: ")

                if choice == "1":
                    print("You decide to investigate on the last gurney.")
                    time.sleep(2)
                    investigating_the_last_gurney()
                    break
                elif choice == "2":
                    print("You decide to go back to the lobby.")
                    time.sleep(2)
                    returning_to_staff_only()
                    time.sleep(2)
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
                    time.sleep(2)
            elif events("investigated the body on the last gurney") == True and check_inventory("Ashes") == True:
                print("What do you want to do?")
                time.sleep(2)
                print("1. Go back to the staff only room.")
                time.sleep(2)
                choice = input("Enter the number of your choice: ")

                if choice == "1":
                    print("You decide to go back to the lobby.")
                    time.sleep(2)
                    returning_to_staff_only()
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
                    time.sleep(2)


def opening_the_incinerator():
    typewritter(opening_the_incinerator_text)
    time.sleep(1)
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Get the ashes.")
        time.sleep(2)
        print("2. Leave the incinerator and explore the rest of the morgue.")
        time.sleep(2)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You decide to get the ashes.")
            time.sleep(2)
            getting_the_ashes()
            break
        elif choice == "2":
            print(
                "You decide to leave the incinerator and explore the rest of the morgue.")
            time.sleep(2)
            standing_in_the_morgue()
            break


def getting_the_ashes():
    typewritter(getting_the_ashes_text)
    time.sleep(1)
    standing_in_the_morgue()


def standing_in_the_morgue():
    typewritter(standing_in_the_morgue_text)
    time.sleep(1)
    while True:
        if events("investigated the body on the last gurney") == False and check_inventory("Ashes") == False:
            print("What do you want to do?")
            time.sleep(2)
            print("1. Investigate on the last gurney that is draped with a white sheet.")
            time.sleep(2)
            print("2. Open the door of the incinerator.")
            time.sleep(2)
            print("3. Go back to the staff only room.")
            time.sleep(2)
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                print("You decide to investigate on the last gurney.")
                time.sleep(2)
                investigating_the_last_gurney()
                break
            elif choice == "2":
                print("You decide to open the door of the incinerator.")
                time.sleep(2)
                # add a function to open the door of the incinerator
                break
            elif choice == "3":
                print("You decide to go back to the lobby.")
                time.sleep(2)
                # add a return to the staff only room
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)
        elif events("investigated the body on the last gurney") == True and check_inventory("Ashes") == False:
            print("What do you want to do?")
            time.sleep(2)
            print("1. Open the door of the incinerator.")
            time.sleep(2)
            print("2. Go back to the staff only room.")
            time.sleep(2)
            choice = input("Enter the number of your choice: ")
            if choice == "1":
                print("You decide to open the door of the incinerator.")
                time.sleep(2)
                # add a function to open the door of the incinerator
                break
            elif choice == "2":
                print("You decide to go back to the lobby.")
                time.sleep(2)
                # add a return to the staff only room
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)
        elif events("investigated the body on the last gurney") == False and check_inventory("Ashes") == True:
            print("What do you want to do?")
            time.sleep(2)
            print("1. Investigate on the last gurney that is draped with a white sheet.")
            time.sleep(2)
            print("2. Go back to the staff only room.")
            time.sleep(2)
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                print("You decide to investigate on the last gurney.")
                time.sleep(2)
                # add a function to investigate on the last gurney
                break
            elif choice == "2":
                print("You decide to go back to the lobby.")
                time.sleep(2)
                # add a return to the staff only room
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)
        elif events("investigated the body on the last gurney") == True and check_inventory("Ashes") == True:
            print("What do you want to do?")
            time.sleep(2)
            print("1. Go back to the staff only room.")
            time.sleep(2)
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                print("You decide to go back to the lobby.")
                time.sleep(2)
                # add a return to the staff only room
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)


def investigating_the_last_gurney():
    typewritter(pulling_the_sheet_text)
    time.sleep(1)
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Try to grab the journal.")
        time.sleep(2)
        print("2. Go back to exploring the morgue.")
        time.sleep(2)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You decide to grab the journal.")
            time.sleep(2)
            grabbing_the_journal()
            break
        elif choice == "2":
            print("You decide to explore the morgue a bit more.")
            time.sleep(2)
            standing_in_the_morgue()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def grabbing_the_journal():
    typewritter(reading_the_journal_morgue_text)
    time.sleep(1)
    typewritter(killer_comes_morgue_text)
    time.sleep(1)
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Hide.")
        time.sleep(2)
        print("2. Fight")
        time.sleep(2)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You decide to hide.")
            time.sleep(2)
            hidding_morgue_text()
            break
        elif choice == "2":
            print("You decide to fight.")
            time.sleep(2)
            fight_morgue_killer()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def fight_morgue_killer():
    outcome = random.randint(1, 2, 3)
    if outcome == 1:
        typewritter(fight_text_1)
        time.sleep(2)
        standing_in_the_morgue()
    elif outcome == 2:
        typewritter(fight_text_2)
        print("You have died. Game over.")
        time.sleep(2)
        while True:
            play_again = input("Would you like to play again? (Y/N) ")
            if play_again.capitalize == "Y":
                print("Restarting game...")
                time.sleep(2)
                intro()
                break
            elif play_again.capitalize == "N":
                print("Thanks for playing!")
                time.sleep(2)
                exit()
                break
    elif outcome == 3:
        typewritter(fight_text_3)
        time.sleep(2)
        standing_in_the_morgue()


def hiding_from_the_morgue_killer():
    typewritter(hidding_morgue_text)
    time.sleep(1)
    typewritter(hidding_1_morgue_text)
    time.sleep(1)
    typewritter(hidding_2_morgue_text)
    time.sleep(1)
    standing_in_the_morgue()


def returning_to_staff_only():
    typewritter(returning_to_staff_only_text)
    time.sleep(1)
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Go to the lobby.")
        time.sleep(2)
        print("2. Go down the dark sairs.")
        time.sleep(2)
        print("3. Go to the morgue.")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You decide to go to the lobby.")
            time.sleep(2)
            entering_Hospital_lobby()
            break
        elif choice == "2":
            print("You decide to go down the dark sairs.")
            time.sleep(2)
            # add a return to the storage room
            break
        elif choice == "3":
            print("You decide to go to the morgue.")
            time.sleep(2)
            going_down_the_morgue()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def going_to_the_storage_room():
    if check_visited_rooms("storage_room") == False:
        typewritter(going_down_storage_room_stairs_new_text)
        time.sleep(1)
        visited_rooms.append("storage_room")
        standing_storage_room()
    else:
        typewritter(going_down_storage_room_stairs_old_text)
        time.sleep(1)
        standing_storage_room()


def standing_storage_room():
    if check_events("Piano Activated") == False and check_events("Storage Shelves") == False:
        typewritter(standing_storage_room_text)
        time.sleep(1)
        storage_room_decision1()
    elif check_events("Piano Activated") == False and check_events("Storage Shelves") == True:
        typewritter(standing_storage_room_shelves_text)
        time.sleep(1)
        storage_room_decision2()
    elif check_events("Piano Activated") == True and check_events("Storage Shelves") == False:
        typewritter(standing_storage_room_piano_text)
        time.sleep(1)
        storage_room_decision3()
    else:
        typewritter(standing_storage_room_piano_shelves_text)
        time.sleep(1)
        storage_room_decision4()


def storage_room_decision1():
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Inspect the piano.")
        time.sleep(2)
        print("2. Inspect the storage shelves.")
        time.sleep(2)
        print("3. Go back up the stairs.")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You decide to inspect the piano")
            time.sleep(2)
            inspect_the_piano()
            break
        elif choice == "2":
            print("You decide to inspect the storage shelves.")
            time.sleep(2)
            look_at_the_storage_shelves()
            break
        elif choice == "3":
            print("You decide to go back up the stairs.")
            time.sleep(2)
            returning_to_staff_only()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)

def inspect_the_piano():
    if check_inventory("Music Box") == False and check_visited_rooms("patient_rooms") == False:
        typewritter(inspecting_the_piano_text)
        time.sleep(1)
        standing_storage_room()
    elif check_inventory("Music Box") == False and check_visited_rooms("patient_rooms") == True:
        typewritter(inspecting_the_piano_ghost_text)
        time.sleep(1)
        standing_storage_room()
    elif check_inventory("Music Box") == True and check_visited_rooms("patient_rooms") == False:
        typewritter(inspecting_the_piano_music_box_text)
        time.sleep(1)
        standing_storage_room()
    else:
        typewritter(activating_the_piano_text)
        time.sleep(1)
        standing_storage_room()
#to do: add 
def look_at_the_storage_shelves():
    pass

def going_up_the_lobby_stairs():
    if check_visited_rooms("lobby_stairs_up") == False:
        typewritter(going_up_lobby_stairs_text_new)
        time.sleep(1)
        visited_rooms.append("lobby_stairs_up")
        lobby_stairs_decision()
    else:
        typewritter(going_up_lobby_stairs_text_old)
        time.sleep(1)
        lobby_stairs_decision()


def lobby_stairs_decision():
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Go to adinistrative offices.")
        time.sleep(2)
        print("2. Go to the patients rooms.")
        time.sleep(2)
        print("3. Go to the second floor.")
        time.sleep(2)
        print("4. Go down the stairs to the lobby.")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You decide to go to the administrative offices.")
            time.sleep(2)
            in_the_administrative_offices()
            break
        elif choice == "2":
            print("You decide to go to the patients rooms.")
            time.sleep(2)
            patient_rooms()
            break
        elif choice == "3":
            print("You decide to go to the second floor.")
            time.sleep(2)
            going_up_first_floor_stairs()
            break
        elif choice == "4":
            print("You decide to go down the stairs to the lobby.")
            time.sleep(2)
            going_down_lobby_stairs()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def standing_lobby_stairs():
    typewritter(standing_in_front_of_lobby_stairs_text)
    time.sleep(1)
    lobby_stairs_decision()


def going_down_lobby_stairs():
    if check_visited_rooms("lobby_stairs_down") == False:
        typewritter(going_down_lobby_stairs_text_new)
        time.sleep(1)
        visited_rooms.append("lobby_stairs_down")
        entering_Hospital_lobby()
    else:
        typewritter(going_down_lobby_stairs_text_old)
        time.sleep(1)
        entering_Hospital_lobby()


def going_up_first_floor_stairs():
    if check_visited_rooms("first_floor_stairs_up") == False:
        typewritter(going_up_first_floor_stairs_text_new)
        time.sleep(1)
        visited_rooms.append("first_floor_stairs_up")
        first_floor_stairs_decision()
    else:
        typewritter(going_up_first_floor_stairs_text_old)
        time.sleep(1)
        first_floor_stairs_decision()


def first_floor_stairs_decision():
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Go to the psychiatric ward.")
        time.sleep(2)
        print("2. Go to the surgical ward.")
        time.sleep(2)
        print("3. Go to the hospital laboratory.")
        time.sleep(2)
        print("4. Go down the stairs to the first floor.")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You decide to go to the psychiatric ward.")
            time.sleep(2)
            entering_the_psychiatric_ward()
            break
        elif choice == "2":
            print("You decide to go to the surgical ward.")
            time.sleep(2)
            entering_the_surgical_ward()
            break
        elif choice == "3":
            print("You decide to go to the laboratory.")
            time.sleep(2)
            entering_the_lab()
            break
        elif choice == "4":
            print("You decide to go down the stairs to the first floor.")
            time.sleep(2)
            entering_the_lab()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def going_down_first_floor_stairs():
    if check_visited_rooms("first_floor_stairs_down") == False:
        typewritter(going_down_first_floor_stairs_text_new)
        time.sleep(1)
        visited_rooms.append("first_floor_stairs_down")
        lobby_stairs_decision()
    else:
        typewritter(going_down_first_floor_stairs_text_old)
        time.sleep(1)
        lobby_stairs_decision()


def standing_first_floor_stairs():
    typewritter(standing_first_floor_stairs_text)
    time.sleep(1)
    first_floor_stairs_decision()


def in_the_administrative_offices():
    # If the player has not visited this room before, display the new text.
    if check_visited_rooms("administrative_offices") == False:
        typewritter(inside_administrative_offices_text_new)
        time.sleep(1)
        visited_rooms.append("administrative_offices")
        administrative_offices_decision()
    # If the player has visited this room before, display the old text.
    else:
        typewritter(inside_administrative_offices_text_old)
        time.sleep(1)
        administrative_offices_decision()


def administrative_offices_decision():
    if check_events("administrative_journal") == False:
        typewritter(inside_administrative_offices_text_no_folder)
        time.sleep(1)
        while True:
            print("What do you want to do?")
            time.sleep(2)
            print("1. Go through the window.")
            time.sleep(2)
            print("2. Go through the door.")
            time.sleep(2)
            print("3. Pick up the folder.")
            time.sleep(2)
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                print("You decide to go through the window.")
                time.sleep(2)
                climbing_through_the_window_out()
                break
            elif choice == "2":
                print("You decide to go through the door.")
                time.sleep(2)
                print("You go through the door and find yourself in a dark corridor.")
                time.sleep(2)
                print("walk quietly, unsure of what you might find.")
                time.sleep(2)
                print(
                    "You finally see a sort of carrefour, and you decide to investigate there.")
                time.sleep(2)
                standing_lobby_stairs()
                break
            elif choice == "3":
                print("You decide to pick up the folder.")
                time.sleep(2)
                picking_up_the_folder()
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)
    else:
        typewritter(inside_administrative_offices_text_folder)
        time.sleep(1)
        while True:
            print("What do you want to do?")
            time.sleep(2)
            print("1. Go through the window.")
            time.sleep(2)
            print("2. Go through the door.")
            time.sleep(2)
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                print("You decide to go through the window.")
                time.sleep(2)
                climbing_through_the_window_out()
                break
            elif choice == "2":
                print("You decide to go through the door.")
                time.sleep(2)
                print("You go through the door and find yourself in a dark corridor.")
                time.sleep(2)
                print("walk quietly, unsure of what you might find.")
                time.sleep(2)
                print(
                    "You finally see a sort of carrefour, and you decide to investigate there.")
                time.sleep(2)
                standing_lobby_stairs()
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)


def climbing_through_the_window_out():
    typewritter(climbing_through_the_window_out_text)
    time.sleep(1)
    return_to_main_entrance()


def picking_up_the_folder():
    typewritter(administrative_office_note)
    time.sleep(1)
    events.append("administrative_journal")
    administrative_offices_decision()


def patient_rooms():
    if check_visited_rooms("patient_rooms") == False:
        typewritter(patient_rooms_text_new)
        time.sleep(1)
        visited_rooms.append("patient_rooms")
        patient_rooms_decision()
    else:
        typewritter(patient_rooms_text_old)
        time.sleep(1)
        patient_rooms_decision()


def patient_rooms_decision():
    print("You decide that there is nothing more to do here, and you leave the room.")
    time.sleep(2)
    print("You walk back to the corridor.")
    standing_lobby_stairs()


def entering_the_psychiatric_ward():
    if check_visited_rooms("psychiatric_ward") == False:
        typewritter(entering_the_psychiatric_ward_next_text)
        time.sleep(1)
        visited_rooms.append("psychiatric_ward")
        psychiatric_ward_decision()
    else:
        if check_events("psychiatric_ward_clue") == False:
            typewritter(entering_the_psychiatric_ward_old_no_clue_text)
            time.sleep(1)
            psychiatric_ward_decision()
        else:
            typewritter(entering_the_psychiatric_ward_old_clue_text)
            time.sleep(1)
            psychiatric_ward_decision()


def psychiatric_ward_decision():
    while True:
        if check_events("psychiatric_ward_clue") == False:
            print("What do you want to do?")
            time.sleep(2)
            print("1. Answer the riddle.")
            time.sleep(2)
            print("2. Go back stairs.")
            time.sleep(2)
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                print("You decide to go answer the riddle.")
                time.sleep(2)
                answering_the_riddle()
                break
            elif choice == "2":
                print("You decide to go back to the stairs.")
                time.sleep(2)
                going_out_the_psychiatric_ward()
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)
        else:
            print("What do you want to do?")
            time.sleep(2)
            print("1. Go back stairs.")
            time.sleep(2)
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                print("You decide to go back to the stairs.")
                time.sleep(2)
                standing_first_floor_stairs_text()
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)


def going_out_the_psychiatric_ward():
    typewritter(getting_out_of_the_psychiatric_ward_no_clue_text)
    time.sleep(1)
    standing_first_floor_stairs_text()


def answering_the_riddle():
    while True:
        time.sleep(2)
        choice = input(
            "Enter in full letter your answer (if you wish to exit this prompt enter 1): ")

        if choice == "1":
            print(
                "You decide that you need more time to think about it, and you leave the room.")
            time.sleep(2)
            getting_out_of_the_psychiatric_ward_no_clue_text()
            break
        elif choice.lower == "immortality":
            print("The gost smiles at you and says: 'You are correct.")
            time.sleep(2)
            events.append("psychiatric_ward_clue")
            riddle_dialogue()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def riddle_dialogue():
    typewritter(answering_the_riddle_right_text)
    time.sleep(1)
    standing_first_floor_stairs_text()


def entering_the_surgical_ward():
    if check_visited_rooms("Surgical_ward") == False:
        typewritter(entering_the_surgical_ward_new_text)
        time.sleep(1)
        visited_rooms.append("Surgical_ward")
        surgical_ward_decision()
    else:
        if check_events("surgical_journal") == False:
            typewritter(enteting_the_surgical_ward_old_No_Journal_text)
            time.sleep(1)
            surgical_ward_decision()
        else:
            typewritter(entering_the_surgical_ward_journal_text)
            time.sleep(1)
            surgical_ward_decision()


def surgical_ward_decision():
    if check_events("surgical_journal") == False:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Pick up the journal.")
        time.sleep(2)
        print("2. Go back stairs.")
        time.sleep(2)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You decide to pick up the journal.")
            time.sleep(2)
            picking_up_the_journal()
        elif choice == "2":
            print("You decide to go back to the stairs.")
            time.sleep(2)
            standing_first_floor_stairs_text()
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)
    else:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Go back stairs.")
        time.sleep(2)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You decide to go back to the stairs.")
            time.sleep(2)
            standing_first_floor_stairs_text()
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


def entering_the_lab():
    if check_visited_rooms("lab") == False:
        typewritter(entering_the_lab_new_text)
        time.sleep(1)
        visited_rooms.append("lab")
        lab_decision_1()
    else:
        if check_inventory("lab_candles") == False and check_events("Lab_Journal") == False:
            typewritter(entering_the_lab_No_candles_No_journal_old_text)
            time.sleep(1)
            lab_decision_1()
        elif check_events("Lab_Journal") == False and check_inventory("lab_candles") == True:
            typewritter(entering_the_lab_no_journal_candles_old_text)
            time.sleep(1)
            lab_decision_2()
        elif check_events("Lab_Journal") == True and check_inventory("lab_candles") == False:
            typewritter(entering_the_lab_journal_no_candles_old_text)
            time.sleep(1)
            lab_decision_3()
        else:
            typewritter(entering_the_lab_candles_journal_old_text)
            time.sleep(1)
            lab_decision_4()


def lab_decision_1():
    print("What do you want to do?")
    time.sleep(2)
    print("1. Pick up the candles.")
    time.sleep(2)
    print("2. pick up the journal.")
    time.sleep(2)
    print("3. Go back stairs.")
    time.sleep(2)
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("You decide to pick up the candles.")
        time.sleep(2)
        picking_up_the_candles()
    elif choice == "2":
        print("You decide to pick up the journal.")
        time.sleep(2)
        picking_up_the_journal()
    elif choice == "3":
        print("You decide to go back to the stairs.")
        time.sleep(2)
        standing_first_floor_stairs_text()
    else:
        print("Invalid choice. Please enter a valid number.")
        time.sleep(2)


def lab_decision_2():
    print("What do you want to do?")
    time.sleep(2)
    print("1. Pick up the journal.")
    time.sleep(2)
    print("2. Go back stairs.")
    time.sleep(2)
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("You decide to pick up the journal.")
        time.sleep(2)
        picking_up_the_journal()
    elif choice == "2":
        print("You decide to go back to the stairs.")
        time.sleep(2)
        standing_first_floor_stairs_text()
    else:
        print("Invalid choice. Please enter a valid number.")
        time.sleep(2)


def lab_decision_3():
    print("What do you want to do?")
    time.sleep(2)
    print("1. Pick up the candles.")
    time.sleep(2)
    print("2. Go back stairs.")
    time.sleep(2)
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("You decide to pick up the candles.")
        time.sleep(2)
        picking_up_the_candles()
    elif choice == "2":
        print("You decide to go back to the stairs.")
        time.sleep(2)
        standing_first_floor_stairs_text()
    else:
        print("Invalid choice. Please enter a valid number.")
        time.sleep(2)


def lab_decision_4():
    print("What do you want to do?")
    time.sleep(2)
    print("1. Go back stairs.")
    time.sleep(2)
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("You decide to go back to the stairs.")
        time.sleep(2)
        standing_first_floor_stairs_text()
    else:
        print("Invalid choice. Please enter a valid number.")
        time.sleep(2)


def picking_up_the_candles():
    typewritter(picking_up_the_candles_text)
    time.sleep(1)
    inventory.append("lab_candles")
    if check_events("lab_journal") == False:
        lab_decision_2()
    else:
        lab_decision_4()


def picking_up_the_journal():
    typewritter(journal_laboratory_text)
    time.sleep(1)
    events.append("Lab_Journal")
    if check_inventory("lab_candles") == False:
        lab_decision_3()
    else:
        lab_decision_4()

    # dummy intro launch that needs to be moved.
intro()
