import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from PIL import Image, ImageDraw

root = tk.Tk()
root.title("Рисование фигур")

canvas = tk.Canvas(root, width=400, height=400)
canvas.grid(row=0, column=0, columnspan=2)

def draw_shape(shape, x1, y1, x2, y2):
    if shape == "Прямоугольник":
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
    elif shape == "Овал":
        canvas.create_oval(x1, y1, x2, y2, fill="red")
def add_shape_window():
    shape_window = tk.Toplevel(root)
    shape_window.title("Добавить фигуру")
    x1_label = ttk.Label(shape_window, text="X1:")
    x1_label.grid(row=0, column=0)
    x1_entry = ttk.Entry(shape_window)
    x1_entry.grid(row=0, column=1)
    y1_label = ttk.Label(shape_window, text="Y1:")
    y1_label.grid(row=1, column=0)
    y1_entry = ttk.Entry(shape_window)
    y1_entry.grid(row=1, column=1)
    x2_label = ttk.Label(shape_window, text="X2:")
    x2_label.grid(row=2, column=0)
    x2_entry = ttk.Entry(shape_window)
    x2_entry.grid(row=2, column=1)
    y2_label = ttk.Label(shape_window, text="Y2:")
    y2_label.grid(row=3, column=0)
    y2_entry = ttk.Entry(shape_window)
    y2_entry.grid(row=3, column=1)
    shape_var = tk.StringVar()
    shape_var.set("Прямоугольник")
    shape_label = ttk.Label(shape_window, text="Выберите фигуру:")
    shape_label.grid(row=4, column=0, columnspan=2)
    rectangle_radio = ttk.Radiobutton(shape_window, text="Прямоугольник", variable=shape_var, value="Прямоугольник")
    rectangle_radio.grid(row=5, column=0, columnspan=2)
    oval_radio = ttk.Radiobutton(shape_window, text="Овал", variable=shape_var, value="Овал")
    oval_radio.grid(row=6, column=0, columnspan=2)
    def draw_shape_on_canvas():
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
        shape = shape_var.get()
        draw_shape(shape, x1, y1, x2, y2)
        shape_window.destroy()
    draw_button = ttk.Button(shape_window, text="Нарисовать", command=draw_shape_on_canvas)
    draw_button.grid(row=7, column=0, columnspan=2)
add_shape_button = ttk.Button(root, text="Добавить фигуру", command=add_shape_window)
add_shape_button.grid(row=1, column=0, columnspan=2)
root.mainloop()