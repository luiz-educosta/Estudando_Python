from os import terminal_size
from playsound import playsound # toca o mp3
import webbrowser as browser #  abrir o browser
from gtts import gTTS # grava a voz
from requests import get #  faz o get do site
from bs4 import BeautifulSoup #  faz o tratamento dos dados pegados
from cria_audios import *
#  Funções de comandos

def ultimas_noticias():
    site = get('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:5]: #  o item é por causa do XML e o 5 é a quantidade de noticias
        mensagem = item.title.text  # segundo objeto do XML
        cria_audio(mensagem)


def playlists(album):
    if album == 'pink_floyd':
        browser.open('https://open.spotify.com/track/6pnwfWyaWjQiHCKTiZLItr?si=33f08d42aa7c41be')
    elif album == 'encontro_tlc':
        browser.open('https://open.spotify.com/track/4TcdFQ8iPrEFW5a7G2ovlS?si=9770b6ffee8c4d4b')


def previsao_tempo(tempo = False, minmax = False):
    site = get('http://api.openweathermap.org/data/2.5/weather?id=3468445&appid=4b7ae495a9c574a14ea7f63a8cf5cce4&units=metric&lang=pt')
    clima = site.json()
    temperatura = clima['main']['temp']
    tmin = clima['main']['temp_min']
    tmax = clima['main']['temp_max']
    descricao = clima['weather'][0]['description']
    if tempo:
        mensagem = (f'No momento fazem {temperatura} graus com: {descricao}')   
    if minmax:
        mensagem = (f'Mínima de {tmin} graus e máxima de {tmax} graus')
    cria_audio(mensagem)

