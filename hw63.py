import re
P = 2
H = 10
list_numbers = []
sum = 0
multiply = 1
count = 0
while True:
  print("Введите число:", end=' ')
  string = re.sub(r'[^0-9\-]+', '', input())
  if len(string) == 0:
    print(" В строке не обнаружено число")
    continue
  number = int(string)
  list_numbers.append(number)
  if number < P:
    sum += number
  elif number > H:
    multiply *= number
  if P < H:
    if P < number < H:
      count += 1
  else:
    if H < number < P:
      count += 1
  last_namber = list_numbers[len(list_numbers) - 1]
  if last_namber == P or last_namber == H:
    break
print("Сумма:", sum)
print("Произведение:", multiply)
print("Количество чисел в диапозоне P и H:", count)
