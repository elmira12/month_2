# 1
# class Person:
#     def __init__(self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married

#     def introduce_myself(self):
#         print(f"Ф.И - {self.fullname}, возраст - {self.age}, женат(а) - {self.is_married}")

# class Teacher(Person):
#     def __init__(self,fullname, age, is_married, experience):
#         Person.__init__(self,fullname, age, is_married )
#         self.experience = experience
#         self.salary = 30000

#     def sum_salaly(self):
#         for i in range(self.experience):
#             self.salary += 3000
#         print(f"{self.fullname}, ваша зарплата - {self.salary}сом, включая ваш стаж работы {self.experience} года")

# result = Teacher("Молдосакова Эльмира", 16, "нет", 3)
# result.sum_salaly()

