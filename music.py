from tkinter import *
import pygame
from tkinter import filedialog
import os


pygame.mixer.init()

root=Tk()
root.title("Music PLayer")
root.geometry("1000x500")
root.configure(bg="black")



def add_song():
    song = filedialog.askopenfilename(initialdir="songs", title="Choose a Song", filetypes=(("wav Files","*.wav"),))
    os.chdir('songs')
    #song = song.replace(".wav", "")
    lst_box.insert(END, song)

def play():
    song = lst_box.get(ACTIVE)
    #song = f"/home/user/Documents/python_exercises/audio_player/songs/{song}.wav"
    pygame.mixer.init()

    pygame.mixer.music.load(song)
    x = song[40::1]
    display_label.config(text=x)
    pygame.mixer.music.play()

def unpausesong():
    # It will Display the  Status
    #status.set("-Playing")
    # Playing back Song
    pygame.mixer.music.unpause()

def pausesong():
    # Displaying Status
    #status.set("-Paused")
    # Paused Song
    pygame.mixer.music.pause()


def stopsong():
    # Displaying Status
    #status.set("-Stopped")
    # Stopped Song
    pygame.mixer.music.stop()

#labels
lblframe1=LabelFrame(root,text="Song Playing")
lblframe1.pack(fill="both")
lblframe1.place()

display_label = Label(root, text=">song name here<")
display_label.place(x=15,y=15)

lblframe2=LabelFrame(root,text="Playlist")
lblframe2.pack(fill="both")
lblframe2.place(x=450, y=10)
lst_box=Listbox(lblframe2, bg="white", fg="blue", width=60)
lst_box.pack(padx=20, pady=20)

lblframe3=LabelFrame(root,text="Buttons")
lblframe3.pack(fill="both")
lblframe3.place()

pause_btn=Button(root, text="Pause Song", bg="red", command=pausesong)
pause_btn.pack()
pause_btn.place(x= 200, y=250)

unpause_btn = Button(root, text='Unpause', bg="green", command=unpausesong)
unpause_btn.pack
unpause_btn.place(x=220, y=300)

play_btn=Button(root, text="Play Song", command=play, bg="white")
play_btn.pack()
play_btn.place(x= 100, y=250)

stopsong_btn = Button(root, text='Stop Song', bg="yellow", command=stopsong)
stopsong_btn.pack()
stopsong_btn.place(x=120, y=300)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add Song To Playlist", command=add_song)


root.mainloop()
