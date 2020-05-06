# File for editing the scene file to change the obstacles.
from itertools import izip
import random
import xml.etree.ElementTree as ET

tree = ET.parse('prototype/prototypeS.xml')
root = tree.getroot()
boxCoords = []
h = 5
w = 5

# Read the box's coordinates and store them.
def getBoxCoords():
    for vertex in root.findall('ObstacleSet/Obstacle/[0]Vertex'):
        boxCoords.append( ((vertex.get('p_x')), (vertex.get('p_y'))) )

    return boxCoords

# Change the box's coords and write them to the xml file.
def changeBoxCoords(boxCoords):
    newTopRightCornerX = random.randint(-5, 10)
    newTopRightCornerY = random.randint(-5, 8)

    boxCoords[0] = (newTopRightCornerX, newTopRightCornerY)
    boxCoords[1] = (newTopRightCornerX-w, newTopRightCornerY)
    boxCoords[2] = (newTopRightCornerX-w, newTopRightCornerY-h)
    boxCoords[3] = (newTopRightCornerX, newTopRightCornerY-h)

    print boxCoords
    for x, vertex in enumerate(root.findall('ObstacleSet/Obstacle/[0]Vertex')):
        vertex.set('p_x', str(boxCoords[x][0]))
        vertex.set('p_y', str(boxCoords[x][1]))
    tree.write('prototype/prototypeS.xml')
