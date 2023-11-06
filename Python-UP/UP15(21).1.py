try:
    with open('fail.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Файл не найден")

