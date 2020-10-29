import shutil
from datetime import date

print("Задание 1:")
head = input("Введите заголовок: ")
body = input("Введите текст: ")
end = 50 * "―"

today = date.today()
print(71 * " " + str(today))
print(36 * " " + "«" + head + "»")

counter = 0
for i in range(len(body)):
    counter = counter + 1
    if body[i] == " " and counter > 60:
        body = body[:i] + "\n" + body[i + 1:]
        counter = 0

lines = body.split('\n')
for line in lines:
    print(line.center(shutil.get_terminal_size().columns))
print(end)
print("Количество слов в тексте: ", len(body.split()), "\n")

print("Задание 2:")
text = input("Введите текст: ")
print(text[::-1])
