import time
import random

def typewritter(string):
    for char in string: 
        print(char, end="", flush=True)
        time.sleep(0.04)
        if char == "\n": 
            time.sleep(0.08)
    print("\n")



#Make an inventory that will hold the items the player will find
inventory = []

#make a general function that cheks if the player has an item in their inventory
def check_inventory(item):
    if item in inventory:
        return True
    else:
        return False


#make a list that tracks the encounters the player had
encounters = []

#make a general function that checks if the player has encountered a ghost
def check_encounters(ghost):
    if ghost in encounters:
        return True
    else:
        return False

#make a list that tracks the events the player has already experienced
events = []

#make a general function that checks if the player has experienced an event
def check_events(event):
    if event in events:
        return True
    else:
        return False


#make a list that tracks the rooms with long descriptions of rooms that the player has already visited
visited_rooms = []

#make a general function that checks if the player has visited a room
def check_visited_rooms(room):
    if room in visited_rooms:
        return True
    else:
        return False



#make an object for the player
class Player:
    def __init__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory


#instantiating the player
player = Player("Luo Mei Ling", 100, inventory)

#make a class for the ghosts they do not have health but they have a name and a description
class Ghost:
    def __init__(self, name, description):
        self.name = name
        self.description = description


#making a class for the morgue killer
class Killer:
    def __init__(self, health, description):
        self.health = health
        self.description = description

#instantiating the morgue killer
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

continue_exploring_outside_text ="""
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

climbing_through_the_window_text = """
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
You enter the administrative office.\n
Everything is quiet.\n
Nothing seems to have changed since your last visit.\n
Though, you can't help but notice that the folder you found last time is still humming with an otherworldly energy.\n
"""
inside_administrative_offices_text_folder = """
You enter the administrative office.\n
Everything is quiet.\n
Nothing seems to have changed since your last visit.\n
The rooms semms to be darker than before now that the folder is gone.\n
"""


administrative_office_note = """

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

#Coming from glowing_window() leads to :
# opening_the_music_box()
# entering_Hospital_lobby()
# continue_exploring_outside()
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
                print("You decide to hop back outside, you feel that something is not right.")
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
            print("You decide to hop back outside, you feel that something is not right.")
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

#coming from entering_the_toilets_from_the_window() or entering_toilets_from_door() Leads to :
# standing_in_the_toilets()
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
                print("You decide to hop back outside, you feel that something is not right.")
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
                print("You decide to hop back outside, you feel that something is not right.")
                time.sleep(4)
                continue_exploring_outside()
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)



#coming from opening_the_music_box() leads to :
# entering_Hospital_lobby()
# continue_exploring_outside()
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
                                                 



#coming from exploring_outside() or glowing_window() Leads to :
# climbing_through_the_window()
# return_to_main_entrance() 
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

#coming from continue_exploring_outside() Leads to :
# climbing_through_the_window()
# glowing_window()
# going_through_main_entrance()
def return_to_main_entrance():
    typewritter(return_to_the_main_entrance_text)
    time.sleep(1)
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
            print("You decide to go back to the window that leads to the first floor.")
            time.sleep(2)
            print("You walk back to the place that had stacked debris and a broken window.")
            time.sleep(2)
            climbing_through_the_window()
            break
        elif choice == "2":
            print("You decide to go back to the window that wasn't boarded like the others on the ground floor.")
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


#²coming from return_to_main_entrance() and climbing_through_the_window() Leads to :
# in_the_administrative_offices() !!!!!!!!!!!!!!!! Need to add it !!!!!!!!!!!!
def climbing_through_the_window():
    typewritter(climbing_through_the_window_text)
    time.sleep(1)
    in_the_administrative_offices()


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




#Coming form going_through_main_entrance() leads to :
# return_to_front_hospital_trough_main_entrance()
# entering_staff_only()
# sairs_first_floor() !!!!!!!!!!!!!!!! Need to add it !!!!!!!!!!!!
# Entering_the_toilets_from_door() 
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
#don't forget to add first floor stairs !!!!!!!!!
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
            print("You can feel the cold sweat on your forehead dripping down your black hair.")
            time.sleep(3)
            print("The stairs still are in a good condition.")
            time.sleep(2)
            print("while you are climbing the stairs, you can feel a presence following your steps.")
            time.sleep(2)
            #adding the first floor function here !!!!!!!!
            break
        elif choice == "4":
            entering_the_toilets_from_door()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)


#Coming from entering_Hospital_lobby() leads to :
# going down the morgue
# going to the storage room !!!!!!!!!!!!!!!! Need to add it !!!!!!!!!!!!
# going to entering_Hospital_lobby()
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

#Coming from entering_staff_only() leads to :
# open the incinerator 
# investigate on the last gurney 
# reurn to returning_to_staff_only() 
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
                print("1. Investigate on the last gurney that is draped with a white sheet.")
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

#coming from the morgue, leads to:
# getting the ashes
#standing in the morgue
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
            print("You decide to leave the incinerator and explore the rest of the morgue.")
            time.sleep(2)
            standing_in_the_morgue()
            break

#coming from the opening the incinerator, leads to:
# standing in the morgue
def getting_the_ashes():
    typewritter(getting_the_ashes_text)
    time.sleep(1)
    standing_in_the_morgue()



#coming from the opening the incenerator, getting ashes, the investigation of the last gurney, leads to:
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
                #add a function to open the door of the incinerator
                break
            elif choice == "3":
                print("You decide to go back to the lobby.")
                time.sleep(2)
                #add a return to the staff only room
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
                #add a function to open the door of the incinerator
                break
            elif choice == "2":
                print("You decide to go back to the lobby.")
                time.sleep(2)
                #add a return to the staff only room
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
                #add a function to investigate on the last gurney
                break
            elif choice == "2":
                print("You decide to go back to the lobby.")
                time.sleep(2)
                #add a return to the staff only room
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
                #add a return to the staff only room
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                time.sleep(2)


#coming from the standing in the morgue, leads to:
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

#coming from investigating the last gurney, leads to:
# hiding from the morgue killer
# fighting the morgue killer
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

#coming from grabbing_the_journal()
#leads to standing_in_the_morgue()
#leads to intro() if you die and choose to play again
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


#coming from grabbing the journal leads to :
# standing in the morgue
def hiding_from_the_morgue_killer():
    typewritter(hidding_morgue_text)
    time.sleep(1)
    typewritter(hidding_1_morgue_text)
    time.sleep(1)
    typewritter(hidding_2_morgue_text)
    time.sleep(1)
    standing_in_the_morgue()


#Need to add the storage room !!!!!!!!!!!!!!!!!!!!!!!!
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
            #add a return to the storage room
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

# coming from the lobby stairs, leads to:
# administrative offices !!!!!!!!!!!!!!!!!!!
# patients rooms !!!!!!!!!!!!!!!!!!!!!!!!!!!
# second floor
# lobby
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
            administrative_offices()
            break
        elif choice == "2":
            print("You decide to go to the patients rooms.")
            time.sleep(2)
            patients_rooms()
            break
        elif choice == "3":
            print("You decide to go to the second floor.")
            time.sleep(2)
            second_floor()
            break
        elif choice == "4":
            print("You decide to go down the stairs to the lobby.")
            time.sleep(2)
            going_down_lobby_stairs()
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            time.sleep(2)

#coming lobby_stairs_decision() leads to:
# entering_Hospital_lobby()
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

# coming from first_floor_stairs_decision() leads to:
# psychiatric ward !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# surgical ward !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# hospital laboratory !!!!!!!!!!!!!!!!!!!!!!!!!!
# going down the stairs to the first floor
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
            administrative_offices()
            break
        elif choice == "2":
            print("You decide to go to the surgical ward.")
            time.sleep(2)
            patients_rooms()
            break
        elif choice == "3":
            print("You decide to go to the laboratory.")
            time.sleep(2)
            second_floor()
            break
        elif choice == "4":
            print("You decide to go down the stairs to the first floor.")
            time.sleep(2)
            going_down_first_floor_stairs()
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





#dummy intro launch that needs to be moved.
intro()