import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, colorchooser
app = tk.Tk()
app.title("Заметки")
app.iconbitmap("cat-meme-funny.gif")
notes_listbox = tk.Listbox(app)
notes_listbox.pack()
note_text = tk.Text(app)
note_text.pack()
def save_note():
    note_content = note_text.get("1.0", tk.END)
    selected_note = notes_listbox.get(notes_listbox.curselection())
    if selected_note:
        file_name = selected_note + ".txt"
        with open(file_name, "w") as file:
            file.write(note_content)
        messagebox.showinfo("Успешно", "Заметка успешно сохранена!")
    else:
        messagebox.showerror("Ошибка", "Выберите заметку для сохранения.")
def load_note():
    selected_note = notes_listbox.get(notes_listbox.curselection())
    if selected_note:
        file_name = selected_note + ".txt"
        try:
            with open(file_name, "r") as file:
                note_content = file.read()
            note_text.delete("1.0", tk.END)
            note_text.insert("1.0", note_content)
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл не найден.")
    else:
        messagebox.showerror("Ошибка", "Выберите заметку для загрузки.")

def create_note():
    note_name = simpledialog.askstring("Создать заметку", "Введите имя заметки:")
    if note_name:
        notes_listbox.insert(tk.END, note_name)
        note_text.delete("1.0", tk.END)

def delete_note():
    selected_note = notes_listbox.get(notes_listbox.curselection())
    if selected_note:
        notes_listbox.delete(notes_listbox.curselection())
        file_name = selected_note + ".txt"
        try:
            import os
            os.remove(file_name)
        except FileNotFoundError:
            pass

def rename_note():
    selected_note = notes_listbox.get(notes_listbox.curselection())
    if selected_note:
        new_name = simpledialog.askstring("Переименовать заметку", "Введите новое имя заметки:")
        if new_name:
            if new_name in notes_listbox.get(0, tk.END):
                messagebox.showerror("Ошибка", "Заметка с таким именем уже существует.")
            else:
                notes_listbox.delete(notes_listbox.curselection())
                notes_listbox.insert(tk.END, new_name)
                old_file_name = selected_note + ".txt"
                new_file_name = new_name + ".txt"
                try:
                    import os
                    os.rename(old_file_name, new_file_name)
                    messagebox.showinfo("Успешно", "Заметка переименована успешно.")
                except FileNotFoundError:
                    pass
        else:
            messagebox.showerror("Ошибка", "Имя заметки не может быть пустым.")

def choose_font_color():
    selected_text = note_text.get(note_text.index(tk.SEL_FIRST), note_text.index(tk.SEL_LAST))
    color = colorchooser.askcolor()[1]
    note_text.tag_add("selected", note_text.index(tk.SEL_FIRST), note_text.index(tk.SEL_LAST))
    note_text.tag_configure("selected", foreground=color)

menu = tk.Menu(app)
app.config(menu=menu)
notes_menu = tk.Menu(menu)
menu.add_cascade(label="Заметки", menu=notes_menu)
notes_menu.add_command(label="Создать новую заметку", command=create_note)
notes_menu.add_command(label="Сохранить", command=save_note)
notes_menu.add_command(label="Загрузить", command=load_note)
notes_menu.add_command(label="Удалить заметку", command=delete_note)
notes_menu.add_command(label="Переименовать заметку", command=rename_note)

view_menu = tk.Menu(menu)
menu.add_cascade(label="Вид", menu=view_menu)
view_menu.add_command(label="Выбрать цвет текста", command=choose_font_color)

app.mainloop()
