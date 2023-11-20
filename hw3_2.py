#1
# class Computer: 
#     def __init__(self, cpu, memory): 
#         self.__cpu = cpu
#         self.__memory = memory


#     @property
#     def cpu(self):
#         return self.__cpu
    
#     @property
#     def memory(self):
#         return self.__memory

#     @memory.setter
#     def memory(self, memory):
#         self.memory == memory
    
    
#     @cpu.setter
#     def cpu(self, cpu):
#         self.cpu == cpu

#     def __make_computations(self):
#         print(f"Результат сложения: {self.cpu + self.memory},результат вычитание: {self.cpu - self.memory}")
#         print(f"результат умножение: {self.cpu * self.memory},результат деление: {self.cpu / self.memory}")

#     @property
#     def make_computations(self):
#         return self.__make_computations 



# class Laptop(Computer):
#     def __init__(self,cpu,memory,memory_card):
#         super().__init__(cpu,memory)
#         self.__memory_card = memory_card
        
    
#     @property
#     def memory_card(self):
#         return self.__memory_card
    
#     def info(self):
#         print(f'у нас {self.cpu} ядер и {self.memory} гб и дополнительно {self.memory_card} гб')

# laptop = Laptop(6,70,46)
# laptop.info()
# laptop.make_computations()