import os
import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize pygame
pygame.init()

# Create a music player class
class MusicPlayer:
    def __init__(self, window):
        self.window = window
        self.window.title("Rajesh Music player")

        # Initialize the pygame mixer
        pygame.mixer.init()

        # Create variables to track song list and current song index
        self.playlist = []
        self.current_song_index = 0

        # Create GUI elements
        self.song_label = tk.Label(window, text="", font=("Helvetica", 12))
        self.play_button = tk.Button(window, text="Play", command=self.play_music)
        self.pause_button = tk.Button(window, text="Pause", command=self.pause_music)
        self.stop_button = tk.Button(window, text="Stop", command=self.stop_music)
        self.next_button = tk.Button(window, text="Next", command=self.next_song)
        self.prev_button = tk.Button(window, text="Previous", command=self.prev_song)
        self.add_button = tk.Button(window, text="Add Songs", command=self.add_songs)

        # Create and configure a playlist box
        self.playlist_box = tk.Listbox(window, selectmode=tk.SINGLE, height=10, width=50)
        self.playlist_box.bind("<Double-1>", self.play_selected_song)

        # Grid layout for GUI elements
        self.song_label.grid(row=0, column=0, columnspan=3)
        self.play_button.grid(row=1, column=0)
        self.pause_button.grid(row=1, column=1)
        self.stop_button.grid(row=1, column=2)
        self.prev_button.grid(row=2, column=0)
        self.next_button.grid(row=2, column=2)
        self.add_button.grid(row=3, column=0, columnspan=3)
        self.playlist_box.grid(row=4, column=0, columnspan=3)

    def add_songs(self):
        # Open a file dialog to select multiple songs
        songs = filedialog.askopenfilenames(title="Select Songs", filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))

        # Add selected songs to the playlist
        for song in songs:
            self.playlist.append(song)
            song_name = os.path.basename(song)
            self.playlist_box.insert(tk.END, song_name)

    def play_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.load(self.playlist[self.current_song_index])
            pygame.mixer.music.play()
            self.update_song_label()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.song_label.config(text="")

    def next_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
        self.play_music()

    def prev_song(self):
        self.current_song_index = (self.current_song_index - 1) % len(self.playlist)
        self.play_music()

    def play_selected_song(self, event):
        selected_index = self.playlist_box.curselection()[0]
        self.current_song_index = selected_index
        self.play_music()

    def update_song_label(self):
        current_song = os.path.basename(self.playlist[self.current_song_index])
        self.song_label.config(text="Now Playing: " + current_song)

# Create the main window
window = tk.Tk()
music_player = MusicPlayer(window)
window.mainloop()
