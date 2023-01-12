from collections import deque
names = input().split(" ")
players = deque(names)
num = int(input())
counter = 0

while len(players) > 1:
    counter += 1
    name_player = players.popleft()

    if counter == num:
        print(f'Removed {name_player}')
        counter = 0
    else:
        players.append(name_player)

print(f'Last is {players[0]}')