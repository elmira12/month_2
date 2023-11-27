import sqlite3,random

connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clients(
id INTEGER PRIMARY KEY,
name VARCHAR (50) NOT NULL,
surname VARCHAR (80) NOT NULL,
age INTEGER NOT NULL,
email TEXT DEFAULT NULL,
balance DONBLE (8,2),
props VARCHAR (20) NOT NULL,
is_active BOOLEAN DEFAULT FALSE
);
""")

class Bank:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.emali = None
        self.balance = 0
        self.props = None
        self.is_active = False

    def register(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.emali = email
        self.prop = random.randint(1111,9999)
        cursor.execute(f"""INSERT INTO clients (name, surname, age, email, balance, props, is_active)
                       VALUES ('{name}', '{surname}', '{age}', '{email}',  0, {self.prop}, False);""")
        connection.commit()

    def refill(self, amount):
        cursor.execute(f"""UPDATE clients SET balance = balance + {amount} - 5 WHERE email = '{self.emali}'""")
        connection.commit()
        self.balance += amount
        cursor.execute(f"""UPDATE clients SET is_active = True""")
        connection.commit()
    

    def withdrawal(self, amount):
        cursor.execute(f"""UPDATE clients SET balance = balance - {amount} WHERE email = '{self.emali}'""")
        connection.commit()
        self.balance -= amount

    def __str__(self):
        return f"Ваш текущий баланс {self.balance} сом"
    
    def main(self):
        while True:
            print("Выберите действие: ")
            choise = int(input("1-Регистрация, 2-Пополнить баланс, 3-Вывезти деньги, 4-Показать баланс, 0-Выйти \n: "))
            if choise == 0:
                print("Всего доброго!")
                break
            elif choise == 1:
                name = input("Введите ваше имя: ")
                surname = input("Введите вашу фамилию: ")
                age = input("Введите ваш возраст: ")
                email = input("Введите ваш email: ")
                self.register(name, surname, age, email)
            elif choise == 2:
                amount = int(input("Введите сумму для пополнения: "))
                if amount > 1000000:
                    print("Можно пополнить баланс до 1000000")
                else:
                    self.refill(amount)
            elif choise == 3:
                amount = int(input("Введите сумму для снятия: "))
                optima = self.balance - amount
                if optima < 0:
                    print("Вы не можете вывести больше 20 сом: ")
                else:
                    self.withdrawal(amount)
            elif choise == 4:
                print(f"Ваш текущий баланс {self.balance}")
            else:
                print("Ошибка, попробуйте ещё раз")

mbank = Bank()
mbank.main()