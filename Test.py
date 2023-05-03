import time

def typewritter(string):
    for char in string: 
        print(char, end="", flush=True)
        time.sleep(0.05)
        if char == "\n": 
            time.sleep(1)
    print("\n")

message_test = "Bla blablalaalajalj \n lmqskdjfqsldf \n fin"


typewritter(intro_scene) 



