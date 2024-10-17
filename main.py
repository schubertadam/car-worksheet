import ttkbootstrap as ttk
from tkinter import Menu
from helpers import window
from windows.settings import Settings

window_width = 1024
window_height = 768

class MainApplication(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")  # Darkly téma használata

        # Ablak alapbeállításai
        self.title("Munkalap készítő")
        self.geometry(f"{window_width}x{window_height}")
        window.center_window(self, window_width, window_height)

        window.set_window_icon(self)

        # Menüsor létrehozása
        self.create_menu()

    def create_menu(self):
        """Menüsor létrehozása."""
        menubar = Menu(self)

        # Fájl menü
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Kilépés", command=self.quit)
        menubar.add_cascade(label="Fájl", menu=file_menu)

        # Beállítások menü, ami nem lenyíló, csak egy egyszerű menüpont
        menubar.add_command(label="Beállítások", command=self.open_settings_window)

        # Menüsor hozzáadása az ablakhoz
        self.config(menu=menubar)

    def open_settings_window(self):
        """Beállítások ablak megnyitása."""
        settings_win = Settings(self)
        settings_win.grab_set()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
