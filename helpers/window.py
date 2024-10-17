from tkinter import StringVar, PhotoImage

def center_window(self, window_width, window_height):
    # Képernyő szélessége és magassága
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()

    # Középre helyezés kiszámítása
    position_top = int((screen_height - window_height) / 2)
    position_right = int((screen_width - window_width) / 2)

    # Az ablak pozíciójának beállítása
    self.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

import tkinter as tk
from tkinter import PhotoImage

def set_window_icon(window, icon_path="assets/logo.png"):
    """Beállítja az ablak és a taskbar ikonját."""
    icon_image = PhotoImage(file=icon_path)
    window.iconphoto(False, icon_image)
