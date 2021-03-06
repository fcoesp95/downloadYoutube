############### Librerias importadas ############### 
from funciones import *

from pytube import Playlist

x=1
pedir = None

domain = False
while domain == False:
            urlUser = (input('\nWrite a url: '))
            try:
                checkURL = existeDominio(urlUser,0)
                if checkURL == True:   
                    p = Playlist(urlUser)
                    domain = True
                    print('Its a Playlist') 
                    mode = "Playlist"
                else:
                    checkURL = existeDominio(urlUser,1)
                    if checkURL == True:    
                        p = YouTube(urlUser)
                        print("Its a video")
                        domain = True
                        mode = "Video"
                    else:
                        print("That's not a video and not a playlist.")
            except Exception as e:
                print(e)
                print("That's not a playlist.")
                """try:
                    checkURL = existeDominio(urlUser,1)
                    if checkURL == True:    
                        p = YouTube(urlUser)
                        print("Its a video")
                        domain = True
                        mode = "Video"""
                """except:
                    print("That's not a video.")"""


#p = Playlist(urlUser)
txt = p.title
path  = processString(txt)

audioOvideo = False
print("1. Only audio")
print("2. Audio and video")


validNumber = False
while validNumber == False:
    choice = (input('\nChoose A format Please: '))    
    if not choice.isdigit(): 
        print("That's not a whole number. Try again")
    else:
        choice = int(choice)
        if ((choice>2) or (choice<1)):
            print("That's not a whole number. Between 1 and 2")
        else:
            validNumber = True    
choice = int(choice)

if choice == 1:
            formatChoice = 1
            audioOvideo = True
elif choice == 2:
            formatChoice = 2
            audioOvideo = True  
print()

if mode == "Playlist":
    for video in p.video_urls:

        url = video


        ####### Para no tener que pedir recurrentemente la opcion solo se preguntara la primera vez #####
        if (pedir is None):
            if formatChoice == 1:
                video_resolutions, videos,itag,abr  = sort_resolutions_OnlyAudio(video)
            else:
                video_resolutions, videos = sort_resolutions_AudioandVideo(video)
            choice = pedirResolucion(video_resolutions, videos,x)
            pedir = video_resolutions[choice-1]

        choiceS = elegirOpcion(video_resolutions,pedir)
        print()
        print(f'Downloading video number {x}: url {video}  ')
        print()

        if formatChoice == 1:
            descargarAudio(video_resolutions,choiceS,x,url,path,itag,abr)
        else:
            descargarVideo(video_resolutions,choiceS,x,url,path)

        print()
        ####### Descargamos toda la Playlist #####################
        if x< p.length:
            x += 1
        else:
            print()
            print("Descargas finalizadas")

else:
    ####### Para no tener que pedir recurrentemente la opcion solo se preguntara la primera vez #####
        if (pedir is None):
            if formatChoice == 1:
                video_resolutions, videos,itag,abr  = sort_resolutions_OnlyAudio(urlUser)
            else:
                video_resolutions, videos = sort_resolutions_AudioandVideo(urlUser)
            choice = pedirResolucion(video_resolutions, videos,x)
            pedir = video_resolutions[choice-1]

        choiceS = elegirOpcion(video_resolutions,pedir)
        print()
        print(f'Downloading video number {x}: url {urlUser}  ')
        print()

        if formatChoice == 1:
            descargarAudio(video_resolutions,choiceS,x,urlUser,path,itag,abr)
        else:
            descargarVideo(video_resolutions,choiceS,x,urlUser,path)

        print()
        print("Descarga finalizada")
