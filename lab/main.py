# config
PLANT_PRICE=100
ANIMAL_PRICE=500
HARVEST_PROFIT=300
FEED_PROFIT=25

# state
money = 100
crop_stage = 0
animals = 0

# константы для цветного форматирования вывода
CONSOLE_RED='\033[31m'
CONSOLE_GREEN='\033[32m'
CONSOLE_DEFAULT='\033[0m'

while True:
    key = input('Выберите команду (plant, water, by_animal, feed, harvest, report, exit): ')
    key = key.strip()

    if key == "plant":
        if money >= PLANT_PRICE:
            money -= PLANT_PRICE
            crop_stage = 1
            print(f'{CONSOLE_GREEN}Растения посажены{CONSOLE_DEFAULT}')
            print(f'{CONSOLE_RED}-{PLANT_PRICE}у.е.{CONSOLE_DEFAULT}')
        else:
            print(f'{CONSOLE_RED}Недостаточно средств. Необходимо {PLANT_PRICE}у.е.{CONSOLE_DEFAULT}')

    elif key == "water":
        crop_stage+=1
        print(f'{CONSOLE_GREEN}Растения политы{CONSOLE_DEFAULT}')

    elif key == "by_animal":
        if money >= ANIMAL_PRICE:
            money -= ANIMAL_PRICE
            animals += 1
            print(f'{CONSOLE_GREEN}Куплено животное{CONSOLE_DEFAULT}')
            print(f'{CONSOLE_RED}-{ANIMAL_PRICE}у.е.{CONSOLE_DEFAULT}')
        else:
            print(f'{CONSOLE_RED}Недостаточно средств. Необходимо {ANIMAL_PRICE}у.е.{CONSOLE_DEFAULT}')

    elif key == "feed":
        if animals > 0:
            money += FEED_PROFIT * animals
            print(f'{CONSOLE_GREEN}Животные покормлены{CONSOLE_DEFAULT}')
            print(f'{CONSOLE_GREEN}+{FEED_PROFIT * animals}у.е.{CONSOLE_DEFAULT}')
        else:
            print(f'{CONSOLE_RED}У вас нет животных. Доход не получен!{CONSOLE_DEFAULT}')

    elif key == "harvest":
        print(f'{CONSOLE_GREEN}Растения скошены{CONSOLE_DEFAULT}')

        if crop_stage >= 3:
            money += HARVEST_PROFIT
            print(f'{CONSOLE_GREEN}+{HARVEST_PROFIT}у.е.{CONSOLE_DEFAULT}')
        else:
            print(f'{CONSOLE_RED}Растения не успели вырасти. Доход не получен!{CONSOLE_DEFAULT}')

        crop_stage = 0

    elif key == "report":
        print(f'Текущее состояние: \n'
              f'- money: {money}\n'
              f'- crop_stage: {crop_stage}\n'
              f'- animals: {animals}')

    elif key == "exit":
        print(f'\n\nДосвидания! ;)\n\n')
        break

    else:
        print(f'{CONSOLE_RED}Неизветсная команда{CONSOLE_DEFAULT}')

    print("\n")