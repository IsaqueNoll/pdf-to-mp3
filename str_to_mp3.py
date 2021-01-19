# imports
import pyttsx3



#objects
engine = pyttsx3.init() # creates the object



# definitions
def configureEngine(gender, speechRate):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[gender].id)  #changes the gender of the voice. (0 male, 1 female)

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + speechRate)   #changes the speech rate of the voice.


def save(string):
    engine.save_to_file(string, 'outcome.mp3')  #saves the audio
    engine.runAndWait()                         #ends the action



