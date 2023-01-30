from collections import deque

ramen = deque([int(x) for x in input().split(", ")]) #posl
customers = deque([int(x) for x in input().split(", ")]) # purv

while ramen and customers:
    current_ramen = ramen.pop()
    current_customer = customers.popleft()

    if current_ramen == current_customer:
        continue

    elif current_ramen > current_customer:
        new_ramen = current_ramen - current_customer
        ramen.append(new_ramen)
        continue
    elif current_customer > current_ramen:
        new_customer = current_customer - current_ramen
        customers.appendleft(new_customer)

ramen = list(ramen)
customers = list(customers)
if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f'Customers left: {", ".join(str(x) for x in customers)}')
else:
    print("Great job! You served all the customers.")
    if ramen:
        print(f'Bowls of ramen left: {", ".join(str(x)for x in ramen)}')

