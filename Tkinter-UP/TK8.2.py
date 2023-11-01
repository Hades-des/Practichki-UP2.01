import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def load_file():
    try:
        file_path = filedialog.askopenfilename()
        if not file_path:
            messagebox.showinfo("Информация", "Файл не был выбран.")
        else:
            with open(file_path, 'r') as file:
                data = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, data)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при загрузке файла:\n{str(e)}")
def save_file():
    try:
        data = text.get(1.0, tk.END)
        if not data.strip():
            messagebox.showinfo("Информация", "Нет данных для сохранения.")
            return
        file_path = filedialog.asksaveasfilename()
        if not file_path:
            messagebox.showinfo("Информация", "Файл не был сохранен.")
        else:
            with open(file_path, 'w') as file:
                file.write(data)
            messagebox.showinfo("Информация", "Файл успешно сохранен.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при сохранении файла:\n{str(e)}")
def clear_text():
    if messagebox.askyesno("Подтверждение", "Вы уверены, что хотите очистить текст?"):
        text.delete(1.0, tk.END)
def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)
app = tk.Tk()
app.title("Обработка данных исключений")
menu = tk.Menu(app)
app.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить файл", command=load_file)
file_menu.add_command(label="Сохранить файл", command=save_file)
text = tk.Text(app)
text.pack()
text.bind("<Button-3>", show_context_menu)  # ПКМ
context_menu = tk.Menu(app, tearoff=0)
context_menu.add_command(label="Очистить", command=clear_text)
app.mainloop()
