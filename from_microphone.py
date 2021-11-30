# Importing speech recognition library
import speech_recognition as sr

# Initializing recognizer class
r = sr.Recognizer()

with sr.Microphone() as source :

    user_input = int(input("Choose your preferred language \n 1. English  \n 2. Nepali \n "))
    # print (type(user_input))

    # This is for English language
    if user_input == 1:
        print("You have 10 seconds to speak")
        r.adjust_for_ambient_noise(source) #adjusting for background noise
        audio_input = r.listen(source,phrase_time_limit=10)
        # print(type(audio_input))
        # audio_input=r.record(source)
        print("Stop")

    
        # Using exception handling to know if speech recognition API works or not
        try :
            #using google speech recognition 
            text = r.recognize_google(audio_input)
            print("Converting audio into text")
            # print(type(text))
            print(text)

            # Writing the result into the text file 
            with open("microphone-results.txt", "w") as f:
                f.write(text)

        except :
            print ('Sorry run again !!!')
    

    # This is for Nepali language
    elif user_input == 2:
        print("You have 10 seconds to speak")
        r.adjust_for_ambient_noise(source) #adjusting for background noise
        audio_input = r.listen(source,phrase_time_limit=10)
        # print(type(audio_input))
        # audio_input=r.record(source)
        print("Stop")

    
        # Using exception handling to know if speech recognition API works or not
        try :
            # using google speech recognition      
            # In this case we are doing for nepali language
            text = r.recognize_google(audio_input, language ='ne-NP')
            print("Converting audio into text")
            # print(type(text))
            print(text)

            # Writing the result into the text file 
            with open("results/microphone-results.txt", "w") as f:
                f.write(text)

        except :
            print ('Sorry run again !!!')
    
    else :
        print("Only choose between '1' or '2' ")
    

