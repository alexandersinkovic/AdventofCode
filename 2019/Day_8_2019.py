
def countnumbers(x):
    counter = 0
    m = 150
    res = 0
    for i in range(0,(int)(len(x)/(25*6))):
        eins = 0
        zwei = 0
        zahlnull = 0
        for j in range(0, 25*6):
            if x[counter:counter+1:] == "1":
                eins += 1
            elif x[counter:counter+1:] == "2":
                zwei += 1
            else:
                zahlnull += 1
            counter += 1
        if m > zahlnull:
            m = zahlnull
            res = eins * zwei        
    print(res)

countnumbers(x)

def decode(x):
    res = ""
    for i in range(0,25*6):
        counter = 0
        while x[i + (25*6*counter):i + (25*6*counter)+1:] == "2":
            counter += 1
        if(x[i + (25*6*counter):i + (25*6*counter)+1:] == "1"):
            res = res+"0"
        else:
            res = res+" "
    for j in range(0, 6):
        print(res[25*j:25*j+25:])

#decode(x)