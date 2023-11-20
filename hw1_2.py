#1
# class Fruits:
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight

#     def info(self):
#         print(f"Название фрукта {self.name}, Цвет фрукта {self.color}, Масса {self.weight}")

# fruits = Fruits("banana", "yellow", 300)
# fruits.info()

#2
# class Book:
#     def __init__ (self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def chek_pages(self):
#         if self.pages < 100:
#             return "Это книга тонкая "
#         elif 100 <= self.pages <= 300:
#             return "Это книга средняя"
#         else:
#             return "Это книга толстая "
        
# book = Book("В конце они оба умрут", "qwery", 567)
# print(book.chek_pages())
 
#ДОП
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.current_page = 1 

#     def check_pages(self):
#         if self.pages < 100:
#             return "Эта книга тонкая"
#         elif 100 <= self.pages <= 300:
#             return "Эта книга средняя"
#         else:
#             return "Эта книга толстая"

#     def turn_page(self, page_number):
#         if 1 <= page_number <= self.pages:
#             self.current_page = page_number
#             print(f"Вы на странице {self.current_page}.")
#         else:
#             print("Эта страница не существует в книге.")

# book = Book("В конце они оба умрут", "qwery", 500)
# print(book.check_pages())

# book.turn_page(21) 
# book.turn_page(500)