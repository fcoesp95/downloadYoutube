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
    abr = []

    for stream in my_video.streams.filter(only_audio=True):
        auxiliar = stream.mime_type + " " + stream.abr
        video_resolutions.append(auxiliar)
        videos.append(stream)
        itag.append(stream.itag)
        abr.append(stream.abr)
    return video_resolutions, videos,itag,abr
################################################################
############### Descargar Video de la Playlist #################
################################################################
def descargarVideo(video,choice,x,url,path):
    nuevoStream = "%s."% (x)
    #formato = video[choice]    

    from pytube import YouTube
    downloader = "'"+url+"'"
    yt = YouTube(downloader,on_progress_callback=on_progress)
    print(f'El titulo es: {yt.title}')
    nameVideo = "./" +path +"/"+path + "_video.txt"
    
    variable = choice
    intentos = 0

    

    existeVideo = False
    ######## Comprobar si ya esta el archivo descargado
    if  os.path.exists(nameVideo):       
        f = open(nameVideo, "r",encoding='utf-8')
        for x in f:
            if (yt.title +f" {video[variable]}").strip() ==  x.strip(): 
                print(x.strip())
                print(f'El video {yt.title} se ha descargado anteriormente')
                existeVideo = True
    while existeVideo != True:
        formato = video[variable]
        try:
            yt.streams.filter(file_extension='mp4').get_by_resolution(formato).download(output_path=path,filename_prefix=nuevoStream)
            
            f = open(nameVideo, "a",encoding='utf-8')
            f.write(yt.title +f" {video[variable]}"+"\n")
            f.close()

            existeVideo = True
        except Exception as e:
            intentos +=1
        if(intentos >3):
            intentos =0
            variable -= 1
    #yt.streams.filter(file_extension='mp4').get_by_resolution(formato).download(output_path=path,filename_prefix=nuevoStream)

################################################################
############### Descargar Audio de la Playlist #################
################################################################
def descargarAudio(video,choice,x,url,path,itag,abr):
    nuevoStream = "%s."% (x)
    formatoItag = itag[choice]    

    from pytube import YouTube
    downloader = "'"+url+"'"
    yt = YouTube(downloader,on_progress_callback=on_progress)
    print(f'El titulo es: {yt.title}')

    nameAudio = "./" +path +"/"+path + "_audio.txt"
    
    variable = choice
    intentos = 0

    existeAudio = False
    ######## Comprobar si ya esta el archivo descargado
    if  os.path.exists(nameAudio):       
        f = open(nameAudio, "r",encoding='utf-8')
        for x in f:
            if (yt.title +f" {abr[variable]}").strip() ==  x.strip(): 
                print(x.strip())
                print(f'El video {yt.title} se ha descargado anteriormente')
                existeAudio = True
    while existeAudio != True:
        formatoItag = itag[variable]
        try:
            yt.streams.get_by_itag(formatoItag).download(output_path=path,filename_prefix=nuevoStream)
            
            f = open(nameAudio, "a",encoding='utf-8')
            f.write(yt.title +f" {abr[variable]}"+"\n")
            f.close()
            existeAudio = True
        except Exception as e:
            intentos +=1
        if(intentos >3):
            intentos =0
            variable -= 1

def elegirOpcion(video_resolutions,pedir):
    choiceS = ''
    x = 0
    for resolution in video_resolutions:
        if pedir == resolution:
            choiceS = x
        x +=1
    return choiceS


################################################################
############### Cambiar caracteres #############################
################################################################
def processString(txt):
  specialChars = '\/:*?"<>|' 
  for specialChar in specialChars:
    txt = txt.replace(specialChar, '')
  existeCarpeta(txt)
  return txt  

################################################################
############### Crear carpeta si no existe y el txt ############
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
def existeDominio(url,value):
    checkURL = False
    checker_url_video = "https://www.youtube.com/oembed?url=http://www.youtube.com/watch?v="
    checker_url_playlist = "https://www.youtube.com/oembed?url=http://www.youtube.com/playlist?list="
    partesURL = url.split("=")
    if value == 0:
        checker_url = checker_url_playlist
    elif value == 1:
        checker_url = checker_url_video
    checkName = partesURL[0].startswith('https://www.youtube.com/')
    if checkName == True:    
        try:
            response = requests.get(url)
            video_url = checker_url + partesURL[-1]
            response = requests.get(video_url)
            if response.status_code == 200:
                print("URL is valid on the internet")
                checkURL = True
            else:
                checkURL = False    
        except requests.ConnectionError as exception:
            print("URL does not exist on Internet")
            print(exception)
            checkURL = False
        finally:
            return checkURL   
    else:
            print('Format not valid')
            return checkURL    