#Задача 8. 
#Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4)
#так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на
#подсказку в том случае, если у него нет никаких предположений. Разработайте
#систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки,
#получали больше тех, кто запросил подсказку

#Napreenkova A. A.
#07.04.2017

import random

WORDS=(("питон", "название языка программирования"), ("анаграмма", "игра в слова"), ("простота", "отсутствие сложностей"), ("сложность", "противоположность простоты"), ("ответ", "решение загадки"), ("подстаканник", "предмет посуды"))
word = random.choice(WORDS)
advice = word[1]
word = word[0]
correct = word
jumble = ""
adviced=0

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(
"""
Добро пожаловать в игру 'Анаграммы'!
Надо переставить буквы так. чтобы получилось осмысленное слово.
(Для выхода нажмите Enter. не вводя своей версии.)
"""
)
print("Boт анаграмма: " , jumble)

guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct or guess == "":
    if guess != "":
        print("K сожалению. вы неправы.")
    else:
        print("Подсказка: " , advice)
        adviced = 1

    guess = input("Попробуйте снова: ")

if guess == correct:
    print("Дa. именно так! Вы отгадали!\n")
    if adviced:
        print("Вы использовали подсказку и заработали 100 баллов")
    else:
        print("Вы не использовали подсказку и заработали 1000 баллов")

print("Cnacибo за игру.")
input("\n\nHaжмитe Enter. чтобы выйти.")