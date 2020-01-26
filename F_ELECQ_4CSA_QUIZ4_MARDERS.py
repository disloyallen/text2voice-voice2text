import speech_recognition as sr
cobblestone = sr.Recognizer()
with sr.AudioFile("2person.wav") as source:
    audio = cobblestone.record(source)

try:
    text = cobblestone.recognize_google(audio)
    print('Generated text: ', text)
    print(text, file = open('output.txt', 'a'))

except:
    passamm