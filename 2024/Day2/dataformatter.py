file_path = 'C:/Users/james/GitHub/AdventOfCode/2024/Day2/data.txt'

numbers = []
activeNumArray = []
theSillyArray = []
poppedOnes = 0
m_count = 0
a_count = 0
final_count = 0

with open(file_path, 'r') as file:
    for line in file:
        numbers.append(line.strip())
for line in numbers:
    activeNumArray = [line.split()]
    theSillyArray = []

    for i in range(len(activeNumArray[0])):
        arrayNumber = int(activeNumArray[0][i])
        if i + 1 < len(activeNumArray[0]):
            nextNumber = int(activeNumArray[0][i + 1])
        else:
            nextNumber = None

        plusThree = arrayNumber + 3
        plusTwo = arrayNumber + 2
        plusOne = arrayNumber + 1
        minusOne = arrayNumber - 1
        minusTwo = arrayNumber - 2
        minusThree = arrayNumber - 3

        if (plusThree == nextNumber):
            theSillyArray.append("a3")
        elif (plusTwo == nextNumber):
            theSillyArray.append("a2")
        elif (plusOne == nextNumber):
            theSillyArray.append("a1")
        else:
            if (minusThree == nextNumber):
                theSillyArray.append("m3")
            elif (minusTwo == nextNumber):
                theSillyArray.append("m2")
            elif (minusOne == nextNumber):
                theSillyArray.append("m1")

    print(theSillyArray)

    m_count = 0
    a_count = 0

    if len(theSillyArray) > 0 and (theSillyArray[0] == "a1" or theSillyArray[0] == "a2" or theSillyArray[0] == "a3"):
        for i in range(len(theSillyArray)):
            if theSillyArray[i].startswith("m"):
                m_count += 1
                poppableIndex = i
        if (m_count == 1):
            theSillyArray.pop(poppableIndex)
            print(theSillyArray)
            print("SAFE (Popped)")
        elif (m_count == 0):
            print(theSillyArray)
            print("SAFE (unPopped)")
        else:
            print("UNSAFE")

    if len(theSillyArray) > 0 and (theSillyArray[0] == "m1" or theSillyArray[0] =="m2" or theSillyArray[0] == "m3"):
        for i in range(len(theSillyArray)):
            if theSillyArray[i].startswith("a"):
                a_count += 1
                poppableIndex = i
            if (a_count == 1):
                theSillyArray.pop(poppableIndex)
                print(theSillyArray)
                print("SAFE (Popped)")
            elif (a_count == 0):
                print(theSillyArray)
                print("SAFE (unPopped)")
            else:
                print("UNSAFE")
    