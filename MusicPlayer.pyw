from tkinter import *
import pygame
from tkinter.filedialog import askdirectory
import os
from tkinter import messagebox

w1 = Tk()
w1.resizable(0, 0)
w1.title("Music Player")
w1.geometry("500x500+500+150")
w1.config(bg="powder blue")

pygame.mixer.init()

playlist = []
current = StringVar()
cb1 = IntVar()
vol = DoubleVar()
index = 0
p = 0
flag = 0

lbl1 = Label(w1, bg="lightblue1", fg="Black", text="PLAYLIST:")
lbl1.place(x=130, y=15)

lbl2 = Label(w1, bg="lightblue1", fg="Black", text="STATUS:")
lbl2.place(x=130, y=230)

lbl3 = Label(w1, bg="khaki1", fg="Black", text="VOLUME:")
lbl3.place(x=10, y=30)

musiclist = Listbox(w1, fg="black", bg="lightblue1", selectbackground="black",
                    selectmode=SINGLE, width=35, height=10, font=("SegoePrint", 10))
musiclist.place(x=130, y=40)

lblcursong = Label(w1, bg="lightblue1", fg="black", textvariable=current, width=35, relief=RIDGE)
lblcursong.place(x=130, y=255)


def set_vol(_=None):
    pygame.mixer.music.set_volume(vol.get() / 100)


v = Scale(w1, bg="khaki1", activebackground="gray9", fg="gray34",
          variable=vol, from_=0, to=100,
          tickinterval=20, orient="vertical",
          cursor="hand2", command=set_vol)
v.place(x=10, y=60)
v.set(50)


def load():
    global flag, length
    directory = askdirectory()
    if directory == '' and musiclist.curselection() == ():
        messagebox.showwarning("Attention", "No Directory Selected")
    else:
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
            messagebox.showerror("Error", "No MP3 files in the chosen Directory")


def play():
    global index,p
    sel = musiclist.curselection()
    if playlist == []:
        messagebox.showerror("Error", "No song in Playlist")
    elif sel == ():
        pygame.mixer.music.load(playlist[0])
        pygame.mixer.music.play()
        index = 0
        current.set(playlist[index])
    else:
        pygame.mixer.music.load(musiclist.selection_get())
        pygame.mixer.music.play()
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
    musiclist.activate(index)


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
    pygame.mixer.music.fadeout(500)
    current.set("Music Stopped")


def clear():
    musiclist.delete(0, END)
    pygame.mixer.music.stop()
    current.set("Playlist Cleared")


def close():
    w1.destroy()


btnload = Button(w1, bg="azure", fg="black", width=5, text="Add\nSongs", command=load)
btnload.place(x=400, y=60)

btnplay = Button(w1, bg="azure", fg="black", width=5, text=u"\u25B6", command=play)
btnplay.place(x=220, y=300)

btnpause = Button(w1, bg="azure", fg="black", width=5, text=u"\u23F8", command=pause)
btnpause.place(x=220, y=360)

btnstop = Button(w1, bg="azure", fg="black", width=5, text=u"\u23F9", command=stop)
btnstop.place(x=220, y=330)

btnnext = Button(w1, bg="azure", fg="black", width=5, text=u"\u23ED", command=nextm)
btnnext.place(x=270, y=330)

btnprev = Button(w1, bg="azure", fg="black", width=5, text=u"\u23EE", command=prev)
btnprev.place(x=170, y=330)

btnclear = Button(w1, bg="cyan", fg="black", width=10, text="Clear Playlist", command=clear)
btnclear.place(x=390, y=120)

btnclose = Button(w1, bg="azure", fg="black", width=8, text="Close", command=close)
btnclose.place(x=408, y=390)

w1.mainloop()
