import tkinter as tk

def open_file():
    file_name = entry.get()
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
    except FileNotFoundError:
        text.delete(1.0, tk.END)
        text.insert(tk.END, "Файл не найден")
    except UnicodeDecodeError:
        text.delete(1.0, tk.END)
        text.insert(tk.END, "Не удалось декодировать файл, попробуйте другую кодировку")

def save_file():
    file_name = entry.get()
    text_content = text.get(1.0, tk.END)
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(text_content)

root = tk.Tk()
root.title("Программа для работы с файлами")

input_frame = tk.Frame(root)
input_frame.pack(side=tk.TOP)

entry = tk.Entry(input_frame, width=82)
entry.pack(side=tk.LEFT, padx=5, pady=10)

open_button = tk.Button(input_frame, text="Открыть", command=open_file)
open_button.pack(side=tk.LEFT, padx=3)

save_button = tk.Button(input_frame, text="Сохранить", command=save_file)
save_button.pack(side=tk.LEFT, padx=3)

text = tk.Text(root)
text.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
