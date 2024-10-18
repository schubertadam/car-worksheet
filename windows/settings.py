import configparser
from tkinter import PhotoImage, messagebox
from tkinter.ttk import Frame

import mysql.connector
from mysql.connector import Error
import ttkbootstrap as ttk
from ttkbootstrap import PRIMARY

from form.input import Input
from helpers import window
from helpers.form import heading, button

window_width = 800
window_height = 400

class Settings(ttk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Beállítások")
        self.geometry(f"{window_width}x{window_height}")
        window.center_window(self, window_width, window_height)
        self.config_file = "config.ini"

        window.set_window_icon(self)

        # Jelszó megtekintési állapot
        self.password_shown = False

        # Ikonok betöltése (nyitott és áthúzott szem ikonok)
        self.show_icon = PhotoImage(file="assets/icons/eye-solid.png")  # Nyitott szem ikon (PNG fájl)
        self.hide_icon = PhotoImage(file="assets/icons/eye-slash-solid.png")  # Áthúzott szem ikon (PNG fájl)

        self.create_form()
        self.load_config()

    def create_form(self):
        app_frame = self.create_app_form()
        db_frame = self.create_db_form()

        self.test_connection = button(db_frame, "Kapcsolat tesztelése", 5, 0, self.test_db_connection, style=PRIMARY)
        self.save = button(db_frame, "Mentés", 5, 1, self.save_config)

    def create_db_form(self, row: int = 0, column: int = 0) -> Frame:
        frame = ttk.Frame(self)
        frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        # DB HEADING
        heading(frame, "Adatbázis kapcsolat", 0, 0)

        self.db_host = Input(frame, "Hoszt:", 1, 0)
        self.db_name = Input(frame, "Adatbázis neve:", 2, 0)
        self.db_user = Input(frame, "Felhasználónév:", 3, 0)
        self.db_pass = Input(frame, "Jelszó:", 4, 0, "password")
        self.show_password = ttk.Button(frame, image=self.show_icon, command=self.toggle_password)
        self.show_password.grid(row=3, column=2, padx=5, pady=5)

        return frame

    def create_app_form(self, row: int = 0, column: int = 1) -> Frame:
        frame = ttk.Frame(self)
        frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # APP HEADING
        heading(frame, "Alkalmazás beállítások", 0, 0)

        # APP USER FULL NAME
        self.full_name = Input(frame, "Ügyintéző neve:", 1, 0)

        # APP USER FULL NAME
        self.zip_code = Input(frame, "Irányítószám:", 2, 0)

        # APP USER FULL NAME
        self.city = Input(frame, "Város:", 3, 0)

        # APP USER FULL NAME
        self.address = Input(frame, "Cím:", 4, 0)

        # APP USER FULL NAME
        self.tax_rate = Input(frame, "ÁFA kulcs:", 5, 0)

        # APP USER FULL NAME
        self.tax_number = Input(frame, "Adószám:", 6, 0)

        return frame

    def toggle_password(self):
        show_char = "*" if self.password_shown else ""
        icon = self.show_icon if self.password_shown else self.hide_icon

        self.db_pass.data.config(show=show_char)
        self.show_password.config(image=icon)

        self.password_shown = not self.password_shown

    def load_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)

        if "Database" in config:
            self.db_host.set_data(0, config["Database"].get("DB_HOST", ""))
            self.db_name.set_data(0, config["Database"].get("DB_NAME", ""))
            self.db_user.set_data(0, config["Database"].get("DB_USER", ""))
            self.db_pass.set_data(0, config["Database"].get("DB_PASS", ""))

        if "Application" in config:
            self.full_name.set_data(0, config["Application"].get("Agent_Name", ""))
            self.zip_code.set_data(0, config["Application"].get("Zip_Code", ""))
            self.city.set_data(0, config["Application"].get("City", ""))
            self.address.set_data(0, config["Application"].get("Address", ""))
            self.tax_rate.set_data(0, config["Application"].get("Tax_Rate", ""))
            self.tax_number.set_data(0, config["Application"].get("Tax_Number", ""))

    def save_config(self):
        config = configparser.ConfigParser()

        config["Database"] = {
            "DB_HOST": self.db_host.get_data(),
            "DB_NAME": self.db_name.get_data(),
            "DB_USER": self.db_user.get_data(),
            "DB_PASS": self.db_pass.get_data(),
        }

        config["Application"] = {
            "Agent_Name": self.full_name.get_data(),
            "Zip_Code": self.zip_code.get_data(),
            "City": self.city.get_data(),
            "Address": self.address.get_data(),
            "Tax_Rate": self.tax_rate.get_data(),
            "Tax_Number": self.tax_number.get_data()
        }

        with open(self.config_file, "w") as configfile:
            config.write(configfile)

        self.destroy()

    def test_db_connection(self):
        host = self.db_host.get_data()
        user = self.db_user.get_data()
        password = self.db_pass.get_data()
        database = self.db_name.get_data()

        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            if connection.is_connected():
                messagebox.showinfo("Sikeres kapcsolat", "Az adatbázis kapcsolat sikeres!")
                connection.close()

        except Error as e:
            messagebox.showerror("Kapcsolati hiba", f"Nem sikerült kapcsolódni az adatbázishoz: {str(e)}")