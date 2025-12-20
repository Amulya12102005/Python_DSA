a=int(input())
b=int(input())
try:
    print(a/b)
except ZeroDivisionError:
    print("division by zero")
    print("b cannot be divided by zero")