# Известен объем информации в байтах. Перевести в килобайты, мегабайты.
import math
B = input("Введите количество байт ")
B = int(B)
kB=B/1024
MB=B/(math.pow(2,20))
print("Количество килобайт ", kB)
print("Количество мегабайт", MB)
