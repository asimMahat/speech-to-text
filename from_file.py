import speech_recognition as sr 

# Initializing recognizer class
r = sr.Recognizer()

# Reading audiofile and storing in audio_text variable

with sr.AudioFile("audio_files/two.wav") as source :
    audio_input = r.listen(source)
    
# Using exception handling to know if speech recognition API works or not
    try :
        #using google speech recognition 
        text = r.recognize_google(audio_input)

        # For adding any other language 
        # in this case we are converting into french language
        # text = r.recognize_google(audio_text, language ='fr-FR')
        print("Converting audio into text")
        print(text)

        # Writing the result into the text file 
        with open("results/file-results.txt", "w") as f:
            f.write(text)

    except :
        print ('Sorry run again !!!')

