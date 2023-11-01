import tkinter as tk

window = tk.Tk()
window.title("Флаг Израиля с Звездой Давида и оконтовкой")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Очистить холст
canvas.delete("all")

# Нарисовать флаг Израиля
canvas.create_rectangle(0, 0, 400, 80, fill="blue")
canvas.create_rectangle(0, 80, 400, 160, fill="white")
canvas.create_rectangle(0, 160, 400, 240, fill="blue")

# Нарисовать оконтовку Звезды Давида (черная)
star_x = 200
star_y = 120
star_size = 30

# Создать контур Звезды Давида (черный)
canvas.create_polygon(
    star_x, star_y - star_size,
    star_x + 0.866 * star_size, star_y + 0.5 * star_size,
    star_x - 0.866 * star_size, star_y + 0.5 * star_size,
    star_x, star_y + star_size,
    star_x + 0.866 * star_size, star_y - 0.5 * star_size,
    star_x - 0.866 * star_size, star_y - 0.5 * star_size,
    fill="", outline="black"
)

# Заполнить Звезду Давида (синим)
canvas.create_polygon(
    star_x, star_y - star_size + 3,  # Смещение на 3 пикселя вверх
    star_x + 0.866 * star_size, star_y + 0.5 * star_size + 3,  # Смещение на 3 пикселя вниз
    star_x - 0.866 * star_size, star_y + 0.5 * star_size + 3,  # Смещение на 3 пикселя вниз
    star_x, star_y + star_size + 3,  # Смещение на 3 пикселя вниз
    star_x + 0.866 * star_size, star_y - 0.5 * star_size + 3,  # Смещение на 3 пикселя вверх
    star_x - 0.866 * star_size, star_y - 0.5 * star_size + 3,  # Смещение на 3 пикселя вверх
    fill="blue", outline=""
)

window.mainloop()
