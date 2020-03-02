# File for editing the scene file to change the obstacles.

import xml.etree.ElementTree as ET

tree = ET.parse('prototype/prototypeS.xml')
root = tree.getroot()

for child in root.iter("ObstacleSet"):
    print '\n', child.tag, child.attrib
    for child2 in child.iter("Obstacle"):
        print child2.tag
        for child3 in child2.iter("Vertex"):
            #print child3.findall("[@p_x]")
            print child3.attrib


# print root[13][0][0]
#
# print root.findall(".")
#print root.findall("./ObstacleSet/Obstacle/Vertex").attrib

#x= root.findall("./ObstacleSet[@type='explicit']/Obstacle[2]//Vertex[1]@p_x")

print root.findall("./ObstacleSet/Obstacle/Vertex//*[@p_x]")

print root.findall(".//Vertex//p_x")
