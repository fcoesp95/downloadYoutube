import sys
from funciones import *
from tkinter import *
from pytube import Playlist

def hacer_click():

 try:
  _valor = (entrada_texto.get())
  print(_valor)
  checkURL = existeDominio(_valor)
  print("")
  print(checkURL)

  if checkURL == True:
    etiqueta.config(text='URL correcta')
    p = Playlist(_valor)
    path = p.title
    etiquetaTitle.config(text=(f"Titulo de la playlist: {path} de {p.owner}"))
    
    #listbox = Listbox(vp)
    #listbox.grid(column=3, row=7, sticky=(W,E))

    x=1
    pedir = None
    import os

    if not os.path.exists(path):
      os.makedirs(path)
    for video in p.video_urls:
              
         # video_extension = sort_extension(video)

          video_resolutions, videos = sort_resolutions(video)

          i = 0
          for item in video_resolutions:
              """listbox.insert(END,item)
              boton_extension = Radiobutton(vp, text=item, command=seleccionar)
              boton_extension.grid(column=1, row=3)
              """
              v = IntVar()

          """  audioOvideo=Radiobutton(vp, text = item, variable = v, value = i)
              audioOvideo.grid(column=i, row=5)
              i += 1
              boton_extension = Button(vp, text="Seleccionar", command=seleccionar)
              boton_extension.grid(column=5, row=5)
          for item in video_resolutions: # Insertamos los items en un Listbox
                listbox.insert(END,item)
                boton_download = Button(vp, text="Descargar", command=downloading)
                boton_download.grid(column=1, row=4)

"""
          if (pedir is None):
            choice = pedirResolucion(video_resolutions, videos,x,path)
            pedir = video_resolutions[choice-1]


  else:
    etiqueta.config(text='Introduce una url valida')  

 except ValueError:
  etiqueta.config(text="Error!")

def downloading():
  print("Entra")

def seleccionar():
  _valor = (audioOvideo.get())
  print(_valor)

app = Tk()
app.title("Descargar Playlist")

#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

# URL
valor = ""
entrada_texto = Entry(vp, width=80, textvariable=valor)
entrada_texto.grid(column=0, row=3,columnspan=3)

## Buscar Playlist
boton = Button(vp, text="Buscar playlist", command=hacer_click)
boton.grid(column=5, row=3)

# Error URL o todo bien
etiqueta = Label(vp, text="")
etiqueta.grid(column=7, row=3, sticky=(W,E))

# Titulo de la playlist
etiquetaTitle = Label(vp, text="")
etiquetaTitle.grid(column=0, row=1, sticky=(W,E))


# Button for closing
exit_button = Button(vp, text="Exit", command=app.destroy)
exit_button.grid(column=7, row=7, sticky=(W,E))


app.mainloop()