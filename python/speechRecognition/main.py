'''
    Author: M. Canesche
    Date: 01/12/18
    About: Speech Recognition for text just in english.
'''

# libraries
import speech_recognition as sr

def main():
    r = sr.Recognizer()                 # initialize recognizer
    with sr.Microphone(device_index=0) as src:
        print("Speak Anything: ")
        audio = r.listen(src)           # listen to the source
        try:
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
        except:
            print("Sorry could`nt reconize your voice! Please speak in english.")

if __name__ == "__main__" :
    main()
