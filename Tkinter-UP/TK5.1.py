import tkinter as tk

def change_text_size():
    try:
        rows = int(rows_entry.get())
        columns = int(columns_entry.get())
        text_widget.config(width=columns, height=rows)
    except ValueError:
        pass

def on_focus_in(event):
    text_widget.config(bg="white")

def on_focus_out(event):
    text_widget.config(bg="lightgrey")

root = tk.Tk()
root.title("Изменение размера")
rows_label = tk.Label(root, text="Rows:")
rows_label.grid(row=0, column=0)
rows_entry = tk.Entry(root)
rows_entry.grid(row=0, column=1)
columns_label = tk.Label(root, text="Columns:")
columns_label.grid(row=1, column=0)
columns_entry = tk.Entry(root)
columns_entry.grid(row=1, column=1)
resize_button = tk.Button(root, text="Изменить", command=change_text_size)
resize_button.grid(row=2, columnspan=2)
text_widget = tk.Text(root, width=30, height=10, bg="lightgrey")
text_widget.grid(row=3, columnspan=2)
text_widget.bind("<FocusIn>", on_focus_in)
text_widget.bind("<FocusOut>", on_focus_out)
root.mainloop()



