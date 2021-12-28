############### Librerias importadas ############### 
from onlyFunction import *

from pytube import Playlist


print("Please Paste The URL of the youtube video")
#urlUser = (input('\nWrite a url: '))
print()
#p = Playlist('https://www.youtube.com/playlist?list=PLWys0ZbXYUy7GYspoUPPsGzCu1bdgUdzf')


x=1
pedir = None

domain = False
while domain == False:
            urlUser = (input('\nWrite a url: '))
            checkURL = existeDominio(urlUser)    
            if checkURL == False: 
                print("That's not a valid URL. Try again")
                domain = False     
            else:
                try:
                    p = Playlist(urlUser) 
                    if p.length >0:  
                        domain = True 
                        mode = "Playlist"
                except:
                    print("That's not a playlist.")
                    try:
                        p = YouTube(urlUser)
                        print("But its a video")
                        domain = True
                        mode = "Video"
                    except:
                        print("That's not a video.")


#p = Playlist(urlUser)
path = p.title
existeCarpeta(path)

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
                video_resolutions, videos,itag  = sort_resolutions_OnlyAudio(video)
            else:
                video_resolutions, videos = sort_resolutions_AudioandVideo(video)
            choice = pedirResolucion(video_resolutions, videos,x)
            pedir = video_resolutions[choice-1]

        choiceS = elegirOpcion(video_resolutions,pedir)
        print()
        print(f'Downloading video number {x}: url {video}  ')
        print()

        if formatChoice == 1:
            descargarAudio(video_resolutions,choiceS,x,url,path,itag)
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
                video_resolutions, videos,itag  = sort_resolutions_OnlyAudio(urlUser)
            else:
                video_resolutions, videos = sort_resolutions_AudioandVideo(urlUser)
            choice = pedirResolucion(video_resolutions, videos,x)
            pedir = video_resolutions[choice-1]

        choiceS = elegirOpcion(video_resolutions,pedir)
        print()
        print(f'Downloading video number {x}: url {urlUser}  ')
        print()

        if formatChoice == 1:
            descargarAudio(video_resolutions,choiceS,x,urlUser,path,itag)
        else:
            descargarVideo(video_resolutions,choiceS,x,urlUser,path)

        print()