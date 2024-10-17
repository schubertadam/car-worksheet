from tkinter import Frame
from typing import Any

import ttkbootstrap as ttk
from ttkbootstrap import SECONDARY, SUCCESS


def label(frame: Frame, text: str, row: int, column: int, **kwargs):
    tmp_label = ttk.Label(frame, text=text, **kwargs)
    tmp_label.grid(row=row, column=column, padx=10, pady=5, sticky="w")

    return tmp_label

def entry(frame: Frame, row: int, column: int, **kwargs):
    tmp_entry = ttk.Entry(frame, width=30, **kwargs)
    tmp_entry.grid(row=row, column=column, padx=10, pady=5)
    return tmp_entry

def heading(frame: Frame, text: str, row: int, column: int, **kwargs):
    return ttk.Label(frame, text=text, bootstyle=SECONDARY, font=("TkDefaultFont", 14, "bold"),
                     foreground="white").grid(row=row, column=column, columnspan=2, padx=10, pady=10, sticky="w", **kwargs)

def button(frame: Frame, text: str, row: int, column: int, command: Any, style=SUCCESS):
    return ttk.Button(frame, text=text, bootstyle=style, command=command).grid(row=row, column=column, pady=20)