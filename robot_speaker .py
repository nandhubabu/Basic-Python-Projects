import pyttsx3 #os not working on windows

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.2. Created by Nandhu")
    while(True):
        x = input("Enter what you want me to speak: ")
        if x=="q":
            engine.say("Good Bye")
            engine.runAndWait()
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
