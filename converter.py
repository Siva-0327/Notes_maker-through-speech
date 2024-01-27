import speech_recognition as s
import pyttsx3 

# First import speech recognition in your Terminal (------>pip insatll speechrecognition)
# And install pyAudio because record the audio what sysytem recognised the speech through microphone
# ------->pip install pyAudio 

word = s.Recognizer() # It will recognise what user will say

def speech():

    with s.Microphone() as source: # Through microphone we can access

        print("Listening....")

        audio = word.listen(source)    # which records audio until it detects a pause in the speech.
                                       # The recorded audio is then stored in a variable, in this case audio
    return audio
def speech_to_text(audio):   # Snake naming convention


    try:
        text = word.recognize_google(audio)
        print(text)
        engine = pyttsx3.init()   # intilize the text to read 
        voices = engine.getProperty('voices')  # getting different type of volumes
        engine.setProperty('voice', voices[1].id) # Selecting the Female voice
        engine.setProperty('rate', 160)    # Audio Speed
        engine.setProperty('volume', 100)   # Volume
        engine.say(text)
        engine.runAndWait()                # To run the speech
        return text

    except s.UnknownValueError:
        print("sorry i can't understand")
    except:
        print("something error was occured")
    return none

def save_to_file(text, filename):
    try:
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Text saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {str(e)}")

if __name__ == "__main__":
    audio = speech()
    text = speech_to_text(audio)
    if text:
        save_to_file(text, 'saved.txt')
