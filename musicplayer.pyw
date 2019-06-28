from tkinter import *
import pygame
from tkinter.filedialog import askdirectory
import os
from tkinter import messagebox

pygame.mixer.init()

w1 = Tk()
w1.config()
w1.minsize(height=500, width=500)
w1.maxsize(height=600, width=600)
w1.title("Music")

playlist = []
current = StringVar()
index = 0
p = 0
flag = 0

lbl1 = Label(w1, bg="Linen", fg="Black", text="PLAYLIST:")
lbl1.place(x=100, y=20)

musiclist = Listbox(w1, fg="black", bg="linen", selectmode=SINGLE, width=50, height=10)
musiclist.place(x=100, y=40)

lbl2 = Label(w1, bg="Linen", fg="Black", text="STATUS:")
lbl2.place(x=100, y=230)

lblcursong = Label(w1, bg="linen", fg="blACK", textvariable=current, width=45, relief=GROOVE)
lblcursong.place(x=100, y=250)


def load():
    global flag
    directory = askdirectory()
    if directory == '':
        messagebox.showerror("error", "No Directory Selected")
    else:
        global length
        os.chdir(directory)
        playlist.clear()
        for i in os.listdir(directory):
            if i.endswith(".mp3"):
                flag = 1
                playlist.append(i)
        if flag == 1:
            length = len(playlist)
            musiclist.delete(0, END)
            if musiclist.size() == 0:
                for i in range(0, length):
                    musiclist.insert(i, "%s" % playlist[i])
            else:
                pass
        else:
            messagebox.showerror("Error", "No MP3 files in chosen Directory")


def play():
    global index
    if musiclist.selection_get() == " ":
        messagebox.showerror("error", " no song selected")
    else:
        pygame.mixer.music.load(musiclist.selection_get())
        pygame.mixer.music.play()
        sel = musiclist.curselection()
        current.set(playlist[sel[0]])
        musiclist.selection_clear(0, END)
        index = sel[0]


def nextm():
    global index
    index += 1
    if index <= (length-1):
        pygame.mixer.music.load(playlist[index])
        update()
        pygame.mixer.music.play()
    else:
        index = 0
        pygame.mixer.music.load(playlist[index])
        update()
        pygame.mixer.music.play()


def prev():
    global index
    index -= 1
    if index >= 0:
        pygame.mixer.music.load(playlist[index])
        update()
        pygame.mixer.music.play()
    elif index < 0:
        index = len(playlist)-1
        pygame.mixer.music.load(playlist[index])
        update()
        pygame.mixer.music.play()


def update():
    current.set(playlist[index])


def pause():
    global p
    if p == 0:
        pygame.mixer.music.pause()
        current.set("Music Paused")
        p = 1
    else:
        pygame.mixer.music.unpause()
        p = 0
        current.set(playlist[index])


def stop():
    pygame.mixer.music.fadeout(1000)
    current.set("Music Stopped")


def clear():
    musiclist.delete(0, END)
    pygame.mixer.music.fadeout(1000)
    current.set("Playlist Cleared")


def close():
    w1.destroy()


btnload = Button(w1, bg="linen", fg="black", width=10, text="Load Music", command=load)
btnload.place(x=310, y=330)

btnplay = Button(w1, bg="linen", fg="black", width=5, text=u"\u25B6", command=play)
btnplay.place(x=190, y=300)

btnpause = Button(w1, bg="linen", fg="black", width=5, text=u"\u23F8", command=pause)
btnpause.place(x=190, y=360)

btnstop = Button(w1, bg="linen", fg="black", width=5, text=u"\u23F9", command=stop)
btnstop.place(x=190, y=330)

btnnext = Button(w1, bg="linen", fg="black", width=5, text=u"\u21A6", command=nextm)
btnnext.place(x=240, y=330)

btnprev = Button(w1, bg="linen", fg="black", width=5, text=u"\u21E4", command=prev)
btnprev.place(x=140, y=330)

btnclear = Button(w1, bg="linen", fg="black", width=10, text="Clear Playlist", command=clear)
btnclear.place(x=400, y=330)

btnclose = Button(w1, bg="linen", fg="black", width=8, text="Close", command=close)
btnclose.place(x=180, y=400)

w1.mainloop()
