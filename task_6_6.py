#Задача №6. вариант № 6.

#Создайте	игру,	в	которой	компьютер	загадывает	название	одного	из	семи	городов
#России,	имеющих	действующий	метрополитен,	а	игрок	должен	его	угадать.

#Карагеур Р.М.

import random

city = ["Москва","Самара","Екатеринбург","Новосибирск","Казань","Нижний Новгород","Петербург"]
Vvodcity = input("Назовите один из городов, где присутствует работающий метрополитен: ")
y = random.choice(city)
if y == "Vvodcity":
    print("Вы угадали! \nПравильный ответ:", y)
else:
    print("Вы не угадали! \nПравильный ответ:", y)
    input('\nPress enter for exit')