file_path = 'C:/Users/james/GitHub/AdventOfCode/2024/Day1/data.txt'

first_five = []
last_five = []
count = 0
finalValue = 0
totalDistance = 0

with open(file_path, 'r') as file:
    for line in file:
        first_five.append(line[:5])
        last_five.append(line[8:13])

first_five.sort()
last_five.sort()

for i in range (len(first_five)):
    totalDistance += abs(int(first_five[i]) - int(last_five[i]))
    for x in range (len(last_five)):
        if (int(last_five[x]) == int(first_five[i])):
            count += 1

    finalValue += int(first_five[i]) * count
    count = 0

print("(Part 1) The total distance is: " + str(totalDistance))
print("(Part 2) The similarity value is: " + str(finalValue))