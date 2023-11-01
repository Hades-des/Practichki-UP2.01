import tkinter as tk
from tkinter import ttk

def change_canvas_color(event):
    selected_color = color_combobox.get()
    canvas.config(bg=selected_color)
root = tk.Tk()
root.title("Изменение цвета холста")
color_combobox = ttk.Combobox(root, values=["Red", "Green", "Blue", "Yellow", "Purple"])
color_combobox.set("Red")
color_combobox.pack(pady=10)
canvas = tk.Canvas(root, width=200, height=200, bg="red")
canvas.pack()
color_combobox.bind("<<ComboboxSelected>>", change_canvas_color)
root.mainloop()