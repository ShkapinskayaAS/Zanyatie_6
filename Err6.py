try:
    a = input()
    b = int(input())
    print(a[b])
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")