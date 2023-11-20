# Множественное наследование и Магические методы

# class Parents:
#     def __init__(self, name, color_eyes):
#         self.name = name
#         self.color_eyes = color_eyes 

#     def __str__(self):
#         return f"{self.name}, {self.color_eyes}"

# class Father(Parents):
#     def __init__(self, name, color_eyes, power):
#         Parents.__init__(self, name, color_eyes)
#         self.power = power

#     def work(self):
#         print("Работа")

#     def __str__(self):
#         return super().__str__() + f" сила по 10-шкале {self.power}"
    
# dad = Father("Ким", "Черные", 10)
# print(dad)

# class Mother(Parents):
#      def __init__(self, name, color_eyes, beauty):
#          Parents.__init__(self, name, color_eyes)
#          self.beauty = beauty

#      def cook(self):
#          print("Готовка")

#      def __str__(self):
#         return super().__str__() + f" Внешность по 10-шкале {self.beauty}"
     
# mom = Mother("Лиса", "Карие", 10)
# print(mom)

# class Child(Father, Mother ):
#     def __init__(self, name, color_eyes, power, beauty):
#         Father.__init__(self, name, color_eyes, power)
#         Mother.__init__(self, name, color_eyes, beauty)
 
#     # def info(self):
#     #     print(f"{self.name}, цвет глаз - {self.color_eyes}, {self.power}, {self.beauty}")

#     def __str__(self):   # print == str
#         return super().__str__()

# child = Child("Тэхён", "Карие", 8, 100)
# print(child)
# # child.info()
# # child.work()
# # child.cook()