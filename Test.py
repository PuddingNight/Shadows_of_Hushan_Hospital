import time

def typewritter(string):
    for char in string: 
        print(char, end="", flush=True)
        time.sleep(0.05)
        if char == "\n": 
            time.sleep(1)
    print("\n")

typewritter(intro_scene) 



