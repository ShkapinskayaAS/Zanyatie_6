try:
    a=int(input())
    b=int(input())
    c=0

    c=a/b
    print(c)
except ZeroDivisionError:
    print("Делить на ноль нельзя")