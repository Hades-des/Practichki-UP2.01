def count_even_numbers(filename):
    try:
       with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file if int(line.strip()) % 2 == 0]
        return len(numbers)
    except FileNotFoundError:
        print("Файл не найден.")
        return 0
filename = 'other/f.txt'
count_of_even_numbers = count_even_numbers(filename)
print(f"Количество четных чисел в файле: {count_of_even_numbers}")
#библиотека: классы - читатель(id,дата посещения, название книги), сотрудник(id,рабочие дни), читательский билет(название книги, кто ее взял, когда взяли, чья смена сотрудника)