import sys
sys.path.insert(1, 'C:/Users/Ed/Desktop/FinalYearProject/code/MengeUtils')
from graph import *

# Calculates the new roadmap and saves it to the graph.txt file.
# We need to change the roadmap for each set of obstacles so that the agents can move
# around them.
def calculateRoadmap(obs):
    myGraph = Graph()
    myGraph.initFromFile('shoppingStreet/graph.txt')

    obsL = []
    for ob in obs:
        obsL.append(list(ob.exterior.coords))

    repeat = True
    while (repeat == True):
        for vertex in myGraph.vertices:
            for obL in obsL:
                if (vertex.pos[0] > obL[0][0] and vertex.pos[1] > obL[0][1] and vertex.pos[0] < obL[2][0] and vertex.pos[1] < obL[2][1]):
                    myGraph.deleteVertex(vertex)
        repeat = False
        for vertex in myGraph.vertices:
            for obL in obsL:
                if (vertex.pos[0] > obL[0][0] and vertex.pos[1] > obL[0][1] and vertex.pos[0] < obL[2][0] and vertex.pos[1] < obL[2][1]):
                    repeat = True


    with open("shoppingStreet/graph.txt", "w") as f:
       f.write(myGraph.newAscii())

# Replaces the roadmap with the filled lattice, ready for the next set of obstacles.
def resetRoadmap():
    with open ('shoppingStreet/graphCopy.txt', 'r') as copy:
        lines = copy.readlines()
    with open ('shoppingStreet/graph.txt', 'w') as g:
        for line in lines:
            g.write(line)
