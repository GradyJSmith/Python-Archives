import tkinter as tk
from tkinter import font
import pygame
import time
import threading
import comtypes
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER

musicFile = r"YOUR_MUSIC_FILE_HERE"

def set_volume_to_50():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, 
        1, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(0.5, None)

def check_and_reset_volume():
    comtypes.CoInitialize()  # Initialize COM for the current thread
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, 
            1, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        
        while pygame.mixer.music.get_busy():
            # Get current volume and mute state
            current_volume = volume.GetMasterVolumeLevelScalar()
            is_muted = volume.GetMute()

            # Reset volume to 50% if it's different
            if current_volume != 0.5:
                volume.SetMasterVolumeLevelScalar(0.5, None)
            
            # Unmute if muted
            if is_muted:
                volume.SetMute(False, None)

            time.sleep(0.1)
    finally:
        comtypes.CoUninitialize()  # Uninitialize COM when done

def playSong():
    global numberInput, info, win, seconds, countdown_window
    loops = numberInput.get()
    seconds = loops * 313
    info['text'] = "This is going to take: " + str(round(seconds / 60, 1)) + " minutes."
    win.update_idletasks()
    open_countdown_window()
    update_counter()

    set_volume_to_50()  # Set volume to 50% before starting music

    pygame.mixer.init()
    pygame.mixer.music.load(musicFile)
    pygame.mixer.music.play(loops)

    threading.Thread(target=check_and_reset_volume, daemon=True).start()  # Start volume monitoring thread

def informer():
    global info
    info['text'] = "Your torture is over."
    win.protocol("WM_DELETE_WINDOW", win.destroy)
    countdown_window.destroy()

def update_counter():
    global seconds, countdown_label
    if seconds > 0:
        countdown_label['text'] = f"{seconds}"
        seconds -= 1
        countdown_window.after(1000, update_counter)
    else:
        countdown_label['text'] = "0"
        pygame.mixer.music.stop()
        informer()

def disable_close():
    pass

def open_countdown_window():
    global countdown_window, countdown_label, static_text_label
    countdown_window = tk.Toplevel(win)
    countdown_window.geometry("600x300")
    countdown_window.title("Countdown")
    countdown_window.configure(bg="black")
    countdown_window.protocol("WM_DELETE_WINDOW", disable_close)

    static_text_label = tk.Label(countdown_window, text="Seconds until torture is over:", fg="red", bg="black", font=("Helvetica", 24, "bold"))
    static_text_label.pack()

    countdown_label = tk.Label(countdown_window, text="0", fg="red", bg="black", font=("Helvetica", 72, "bold"))
    countdown_label.pack(expand=True)


win = tk.Tk()
win.protocol("WM_DELETE_WINDOW", disable_close)

question = tk.Label(text="How many times would you like to listen to the song?")
question.pack()

custom_font = font.Font(family="Helvetica", size=14, weight="bold", underline=1)
statement = tk.Label(text="IT IS A LOT OF TORTURE!!!", fg="red", font=custom_font)
statement.pack()

seconds = 0
counter_label = tk.Label(text="Seconds until torture is over: 0")
counter_label.pack()

numberInput = tk.Scale(from_=0, to=10, orient=tk.HORIZONTAL)
numberInput.pack()

button = tk.Button(win, text="Play Song", command=playSong)
button.pack()

info = tk.Label(text="")
info.pack()

win.mainloop()
