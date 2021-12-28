############### Librerias importadas ###############
from tkinter.constants import NUMERIC
from pytube import YouTube
from pytube import Playlist

from pytube.cli import on_progress #this module contains the built in progress bar. 

################################################################
############### Preguntar Resolucion de Descarga ###############
################################################################
def pedirResolucion(video_resolutions, videos,x):

        ############### Listar por pantalla las  ###############
        ############### Resoluciones Disponibles ###############
        i = 1
        for resolution in video_resolutions:
            print(f'{i}. {resolution}')
            i += 1

        ############### Solo es valido Number ##################
        validNumber = False
        while validNumber == False:
            Resolucionchoice = (input('\nChoose A resolution Please: '))    
            if not Resolucionchoice.isdigit(): 
                print("That's not a whole number. Try again")
            else:
                Resolucionchoice = int(Resolucionchoice)
                if ((Resolucionchoice>i-1) or (Resolucionchoice<1)):
                    print(f"That's not a whole number. Between 1 and {i-1}")
                else:
                    validNumber = True    
        Resolucionchoice = int(Resolucionchoice)
        return Resolucionchoice

################################################################
############### Ordenar resoluciones AudioyVideo ###############
################################################################
def sort_resolutions_AudioandVideo(url):

    my_video = YouTube (url)

    video_resolutions = []
    videos = []
    for stream in my_video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution'):
        video_resolutions.append(stream.resolution)
        videos.append(stream)


    return video_resolutions, videos

################################################################
############### Ordenar resoluciones Solo Audio ################
################################################################
def sort_resolutions_OnlyAudio(url):

    my_video = YouTube (url)

    video_resolutions = []
    videos = []
    itag = []
    for stream in my_video.streams.filter(only_audio=True):
        video_resolutions.append(stream.mime_type)
        videos.append(stream)
        itag.append(stream.itag)
        print(f"{stream.mime_type} con una abr de {stream.abr}")
    return video_resolutions, videos,itag
################################################################
############### Descargar Video de la Playlist #################
################################################################
def descargarVideo(video,choice,x,url,path):
    nuevoStream = "%s."% (x)
    formato = video[choice]    

    from pytube import YouTube
    downloader = "'"+url+"'"
    yt = YouTube(downloader,on_progress_callback=on_progress)
    print(f'El titulo es: {yt.title}')
    yt.streams.filter(file_extension='mp4').get_by_resolution(formato).download(output_path=path,filename_prefix=nuevoStream)

################################################################
############### Descargar Audio de la Playlist #################
################################################################
def descargarAudio(video,choice,x,url,path,itag):
    nuevoStream = "%s."% (x)
    formato = video[choice]    
    formatoItag = itag[choice]    

    from pytube import YouTube
    downloader = "'"+url+"'"
    yt = YouTube(downloader,on_progress_callback=on_progress)
    print(f'El titulo es: {yt.title}')
    yt.streams.get_by_itag(formatoItag).download(output_path=path,filename_prefix=nuevoStream)

def elegirOpcion(video_resolutions,pedir):
    choiceS = ''
    x = 0
    for resolution in video_resolutions:
        if pedir == resolution:
            choiceS = x
        x +=1
    return choiceS

################################################################
############### Crear carpeta si no existe #####################
################################################################
import os
def existeCarpeta(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Carpeta para la ruta {path} creada con exito")
        print()

################################################################
############### Comprobar dominio de la url ####################
################################################################
import requests
def existeDominio(url):
    checkURL = False
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("URL is valid on the internet")
            checkURL = True
    except requests.ConnectionError as exception:
        print("URL does not exist on Internet")
        print(exception)
        checkURL = False
    finally:
        return checkURL   
