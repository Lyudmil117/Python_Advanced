from collections import deque

quantity = int(input())
orders = deque()
line = list(map(int, (input().split())))

for x in line:
    orders.append(x)
print(max(orders))
while orders:
    order = orders[0]
    if quantity - order >= 0:
        quantity -= order
        orders.popleft()
    else:
        break

if len(orders) == 0:
    print("Orders complete")

if len(orders) > 0:
    print(f'Orders left: {" ".join([str(x) for x in orders])}')