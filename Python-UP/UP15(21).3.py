try:
    input_str = input("Введите список чисел через запятую: ")
    num_list = [int(x) for x in input_str.split(',')]
    if not num_list:
        print("Список пуст")
    else:
        try:
            max_value = max(num_list)
            print("Максимальное значение в списке:", max_value)
        except ValueError:
            print("Список пуст")
        for num in num_list:
            try:
                if num == 0 or isinstance(num, str):
                    raise ValueError("Ошибка при делении элемента на 10")
                result = num / 10
                print(f"Результат деления {num} на 10:", result)
            except ValueError as e:
                print(str(e))
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    print("Программа завершена")
