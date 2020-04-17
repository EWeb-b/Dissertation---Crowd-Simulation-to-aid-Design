
graphEdges = []
graphVertices = []
testObject = [('3.5', '15.5'), ('7.5', '15.5'), ('7.5', '19.5'), ('3.5', '19.5')]
toDelete = []
delVertCount = 0
delEdgeCount = 0

with open("shoppingStreet/graph.txt", "r") as myfile:
    lines = myfile.readlines()
    numVertices = int(lines[0])
    numEdges = int(lines[numVertices + 1])

    for x, line in enumerate(lines[1:numVertices+1]):
        splitLine = line.split(' ')
        #splitLine[2] = splitLine[2].rstrip()
        if (float(splitLine[1]) > float(testObject[0][0]) and float(splitLine[2]) > float(testObject[0][1]) and float(splitLine[1]) < float(testObject[2][0]) and float(splitLine[2]) < float(testObject[2][1])):
            print(x)
            print (line)
            toDelete.append(line)
            delVertCount = delVertCount + 1
            for eLine in lines[numVertices + 2:numEdges + 1]:
                splitLine2 = eLine.split(' ')
                #splitLine2[1] = splitLine2[1].rstrip()
                if (int(splitLine2[0]) == x or int(splitLine2[1]) == x):
                    print (splitLine2)
                    print (eLine)
                    if (eLine not in toDelete):
                        toDelete.append(eLine)
                        delEdgeCount = delEdgeCount + 1

with open("shoppingStreet/graph.txt", "w") as f:
    for line in lines:
        if line not in toDelete:
            splitLine3 = line.split(' ')
            if (len(splitLine3) == 1):
                if (int(line) == numVertices):
                    f.write(str(numVertices - delVertCount) + '\n')
                elif (int(line) == numEdges):
                    f.write(str(numEdges - delEdgeCount) + '\n')
            else:
                f.write(line)

print (toDelete)
print (delVertCount, delEdgeCount)
#     for eLine in lines[numVertices + 2:numEdges + 1]:
#         splitLine2 = eLine.split(' ')
#         graphEdges.append((int(splitLine2[0]), int(splitLine2[1])))
#
# toDelete = []
# delVertCount = 0
# delEdgeCount = 0
# for vertex in graphVertices:
#     if (vertex[1] > float(testObject[0][0]) and vertex[2] > float(testObject[0][1]) and vertex[1] < float(testObject[2][0]) and vertex[2] < float(testObject[2][1])):
#         print(vertex)
#         delVertCount = delVertCount + 1
#         toDelete.append(vertex)
#         for edge in graphEdges:
#             if (edge[0] == vertex[0] or edge[1] == vertex[0]):
#                 print (edge)
#                 if (edge not in toDelete):
#                     delEdgeCount = delEdgeCount + 1
#                     toDelete.append(edge)
# print (numEdges)
# print (toDelete)
# print (delVertCount, delEdgeCount)

# if line.strip("\n") in toDelete:



#print(graphVertices)
