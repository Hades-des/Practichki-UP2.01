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
app = tk.Tk()
app.title("Обработка данных исключений")
load_button = tk.Button(app, text="Загрузить файл", command=load_file)
load_button.pack()
save_button = tk.Button(app, text="Сохранить файл", command=save_file)
save_button.pack()
clear_button = tk.Button(app, text="Очистить", command=clear_text)
clear_button.pack()
text = tk.Text(app)
text.pack()
app.mainloop()
