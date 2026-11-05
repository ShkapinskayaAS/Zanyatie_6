while True:
    try:
        number = int(input())
        break
    except ValueError:
        print("Это не число, попробуй ещё:")

print(number)