#Полиморфизм и Инкапсуляция

# class Amimal:
#     def __init__(self, name, color):
#         self.name = name 
#         self.color = color
#         self.age = 0

#     def info_about_amimal(self):
#         print(f"Имя - {self.name}, цвет - {self.color}")

#     def speak(self):
#         pass


# class Dog(Amimal):
#     def __init__(self, name, color):
#         Amimal.__init__(self, name, color)

#     def speak(self):
#         print("Gaf-Gaf")

# class Cat(Amimal):
#     def __init__(self, name, color):
#         Amimal.__init__(self, name, color)

#     def speak(self):
#         print("Meow")

# class Cow(Amimal):
#     def __init__(self, name, color):
#         Amimal.__init__(self, name, color)

#     def speak(self):
#         print("Moo")

# dog = Dog("Sharik", "Black")
# cat = Cat("Murzik", "Milkyway")
# cow = Cow("Murka", "Brown")

# dog.speak()
# cat.speak()
# cow.speak()

# class Toys:
#     def __init__(self):
#         pass

#     def play(self):
#         pass

# class CarToys(Toys):
#     def __init__(self):
#         print("Едет")

#     def play(self):
#         pass

# class DollToys(Toys):
#     def __init__(self):
#         pass

#     def play(self):
#         print("Говорить")

# car = CarToys()
# car.play()

# doll = DollToys()
# doll.play()

#  Инкапсуляция

# class SmartPhone:
#     def __init__(self, sim_cards, battery):
#         self.__sim_cards = sim_cards
#         self._battery = battery # Защищенный атрибут

#     def _info(self):
#         print(f"{self.__sim_cards}, {self._battery} - mh")

#     @property
#     def sim_cards(self):
#         return self.__sim_cards
    

#     @sim_cards.setter
#     def sim_cards(self, new_sim_cards):
#         self.sim_cards = new_sim_cards


# mi = SmartPhone(["Beeline", "Tele2"], 5000)
# mi.sim_cards = "O!"
# print(mi.sim_cards)
# mi._info()

# Декораторы
# def dec(func):
#     def write():
#         print("Hello world!")
#         func()
#         print("Bye")
#     return write

# @dec
# def hi():
#     print("Hi")
# hi()