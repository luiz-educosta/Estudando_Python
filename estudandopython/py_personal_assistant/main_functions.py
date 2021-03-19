from os import terminal_size
from playsound import playsound # toca o mp3
from gtts import gTTS # grava a voz
import speech_recognition as sr # reconhecimento de voz
#  Precisa baixar os modulos: gcloud e google-api-python-client e não precisa importar por código
from cria_audios import *
from command_functions import *

#  Configurações Gerais
hotword = 'abigail'
with open('py-personal-assistant-86956b572fd9.json') as credenciais_google:
    credenciais_google = credenciais_google.read()

#  Funções principais

def monitora_audio():
    # obtendo audio do microfone
    microfone = sr.Recognizer()
    with sr.Microphone() as source:

        while True:  #  Loop para poder ficar esperando o comando
            print("Aguardando o Comando: ")
            audio = microfone.listen(source)

            # reconhecimento de voz usando Google Cloud Speech
            try:
                trigger = microfone.recognize_google_cloud(audio, credentials_json=credenciais_google, language='pt-BR')
                trigger = trigger.lower()

                if hotword in trigger:
                    print(f'COMANDO: {trigger}')
                    responde('feedback')
                    executa_comandos(trigger)
                    #  executar os comandos
                    break

            except sr.UnknownValueError:
                print("Google Cloud Speech could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Cloud Speech service; {e}")
    return trigger


def responde(arquivo):
    #call(['aplay', 'audios/'+ arquivo + '.mp3'])
    playsound('audios/'+ arquivo + '.mp3')


def executa_comandos(trigger):
    if 'notícias' in trigger:
        ultimas_noticias()
    elif 'toca' in trigger and 'pink floyd' in trigger:
        playlists('pink_floyd')
    elif 'toca' in trigger and 'tlc' in trigger:
        playlists('encontro_tlc')
    elif 'tempo agora' in trigger:
        previsao_tempo(tempo = True)
    elif 'temperatura hoje' in trigger:
        previsao_tempo(minmax = True)
    else:
        mensagem = trigger.strip(hotword)
        cria_audio(mensagem)
        print('COMANDO INVÁLIDO', mensagem)
        responde('comando_invalido')
