inputdata = open("Day_10_2019.txt", "r")
inputarray = []
input = ""

for line in inputdata:
    inputarray.append(line.rstrip())

def checkAngle(x, y, resultX, resultY, increaseX, increaseY, found):
    x = int(x)
    y = int(y)
    f = found
    #print(x,y, resultX, resultY)
    if x == resultX and y == resultY:
        if found == 1:
            return True
        else:
            return False
    if inputarray[y][x:x+1:] == '#':
        f = f + 1
    #print("increaseX: "+ str(increaseX))
    #print("increaseY: "+ str(increaseY))
    return checkAngle(x + increaseX, y + increaseY, resultX, resultY, increaseX, increaseY, f)

def ggt(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return ggt(a-b, b)
    else:
        return ggt(a, b-a)

def dayTen():
    max = 0
    for centerX in range(0,len(inputarray[0])):
        for centerY in range(0,len(inputarray)):
            if inputarray[centerY][centerX:centerX+1:] == '#':
                #print("Aktuelles Zentrum: Spalte: " + str(centerX) + " Reihe: " + str(centerY))
                tempMax = 0
                for pointX in range(0,len(inputarray[0])):
                    for pointY in range(0,len(inputarray)):
                        if (pointX == centerX and pointY == centerY) or inputarray[pointY][pointX:pointX+1:] == '.':
                            continue
                        increaseX = abs(pointX - centerX)
                        increaseY = abs(centerY - pointY)  
                        g = ggt(increaseY , increaseX)
                        if pointX > centerX:
                            increaseX = increaseX * -1
                        if pointY > centerY:
                            increaseY = increaseY * -1
                        #print(pointX, pointY, centerX, centerY,increaseX,increaseY)
                        if checkAngle(pointX, pointY, centerX, centerY, increaseX/g, increaseY/g, 0):
                            #print(inputarray[pointY][pointX:pointX+1:])
                            #print(pointX, pointY)
                            tempMax = tempMax +1
                                #print("Geschafft?")
                if max < tempMax:
                    max = tempMax
                    #print(tempMax)
                    #print(centerX, centerY)
                #if centerX == 5 and centerY == 8:
    return max

#print(dayTen())  # x = 23; y = 29
#print(max)                      
print("Done")
inputdata.close()