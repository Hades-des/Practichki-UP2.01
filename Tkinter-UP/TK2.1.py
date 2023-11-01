import tkinter as tk

colors = {
    "Красный": "#ff0000",
    "Оранжевый": "#ff7d00",
    "Желтый": "#ffff00",
    "Зеленый": "#00ff00",
    "Голубой": "#007dff",
    "Синий": "#0000ff",
    "Фиолетовый": "#7d00ff"
}

def on_button_click(color_name, color_code):
    color_label.config(text=color_name)
    text_field.delete(1.0, tk.END)
    text_field.insert(tk.END, color_code)

root = tk.Tk()
root.title("Выберите цвет радуги")

color_label = tk.Label(root, text="", font=("Arial", 14))
color_label.pack(pady=10)

text_field = tk.Text(root, height=1, width=14, font=("Arial", 14))
text_field.pack()



button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for color_name, color_code in colors.items():
    button = tk.Button(button_frame, bg=color_code, width=20, height=2, command=lambda name=color_name, code=color_code: on_button_click(name, code))
    button.pack(side=tk.TOP, pady=5)


root.mainloop()
