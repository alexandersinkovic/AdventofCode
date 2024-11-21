
keys = ["x","y","z"]

def applyGravity(moons, velo):
    moons2 = moons.copy()
    for i in moons:
        moons2.pop(i)
        for k in moons2:
            for key in keys:
                if  moons.get(i).get(key) < moons2.get(k).get(key):
                    velo.get(i)[key] += 1
                    velo.get(k)[key] += -1
                elif moons.get(i).get(key) > moons2.get(k).get(key):
                    velo.get(i)[key] += -1
                    velo.get(k)[key] += 1

def applyVelocity(moons, velo):
    for i in moons:
        for key in moons.get(i):
            moons.get(i)[key] += velo.get(i)[key]

def calculateTotalEnergy(moons, velo):
    energy = 0
    for i in moons:
        totalPotential = 0
        totalKinetic = 0
        for j in moons.get(i):
            totalPotential += abs(moons.get(i).get(j))
            totalKinetic += abs(velo.get(i).get(j))
        energy += totalPotential * totalKinetic
    print(energy)

def simulation(moons, velo):
    steps = 0
    while True:
        steps += 1
        #print(steps)
        applyGravity(moons, velo)
        applyVelocity(moons, velo)
        foundNumber = False
        for i in velo:
            if foundNumber:
                break
            for j in velo.get(i):
                if foundNumber:
                    break
                if velo.get(i).get(j) != 0:
                    foundNumber = True
        if not foundNumber:
            print("Result: " + str(steps))
            break
        #for i in moonsArray:
        #    for j in moonsArray.get(i):
        #        print(j, moonsArray.get(i).get(j), velocity.get(i).get(j))    
    #calculateTotalEnergy(moons, velo)

def applyGravityOneVariable(moons, velo):
    moons2 = moons.copy()
    for i in moons:
        moons2.pop(i)
        for k in moons2:
            if  moons.get(i) < moons2.get(k):
                velo[i] += 1
                velo[k] += -1
            elif moons.get(i) > moons2.get(k):                    
                velo[i] += -1
                velo[k] += 1

def applyVelocityOneVariable(moons, velo):
    for i in moons:
        moons[i] += velo[i]

def simulationOneVariable(moons, velo):
    steps = 0
    while True:
        steps += 1
        #print(steps)
        applyGravityOneVariable(moons, velo)
        applyVelocityOneVariable(moons, velo)
        foundNumber = False
        for i in velo:
            if foundNumber:
                break
            if velo.get(i) != 0:
                foundNumber = True
        if not foundNumber:
            print("Result: " + str(steps))
            break


#printExample
#for i in moonsArray:
    #for j in moonsArray.get(i):
        #print(moonsArray.get(i).get(j))

#simulation(moonsArray, velocity)

moonsCopyX = {"a" : -1, "b" : 4, "c" : -14, "d" : 1}
moonsCopyY = {"a" : -4, "b" : 7, "c" : -10, "d" : 2}
moonsCopyZ = {"a" : 0, "b" : -1, "c" : 9, "d" : 17}
veloCopyX = {"a" : 0, "b" : 0, "c" : 0, "d" : 0}
veloCopyY = {"a" : 0, "b" : 0, "c" : 0, "d" : 0}
veloCopyZ = {"a" : 0, "b" : 0, "c" : 0, "d" : 0}

#simulationOneVariable(moonsCopyX, veloCopyX)
#simulationOneVariable(moonsCopyY, veloCopyY)
#simulationOneVariable(moonsCopyZ, veloCopyZ)

print(115807*96526*30212)