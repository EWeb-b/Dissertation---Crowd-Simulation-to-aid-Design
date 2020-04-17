
graphEdges = []
graphVertices = []
testObject = [('3.5', '15.5'), ('7.5', '15.5'), ('7.5', '19.5'), ('3.5', '19.5')]

with open("shoppingStreet/graph.txt") as myfile:
    lines = myfile.readlines()
    numVertices = int(lines[0])
    numEdges = int(lines[numVertices + 1])

    for x, vLine in enumerate(lines[1:numVertices+1]):
        splitLine = vLine.split(' ')
        graphVertices.append((x, float(splitLine[1]), float(splitLine[2].rstrip())))

    for eLine in lines[numVertices + 2:numEdges + 1]:
        splitLine2 = eLine.split(' ')
        graphEdges.append((int(splitLine2[0]), int(splitLine2[1])))

toDelete = []
delVertCount = 0
delEdgeCount = 0
for vertex in graphVertices:
    if (vertex[1] > float(testObject[0][0]) and vertex[2] > float(testObject[0][1]) and vertex[1] < float(testObject[2][0]) and vertex[2] < float(testObject[2][1])):
        print(vertex)
        delVertCount = delVertCount + 1
        toDelete.append(vertex)
        for edge in graphEdges:
            if (edge[0] == vertex[0] or edge[1] == vertex[0]):
                print (edge)
                if (edge not in toDelete):
                    delEdgeCount = delEdgeCount + 1
                    toDelete.append(edge)
print (numEdges)
print (toDelete)
print (delVertCount, delEdgeCount)

#print(graphVertices)
