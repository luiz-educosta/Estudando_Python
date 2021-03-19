from gtts import gTTS
#from subprocess import call
from playsound import playsound

def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')  #  texto para audio
    tts.save('audios/comando_invalido.mp3')

    #call(['aplay', 'audios/feedback.mp3'])
    playsound('audios/comando_invalido.mp3')


cria_audio('Você fez algum comando errado!')