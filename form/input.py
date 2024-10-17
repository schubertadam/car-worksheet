import ttkbootstrap as ttk
from tkinter import Frame, messagebox


class Input:
    def __init__(self, frame: Frame, label: str, row: int, column: int, type: str ="text", required: bool = True, data_kwargs = None, **kwargs):
        self.required = required
        self.type = type

        if data_kwargs is None:
            data_kwargs = {}

        if type == "password":
            data_kwargs["show"] = "*"

        if self.required:
            label += "*"

        self.label = ttk.Label(frame, text=label, **kwargs)
        self.label.grid(row=row, column=column, padx=10, pady=5, sticky="w")

        self.data = ttk.Entry(frame, width=30, **data_kwargs)
        self.data.grid(row=row, column=column + 1, padx=10, pady=5, sticky="w")

    def get_label(self):
        return self.label

    def get_data(self):
        return self.data.get().strip()

    def set_data(self, index: int, string: str):
        self.data.insert(index, string)

    def validate(self):
        value = self.data.get()

        # Check if data is required
        if self.required and len(value) < 1:
            messagebox.showerror("Hiba", f"{self.label.cget('text')} mező kitöltése kötelező.")
            return False

        # If data data is email then check if data contains '@'
        if self.type == "email" and "@" not in value:
            messagebox.showerror("Hiba", f"Kérjük, érvényes email címet adjon meg a {self.label.cget('text')} mezőben.")
            return False

        return True