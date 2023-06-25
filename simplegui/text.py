import PySimpleGUI as sg
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 200
window_height = 150

window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2
print(window_x, window_y)
