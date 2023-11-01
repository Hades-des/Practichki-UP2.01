
with open('f.txt', 'r') as file_f:
    numbers = list(map(int, file_f.read().split()))
    unique_numbers = list(set(numbers))


with open('g.txt', 'w') as file_g:
    for num in unique_numbers:
        file_g.write(str(num) + '\n')
