M = 2
list_strings = []
for i in range(0, M):
 print("Введите строку:", end=' ')
 list_strings.append(input())
max_str_len = 0
for str in list_strings:
 str_len = len(str)
if str_len > max_str_len:
 max_str_len = str_len
print("Максимальная длина строки:", max_str_len)
for str in list_strings:
 str_len = len(str)
if str_len < max_str_len:
 for i in range(0, max_str_len - str_len):
  str = '*' + str
print(str)
