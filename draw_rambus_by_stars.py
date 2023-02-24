size = int(input())
for x in range(size):
    space_data = size - x - 1
    stars_data = x + 1
    print(space_data * " " + stars_data * "* ")
for x in range(size - 2, -1, -1):
    space_data = size - x - 1
    stars_data = x + 1
    print(space_data * " " + stars_data * "* ")