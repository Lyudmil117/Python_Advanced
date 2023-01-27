def numbers(*data1):
    positives = 0
    negatives = 0
    for i in data:
        if i > 0:
            positives += i
        else:
            negatives += i
    print(negatives)
    print(positives)

    if positives > abs(negatives):
        return print("The positives are stronger than the negatives")

    else:
        return print("The negatives are stronger than the positives")


data = [int(x) for x in input().split(" ")]

numbers()