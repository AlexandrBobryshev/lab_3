import matplotlib.pyplot as plt
import math
import numpy as np


def changeDataSet(inputFile, OutputFile, inputPoint, angle):

    fIn = open(inputFile, 'r')
    line = fIn.readline()

    listOfNewX = []
    listOfNewY = []

    while True:

        line = fIn.readline()
        if not line:
            break
        
        originalPointsCoord = np.array([float(line.split()[0]), float(line.split()[1]), 1])

        matrix = resultMatrix(inputPoint, angle)

        newPointsCoord = np.dot(originalPointsCoord, matrix)
        
        newX = newPointsCoord[0]
        newY = newPointsCoord[1]

        listOfNewX.append(newX)
        listOfNewY.append(newY)
    
    fOut = open(OutputFile, 'w')
    
    for i in range(0, len(listOfNewX)):
        fOut.write(str(listOfNewX[i]) + " " + str(listOfNewY[i]) + " " + str(1) + ('\n'))

    return OutputFile

def resultMatrix(inputPoint, angle):
    
    cos = math.cos(angle)
    sin = math.sin(angle)
    matrix = np.array([[cos, sin, 0], [-sin, cos, 0], [inputPoint[0]*(1-cos)+inputPoint[1]*sin, inputPoint[0]*(1-cos)-inputPoint[0]*sin, 1]])

    return matrix
 
def printPoints(filename):

    f = open(filename, 'r')
    x = []
    y = []
    
    while True:
        line = f.readline()
        if not line:
            break
        x.append(float(line.split()[0]))
        y.append(float(line.split()[1]))
        
    
    plt.rcParams['toolbar'] = 'None'
    plt.figure(figsize=(960/plt.rcParams['figure.dpi'], 960/plt.rcParams['figure.dpi']))
    plt.scatter(x, y)
    plt.axis('off')
    plt.savefig('result.jpg')
    f.close()

point = [480, 480]
alpha = 10*(3+1)*(math.pi/180)

thisFile = "DS3.txt"
newFile = changeDataSet(thisFile, "Changed_DS3.txt", point, alpha)
printPoints(newFile)

