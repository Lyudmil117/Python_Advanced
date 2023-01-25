def multiply(*args):
    num = 1
    for x in args:
        num *= x
    return num


print(multiply(1, 4, 5))
