from tkinter import *

def motion(x_target, y_target):
    x1, y1, x2, y2 = c.coords(ball)
    if x1 < x_target:
        c.move(ball, 1, 0)
    elif x1 > x_target:
        c.move(ball, -1, 0)
    if y1 < y_target:
        c.move(ball, 0, 1)
    elif y1 > y_target:
        c.move(ball, 0, -1)
    if (x1, y1) != (x_target, y_target):
        root.after(10, motion, x_target, y_target)
def on_canvas_click(event):
    x_target, y_target = event.x, event.y
    motion(x_target, y_target)
root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140, fill='black')
c.bind("<Button-1>", on_canvas_click)
root.mainloop()
