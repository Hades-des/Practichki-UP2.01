import tkinter as tk
window = tk.Tk()
window.title("Пример рисунка с Tkinter")
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()
canvas.create_rectangle(10, 10, 80, 80, fill="blue")
canvas.create_oval(300, 300, 100, 100, fill="red")
canvas.create_polygon(10, 150, 10, 1000, 300, 600, fill="green")
canvas.create_line(700, 700, 100, 100, fill="black", width=3)
canvas.create_polygon(150, 50, 250, 150, 150, 250, 50, 150, fill="gray", outline="black")
window.mainloop()

