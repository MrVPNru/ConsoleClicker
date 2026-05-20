import random
import sys
import threading
import time
import os
import json

cooldown = 0.5
auto_clicks = 0
print("Привет, это мой текстовый кликер.")
print("Нажимай на Enter, чтобы кликать, и на 'q', чтобы выйти.")
print("Что бы зайти в магазин, набери 'shop'.")

clicks = 0
multiplier = 1.0
cooldown = 0.5
auto_clicks = 0
in_shop = False
plush = 0
plush2 = 0
plush3 = 0

if os.path.exists("save.json"):
    try:
        with open("save.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            clicks = data.get("clicks", 0)
            multiplier = data.get("multiplier", 1.0)
            cooldown = data.get("cooldown", 0.5)
            auto_clicks = data.get("auto_clicks", 0)
            plush = data.get("plush", 0)
            plush2 = data.get("plush2", 0)
            plush3 = data.get("plush3", 0)
        print(f"Игра загружена! У тебя {clicks} кликов.")
    except Exception as e:
        print(f"Ошибка чтение файла. Игра начата с нуля. Ошибка: {e}")
def background_auto_clicker():
    global clicks
    while True:
        time.sleep(1)
        if auto_clicks > 0:
            clicks += auto_clicks

            if not in_shop:

                sys.stdout.write("\r\033[K")
                
                sys.stdout.write(f"Автокликер сработал! У тебя {clicks} кликов.")


                try:
                    import readline
                    current_input = readline.get_line_buffer()
                    sys.stdout.write(current_input)
                except Exception:
                    pass

            save_game()


threading.Thread(target=background_auto_clicker, daemon=True).start()

def save_game():

    global clicks, multiplier, cooldown, auto_clicks, plush, plush2, plush3
    data = {
        "clicks": clicks,
        "multiplier": multiplier,
        "cooldown": cooldown,
        "auto_clicks": auto_clicks,
        "plush": plush,
        "plush2": plush2,
        "plush3": plush3
    }
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


while True:

    user_input = input()
    
    if user_input.lower() == "q":
        print(f"Ты кликнул {clicks} раз. До свидания!")

    elif user_input.lower() == "shop":
        in_shop = True
        print("Добро пожаловать в магазин! Здесь ты можешь купить улучшения для своих кликов.")
        print(f"У тебя {clicks} кликов. Что купишь?")

        print("1. Увелечиние кликов на 1. 20 кликов.")
        print("2. Увелечиние кликов на 5. 100 кликов.")
        print("3. Увелечиние кликов на 10. 500 кликов.")
        print("4. Уменьшение времени между кликами на 0.1 секунды. 200 кликов.")
        print("5. Автокликер: клик каждую секунду. 10 кликов.")
        print("6.  Яйцо с питомцами: 300 кликов.")


        shop_choiche = int(input("Выбери улучшение: "))

        if shop_choiche == 1:
            if clicks >= 20:
                clicks -= 20
                print(f"Ты купил улучшение! У тебя осталось {clicks} кликов.")
                plush = 1
            else:
                print("У тебя недостаточно кликов для этой покупки.")
        elif shop_choiche == 2:
            if clicks >= 100:
                clicks -= 100
                print(f"Ты купил улучшение! У тебя осталось {clicks} кликов.")
                plush2 = 5
            else:
                print("У тебя недостаточно кликов для этой покупки.")
        elif shop_choiche == 3:
            if clicks >= 500:
                clicks -= 500
                print(f"Ты купил улучшение! У тебя осталось {clicks} кликов.")
                plush3 = 10
            else:
                print("У тебя недостаточно кликов для этой покупки.")

        elif shop_choiche == 4:
            if clicks >= 200:
                clicks -= 200
                print(f"Ты купил улучшение! У тебя осталось {clicks} кликов.")
                cooldown -= 0.1
            else:
                print("У тебя недостаточно кликов для этой покупки.")

        elif shop_choiche == 5:
            if clicks >= 10:
                clicks -= 10
                auto_clicks += 1
                print(f"Ты купил улучшение! У тебя осталось {clicks} кликов.")
                
                    
            else:
                print("У тебя недостаточно кликов для этой покупки.")

        elif shop_choiche == 6:
            if clicks >= 300:
                clicks -= 300
                print("Ты купил яйцо с питомцами! Давай посмотрим, что тебе досталось...")
                time.sleep(2)
                pets = ["Котенок", "Щенок", "Птичка", "Хомячок", "Рыбка", "Черепашка"]

                multipliers = [1.2, 1.4, 1.6, 1.9, 2.5, 3.0]

                chances = [50, 20, 15, 10, 4, 1]

                indices = list(range(len(pets)))
                pet = random.choices(indices, weights=chances, k=1)[0]
                print(f"Поздравляем! Ты получил {pets[pet]}! Твой множитель кликов теперь {multipliers[pet]}x!")
                multiplier *= multipliers[pet]
            else: 
                print("У тебя недостаточно кликов для этой покупки.")

        in_shop = False
        save_game()



    else:
        print("Ты кликнул!")
        print(f"У тебя {clicks} кликов.")
        clicks += int((1 + plush + plush2 + plush3) * multiplier)

        save_game()

        time.sleep(cooldown)

        try:
            import termios
            termios.tcflush(sys.stdin, termios.TCIFLUSH)
        except Exception:
            pass
        
