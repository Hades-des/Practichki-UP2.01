import re

with open("other/text.txt", "r", encoding="utf-8") as file:
    text = file.read()

emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', text)
phone_numbers = re.findall(r'\(\d{3}\) \d{3}-\d{4}', text)
dates = re.findall(r'\d{2}/\d{2}/\d{4}', text)

email_count = len(emails)
phone_count = len(phone_numbers)
date_count = len(dates)


print("Email-адреса:", emails)
print("Номера телефонов:", phone_numbers)
print("Даты:", dates)
print("Общее количество email-адресов:", email_count)
print("Общее количество номеров телефонов:", phone_count)
print("Общее количество дат:", date_count)

with open("other/results.txt", "w", encoding="utf-8") as result_file:
    result_file.write(f"Email-адреса: {emails}\n")
    result_file.write(f"Номера телефонов: {phone_numbers}\n")
    result_file.write(f"Даты: {dates}\n")

print("Результаты записаны в results.txt.")
