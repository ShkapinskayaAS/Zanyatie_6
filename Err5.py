a = input()
b = int(input())

try:
    print(a[b])
except IndexError:
    print("Нет такого символа")