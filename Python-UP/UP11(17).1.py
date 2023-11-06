class Book:
    def __init__(self, title, author, publication_year, isbn):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
    def display_book_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год публикации: {self.publication_year}")
        print(f"ISBN: {self.isbn}")

book1 = Book("Цвет из иных миров", "Говард Лавкрафт", 1927, "123-5-567-8901-2")
book2 = Book("Оно", "Стивен Кинг", 1986, "123-5-567-8901-3")
library = [book1, book2]
while True:
    print("Меню:")
    print("1. Добавить новую книгу")
    print("2. Показать информацию о существующих книгах")
    print("3. Выйти из программы")
    choice = input("Выберите опцию: ")
    if choice == '1':
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        publication_year = int(input("Введите год публикации: "))
        isbn = input("Введите ISBN книги: ")
        new_book = Book(title, author, publication_year, isbn)
        library.append(new_book)
        print("Книга успешно добавлена!")
    elif choice == '2':
        if not library:
            print("В библиотеке нет книг.")
        else:
            for i, book in enumerate(library, 1):
                print(f"Книга {i}:")
                book.display_book_info()
                print("\n")
    elif choice == '3':
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите существующую опцию (1, 2 или 3).")