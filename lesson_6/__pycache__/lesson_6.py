# Декомпозиция - разделение логики кода по модулям

from calc import add, sun  # точнечный импорт
from test import hello

hello()
print(__name__)

add(7, 9)
sun(11, 17)

from calc import *  # Звездочка - импорт всего содеримого

add(5, 7)
sun(13, 6)

from calc import add as sun
from folder.test import add as mult

sun(3, 3)
mult(3, 3)



