startY = 25
offsetStartY = 24.5
offsetEndY = 10.5

numRows = 16
numColumns = 101
numPoints = numRows * numColumns
totalEdges = (2*numRows*numColumns) - numRows - numColumns
edgeList = []

def writePoints():
        f.write(str(numPoints) + '\n')
        pointID = 223
        for i in range(numColumns):
            for k in range(numRows):
                firstOrLast = 1

                #first or last column
                if (i == 0 or i == numColumns -1):
                    firstOrLast = 0
                    if (k == 0 or k == numRows - 1):
                        numConns = 2
                    else:
                        numConns = 3

                if (firstOrLast == 1):
                    if (k == 0 or k == numRows - 1):
                        numConns = 3
                    else:
                        numConns = 4

                xPos = i
                yPos = startY - k
                if (k == 0):
                    yPos = offsetStartY
                elif (k == numRows - 1):
                    yPos = offsetEndY

                f.write(str(numConns) + ' ' + str(xPos) + ' ' + str(yPos) + '\n')

                if (i < numColumns - 1):
                    if (numConns == 2):
                        edgeList.append(str(pointID) + ' ' + str(pointID + numRows))
                        if (k == 0):
                            edgeList.append(str(pointID) + ' ' + str(pointID + 1))
                    elif (numConns == 3 and i == 0):
                        edgeList.append(str(pointID) + ' ' + str(pointID + numRows))
                        edgeList.append(str(pointID) + ' ' + str(pointID + 1))
                    elif (numConns == 3 and i != 0):
                        edgeList.append(str(pointID) + ' ' + str(pointID + numRows))
                        if (k == 0):
                            edgeList.append(str(pointID) + ' ' + str(pointID + 1))
                    elif (numConns == 4):
                        edgeList.append(str(pointID) + ' ' + str(pointID + numRows))
                        edgeList.append(str(pointID) + ' ' + str(pointID + 1))
                elif (i == numColumns - 1 and k < numRows - 1):
                    edgeList.append(str(pointID) + ' ' + str(pointID + 1))

                pointID = pointID + 1
def writeConnections():
    #with open('testLattice.txt', 'w') as f:
    f.write(str(totalEdges) + '\n')
    print(edgeList)
    for points in edgeList:
        f.write(str(points) + '\n')


with open('testLattice.txt', 'w') as f:
    writePoints()
    writeConnections()
