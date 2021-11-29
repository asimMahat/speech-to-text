import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source :
    print("You have 10 seconds to speak")
    r.adjust_for_ambient_noise(source) #adjusting for background noise
    audio_input = r.listen(source,phrase_time_limit=10)
    # print(type(audio_input))
    # audio_input=r.record(source)
    print("Stop")

    try:

        text = r.recognize_google(audio_input)
        print("Converting audio into text")
        # print(type(text))
        print(text)

        # Writing the result into the text file 
        with open("microphone-results.txt", "w") as f:

            f.write(text)
        
    except:
        print ('Sorry run again !!!')
    
