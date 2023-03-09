from collections import deque

food_portions = deque([int(x) for x in input().split(", ")])
stamina_potions = deque([int(x) for x in input().split(", ")])
peaks = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza': 70}
climbed_peaks = []
days = 0

while food_portions and stamina_potions:
    if len(climbed_peaks) == 5:
        break
    if not food_portions or not stamina_potions:
        break

        
    food = food_portions.pop()
    stamina = stamina_potions.popleft()
    days += 1
    for current_peak in peaks:
        if food + stamina >= peaks[current_peak]:
            climbed_peaks.append(current_peak)

        else:
            while food_portions and stamina_potions:
                food = food_portions.pop()
                stamina = stamina_potions.popleft()
                days += 1

                if stamina + food >= peaks[current_peak]:
                    climbed_peaks.append(current_peak)
                    break
                else:
                    continue 

if len(climbed_peaks) == 5 and days <= 7:
    print(f'Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if climbed_peaks:
    print('Conquered peaks:')
    print(*climbed_peaks, sep="\n")
