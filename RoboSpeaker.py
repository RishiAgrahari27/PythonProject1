import pyttsx3 

if __name__ == '__main__':
    print("Welcome to robo Speaker 2.0 Designed by Rishi")
    engine = pyttsx3.init()
while True:
    x = input("Enter what you want to spake:")
    if x == "q|quit|back":
        break
    engine.say(x)
    engine.runAndWait()
