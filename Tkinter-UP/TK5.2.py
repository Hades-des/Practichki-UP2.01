import tkinter as tk

def add_to_listbox(event):
    text = entry.get()
    listbox.insert(tk.END, text)
    entry.delete(0, tk.END)

def copy_to_entry(event):
    selected_text = listbox.get(listbox.curselection())
    entry.delete(0, tk.END)
    entry.insert(0, selected_text)

root = tk.Tk()

entry = tk.Entry(root)
entry.pack(pady=10)
entry.bind("<Return>", add_to_listbox)

listbox = tk.Listbox(root)
listbox.pack()
listbox.bind("<Double-Button-1>", copy_to_entry)

root.mainloop()
