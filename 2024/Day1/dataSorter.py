file_path = 'C:/Users/james/GitHub/AdventOfCode/2024/Day1/data.txt'

first_five = []
last_five = []
totalDistance = 0

with open(file_path, 'r') as file:
    for line in file:
        first_five.append(line[:5])
        last_five.append(line[8:13])

        
first_five.sort()
last_five.sort()

# print("FIRST FIVE:" + str(first_five))
# print("LAST FIVE:" + str(last_five))


for i in range (len(first_five)):
    totalDistance += abs(int(first_five[i]) - int(last_five[i]))

print(totalDistance)