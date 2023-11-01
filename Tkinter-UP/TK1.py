import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.geometry("300x300")
root.title("Калькулятор")

entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = ['7', '8', '9', '+','4', '5', '6', '-','1', '2', '3', '*','C', '0', '=', '/']
i = 0
for button in buttons:
    button = tk.Button(button_frame, text=button, font=("Helvetica", 16))
    button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)
    i += 1

root.mainloop()
