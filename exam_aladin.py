from collections import deque
materials = [int(x) for x in input().split(" ")]
magic = deque([int(x) for x in input().split(" ")])

gifts = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}


while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    sum_ = current_magic + current_material

    if sum_ < 100:
        if sum_ % 2 == 0:
            current_material = current_material * 2
            current_magic = current_magic * 3
            sum_ = current_magic + current_material
        else:
            sum_ = sum_ * 2
    elif sum_ > 499:
        sum_ = sum_ / 2

    if 100 > sum_ > 499:
        continue

    if 100 <= sum_ <= 199:
        gifts["Gemstone"] += 1
    elif 200 <= sum_ <= 299:
        gifts["Porcelain Sculpture"] += 1
    elif 300 <= sum_ <= 399:
        gifts["Gold"] += 1
    elif 400 <= sum_ <= 499:
        gifts["Diamond Jewellery"] += 1

suma1 = 0
suma2 = 0
for k, v in gifts.items():
    if k == "Gemstone":
        if v > 0:
            suma1 += 1
    elif k == "Porcelain Sculpture":
        if v > 0:
            suma1 += 1
    elif k == "Gold":
        if v > 0:
            suma2 += 1
    elif k == "Diamond Jewellery":
        if v > 0:
            suma2 += 1

if suma1 > 1 or suma2 > 1:
    print("The wedding presents are made!")

else:
    print("Aladdin does not have enough wedding presents.")

if magic:
    print(f'Magic left: {", ".join(str(x) for x in magic)}')
if materials:
    print(f'Materials left: {", ".join(str(x) for x in materials)}')

for k, v in gifts.items():
    if v > 0:
        print(f'{k}: {v}')
