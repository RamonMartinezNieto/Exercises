import random
import numpy as np


dictionaryListCoordenates = {}
dictionaryListDistances = {}


def getListWithRandomValues(numberOfElements):
    for i in range(numberOfElements):
        x = getRandomNumber()
        y = getRandomNumber()
        addListNumber(i,x,y)


def getRandomNumber():
    secure_random = random.SystemRandom()
    return secure_random.uniform(0,1)


def addListNumber(position,x,y):
    dictionaryListCoordenates.update({
        str(position): {
            "x":x,
            "y":y
            }
        })


def calculateDistanceAndCreateList():
    for clave in dictionaryListCoordenates:
        x2 = np.square(dictionaryListCoordenates[clave]["x"])
        y2 = np.square(dictionaryListCoordenates[clave]["y"])
        distance = np.sqrt(x2+y2)
        if(distance <= 1):
            addListNumberDistance(clave,distance)


def addListNumberDistance(position,distance):
    dictionaryListDistances.update({
        str(position): {
            "distance":distance
            }
        })


def calculateNumberPi():
    calculatePi = (4 * len(dictionaryListDistances)) / len(dictionaryListCoordenates)
    return calculatePi


# pi * r2 / (2*r)2
getListWithRandomValues(250)
calculateDistanceAndCreateList()
print(calculateNumberPi())