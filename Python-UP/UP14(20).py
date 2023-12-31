import sqlite3


conn = sqlite3.connect('other/empl.db')
cursor = conn.cursor()

#Cотрудники/Зп(1)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Сотрудники (
        id INTEGER PRIMARY KEY,
        имя TEXT,
        фамилия TEXT,
        возраст INTEGER,
        адрес TEXT,
        телефон TEXT
    )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Зарплата (
        код INTEGER PRIMARY KEY,
        тариф REAL,
        отработанные_дни INTEGER,
        начислено REAL,
        премия REAL,
        налог REAL
    )''')

cursor.executemany("INSERT INTO Сотрудники VALUES (?, ?, ?, ?, ?, ?)", [
    (1, 'Иван', 'Иванов', 30, 'Москва', '+7 123 456-78-90'),
    (2, 'Петр', 'Петров', 35, 'Санкт-Петербург', '+7 987 654-32-10'),
    (3, 'Анна', 'Сидорова', 28, 'Новосибирск', '+7 234 567-89-01'),
    (4, 'Елена', 'Козлова', 40, 'Екатеринбург', '+7 345 678-90-12'),
    (5, 'Михаил', 'Семенов', 25, 'Казань', '+7 456 789-01-23')
])

cursor.executemany("INSERT INTO Зарплата VALUES (?, ?, ?, ?, ?, ?)", [
    (1, 1000, 20, 20000, 5000, 2000),
    (2, 1200, 18, 21600, 6000, 2500),
    (3, 900, 22, 19800, 4500, 1800),
    (4, 1100, 25, 27500, 5500, 2200),
    (5, 950, 21, 19950, 4800, 1900)
])
#Автомобили(2)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Автомобили (
        id INTEGER PRIMARY KEY,
        марка TEXT,
        мощность INTEGER,
        цена REAL,
        цвет TEXT,
        коэффициент_уценки REAL
    )''')

cursor.executemany("INSERT INTO Автомобили VALUES (?, ?, ?, ?, ?, ?)", [
    (1, 'Toyota', 150, 25000, 'Синий', 0.9),
    (2, 'Ford', 180, 28000, 'Красный', 0.85),
    (3, 'Honda', 140, 22000, 'Черный', 0.95),
    (4, 'Chevrolet', 160, 26000, 'Серебристый', 0.92),
    (5, 'Nissan', 170, 40000000, 'Зеленый', 0.88)
])

#Гостинницы/Дикректора(3)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Директора (
        id INTEGER PRIMARY KEY,
        фамилия TEXT,
        город TEXT,
        телефон TEXT,
        категория_гостиницы TEXT
    )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Гостиницы (
        id INTEGER PRIMARY KEY,
        наименование TEXT,
        число_мест INTEGER,
        цены_по_категориям TEXT
    )''')

cursor.executemany("INSERT INTO Директора VALUES (?, ?, ?, ?, ?)", [
    (1, 'Иванов', 'Москва', '+7 123 456-78-90', '5 звезд'),
    (2, 'Петров', 'Санкт-Петербург', '+7 987 654-32-10', '4 звезды'),
    (3, 'Сидорова', 'Новосибирск', '+7 234 567-89-01', '3 звезды'),
    (4, 'Козлова', 'Екатеринбург', '+7 345 678-90-12', '4 звезды'),
    (5, 'Семенов', 'Казань', '+7 456 789-01-23', '5 звезд')
])

cursor.executemany("INSERT INTO Гостиницы VALUES (?, ?, ?, ?)", [
    (1, 'Отель А', 100, '1000 руб/ночь'),
    (2, 'Гостиница Б', 80, '800 руб/ночь'),
    (3, 'Отель В', 120, '1200 руб/ночь'),
    (4, 'Гостиница Г', 90, '900 руб/ночь'),
    (5, 'Отель Д', 150, '1500 руб/ночь')
])
#Пословицы(4)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Начало_пословиц (
        id INTEGER PRIMARY KEY,
        начало TEXT  )''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Конец_пословиц (
        id INTEGER PRIMARY KEY,
        конец TEXT  )''')

cursor.executemany("INSERT INTO Начало_пословиц VALUES (?, ?)", [
    (1, 'Что ни говори,'),
    (2, 'Не имей 100 рублей,'),
    (3, 'Год спишь - год'),
    (4, 'Где раки зимуют,'),
    (5, 'Дорогу осилит')
])
cursor.executemany("INSERT INTO Конец_пословиц VALUES (?, ?)", [
    (1, 'да не выходи из лесу'),
    (2, 'а имей 100 друзей'),
    (3, 'просишь'),
    (4, 'там и раки ловят'),
    (5, 'идущий')
])
#Поставщики/Склад(5)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Поставщики (
        id INTEGER PRIMARY KEY,
        наименование TEXT,
        город TEXT,
        телефон TEXT,
        категория_товара TEXT
    )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Склад (
        id INTEGER PRIMARY KEY,
        товар TEXT,
        количество_поставок INTEGER,
        цена REAL
    )''')

cursor.executemany("INSERT INTO Поставщики VALUES (?, ?, ?, ?, ?)", [
    (1, 'Поставщик 1', 'Москва', '+7 123 456-78-90', 'Электроника'),
    (2, 'Поставщик 2', 'Санкт-Петербург', '+7 987 654-32-10', 'Одежда'),
    (3, 'Поставщик 3', 'Новосибирск', '+7 234 567-89-01', 'Продукты'),
    (4, 'Поставщик 4', 'Екатеринбург', '+7 345 678-90-12', 'Мебель'),
    (5, 'Поставщик 5', 'Казань', '+7 456 789-01-23', 'Автомобили')
])

cursor.executemany("INSERT INTO Склад VALUES (?, ?, ?, ?)", [
    (1, 'Телефоны', 500, 1000.0),
    (2, 'Футболки', 1000, 20.0),
    (3, 'Молоко', 2000, 1.0),
    (4, 'Стулья', 200, 50.0),
    (5, 'Автомобили', 50, 25000.0)
])


# Задание 1:Сформировать запрос на вывод данных из таблиц: код, фамилия, отработанные дни, начислено, премия.
cursor.execute('''
    SELECT Зарплата.код, Сотрудники.фамилия, Зарплата.отработанные_дни, Зарплата.начислено, Зарплата.премия
    FROM Зарплата
    INNER JOIN Сотрудники ON Зарплата.код = Сотрудники.id
''')
print("Задание 1:")
print(cursor.fetchall())

# Задание 2 : Сформировать запрос, выводящий данные: по требуемым кодам автомобилей; по уцененным автомобилям; по стоимости автомобилей ниже 4000000; по мощности автомобилей.
cursor.execute('''
    SELECT * FROM Автомобили
    WHERE id IN (2, 4)
    ''')
print("Задание 2:")
print(cursor.fetchall())

cursor.execute('''
    SELECT * FROM Автомобили
    WHERE коэффициент_уценки < 0.9
    ''')
print(cursor.fetchall())

cursor.execute('''
    SELECT * FROM Автомобили
    WHERE цена < 4000000
    ''')
print(cursor.fetchall())

cursor.execute('''
    SELECT * FROM Автомобили
    ORDER BY мощность
    ''')
print(cursor.fetchall())

# Задание 3: Сформировать запросы выводящие данные: о директорах гостиниц 1 категории; о директорах из требуемого города; о гостиницах с их реквизитами.
# Сформировать запрос, выводящий данные по следующим полям: первичный ключ, фамилия, город, категория гостиницы, наименование гостиницы, число мест.
cursor.execute('''
    SELECT Директора.id, Директора.фамилия, Директора.город, Директора.категория_гостиницы, Гостиницы.наименование, Гостиницы.число_мест
    FROM Директора
    INNER JOIN Гостиницы ON Директора.id = Гостиницы.id
    WHERE Директора.категория_гостиницы = '5 звезд'
    ''')
print("Задание 3 (директоры гостиниц 5 звезд):")
print(cursor.fetchall())

cursor.execute('''
    SELECT Директора.id, Директора.фамилия, Директора.город, Гостиницы.наименование
    FROM Директора
    INNER JOIN Гостиницы ON Директора.id = Гостиницы.id
    WHERE Директора.город = 'Москва'
    ''')
print("Задание 3 (директоры из Москвы):")
print(cursor.fetchall())

# Задание 4: Сформировать запрос, выводящий полную пословицу, по запросу ее кода
cursor.execute('''
    SELECT Начало_пословиц.начало , Конец_пословиц.конец 
    FROM Начало_пословиц
    Inner Join Конец_пословиц ON Начало_пословиц.id = Конец_пословиц.id
    WHERE Начало_пословиц.id = 2
    ''')
print("Задание 4:")
print(cursor.fetchall())

# Задание 5: Сформировать запрос, выводящий товар, предоставляемый поставщиком, с расчетом общей суммы товаров.
cursor.execute('''
    SELECT Поставщики.наименование, SUM(Склад.количество_поставок * Склад.цена) AS общая_сумма
    FROM Поставщики
    INNER JOIN Склад ON Поставщики.id = Склад.id
    GROUP BY Поставщики.наименование
    ''')

print("Задание 5:")
print(cursor.fetchall())

conn.close()
