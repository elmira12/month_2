import random
def start_geme():
    fruit = ['банан', 'апельсин', 'яблоко', 'инжир', 'айва', 'груша']
    fruits = random.choice(fruit) 
    word_letters = []
    attemprs = 5
    while attemprs > 0:
        hidder_word = ""
        for letter in fruits:
           if letter in word_letters:
                hidder_word += letter
           else:
               hidder_word += "_"

        print(f"Загадонное слова - {hidder_word}")
        print(f"Осталось {attemprs} попыток")

        user = input("Введите букву: ").lower()

        if user in word_letters:
            print(f"Откройте букву: {user}")
            continue
        word_letters.append(user)

        if user not in fruits:
            attemprs -= 1
            print("К сожилению такой буквы нет!!! ")

            if "_" not in hidder_word:
                print("Поздравляю вы выиграли")
                break

        if attemprs == 0:
            print(f"Загадонное слова - ({fruits})")
            print("Вы проиграли")