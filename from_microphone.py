import speech_recognition as sr

# Initializing recognizer class
r = sr.Recognizer()

with sr.Microphone() as source :
    print("Start talking")
    audio_input = r.listen(source)
    print("Stop")

    
# Using exception handling to know if speech recognition API works or not
    try :
        #using google speech recognition 
        text = r.recognize_google(audio_input)

        # For adding any other language ,in this case we are converting into french language
        # text = r.recognize_google(audio_text, language ='fr-FR')

        print("Converting audio into text")
        print(text)

    except :
        print ('Sorry run again !!!')


with open("microphone-results.raw", "wb") as f:
    f.write(audio_input.get_raw_data())

'''

# write audio to a RAW file
with open("microphone-results.raw", "wb") as f:
    f.write(audio.get_raw_data())

# write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

# write audio to an AIFF file
with open("microphone-results.aiff", "wb") as f:
    f.write(audio.get_aiff_data())

# write audio to a FLAC file
with open("microphone-results.flac", "wb") as f:
    f.write(audio.get_flac_data())

'''