import win32com.client as wincom

print("This is robo speaker 2.0 which is created by kartik")

speak = wincom.Dispatch("SAPI.spVoice")  #This function is part of the win32com.client library,
#which allows Python to interact with COM (Component Object Model).
# This function allow to speak the text to integrate with wincom library .

while True: # for infinite loop 
    text = input("Enter what you want me to speak : ")
    if text.lower() == "bye": # "Bye", "bye", and "BYE" will all become "bye" when .lower()
        break
    speak.Speak(text) # this function use to speak the text string 
    