import tkinter as tk

def move_selected_items():
    selected_items = listbox1.curselection()
    for index in selected_items:
        item = listbox1.get(index)
        listbox2.insert(tk.END, item)
    for index in selected_items[::-1]:
        listbox1.delete(index)

def remove_selected_items():
    selected_items = listbox2.curselection()
    for index in selected_items:
        item = listbox2.get(index)
        listbox1.insert(tk.END, item)
    for index in selected_items[::-1]:
        listbox2.delete(index)

root = tk.Tk()
root.title("Списки товаров и покупок")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

listbox1 = tk.Listbox(frame, selectmode=tk.MULTIPLE)
listbox1.pack(side=tk.LEFT)

products = ["Macbook", "Ardor", "MSI Katana", "Huawei", "Samsung"]
for product in products:
    listbox1.insert(tk.END, product)

listbox2 = tk.Listbox(frame, selectmode=tk.MULTIPLE)
listbox2.pack(side=tk.RIGHT)

move_button = tk.Button(frame, text=">>>", command=move_selected_items)
move_button.pack()
remove_button = tk.Button(frame, text="<<<", command=remove_selected_items)
remove_button.pack()

root.mainloop()