import sqlite3
import keyboard

def show_data():
    conn = sqlite3.connect('other/empl.db')
    cursor = conn.cursor()
    cursor.execute('SELECT full_name, id, position FROM employees')
    data = cursor.fetchall()
    for row in data:
        print(f'\nФИО: {row[0]}, ID: {row[1]}, Должность: {row[2]}')

conn = sqlite3.connect('other/empl.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS empl (
        id INTEGER PRIMARY KEY,
        full_name TEXT,
        position TEXT
    )
''')
keyboard.add_hotkey('1', show_data)
while True:

    user_input = input("Введите команду (1- Вывести данные,2 - Добавить данные, exit - Выход): ")

    if user_input == '2':
        full_name = input("Введите ФИО работника: ")
        employee_id = input("Введите ID работника: ")
        position = input("Введите должность работника: ")


        cursor.execute('INSERT INTO employees (full_name, id, position) VALUES (?, ?, ?)', (full_name, employee_id, position))
        conn.commit()
        print("Данные добавлены в базу данных.")
    elif user_input.lower() == 'exit':
        break
    else:
        print("Неверная команда. Введите 2 для добавления данных или 'exit' для выхода.")
conn.close()



