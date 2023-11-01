import tkinter as tk

def update_label():
    label.config(text=operator.get())

root = tk.Tk()
root.title("Радиокнопки")
root.geometry("250x200")

label = tk.Label(root, text="Номер тел.", padx=20)
label.pack(side=tk.RIGHT)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(side=tk.LEFT)

operator = tk.StringVar()

radio_button1 = tk.Radiobutton(frame, indicatoron=0, width=10, height=2,
                               text="Андрей", variable=operator,
                               value="+7 976 543 21 09", command=update_label)
radio_button2 = tk.Radiobutton(frame, indicatoron=0, width=10, height=2,
                               text="Петя", variable=operator,
                               value="+7 123 456 78 90", command=update_label)
radio_button3 = tk.Radiobutton(frame, indicatoron=0, width=10, height=2,
                               text="Артем", variable=operator,
                               value="+7 135 246 79 02", command=update_label)
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

root.mainloop()

