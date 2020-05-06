# This file is for building the random obstacles. Each obstacle is only saved when it
# fits around the existing objects.

import random
from shapely.geometry import Polygon

obs = []

def buildUnit():
    bLX = random.randint(4, 91) - 0.5
    bLY = random.randint(13, 17) - 0.5
    unitPoly = Polygon([(bLX,bLY), (bLX+5,bLY), (bLX+5,bLY+5), (bLX,bLY+5)])
    return unitPoly

def buildBench():
    bLX = random.randint(4, 94) - 0.5
    bLY = random.randint(13, 20) - 0.5
    portrait = random.randint(0,1)
    if portrait is 1:
        benchPoly = Polygon([(bLX,bLY), (bLX+1,bLY), (bLX+1,bLY+2), (bLX,bLY+2)])
    else:
        benchPoly = Polygon([(bLX,bLY), (bLX+2,bLY), (bLX+2,bLY+1), (bLX,bLY+1)])
    return benchPoly

# This function is for making the benches thinner. This is so that there's room in the simulation
# for agents to 'sit' at the benches.
# This is done after the bench positions have been set so that placement doesn't affect the other objects.
def modifyBench(bench):
    b = list(bench.exterior.coords)
    if b[1][0] - b[0][0] == 1.0:
        thinBenchPoly = Polygon([(b[0][0]+0.25,b[0][1]), (b[1][0]-0.25,b[1][1]), (b[2][0]-0.25,b[2][1]), (b[3][0]+0.25,b[3][1])])
        return thinBenchPoly
    elif b[1][0] - b[0][0] == 2.0:
        thinBenchPoly = Polygon([(b[0][0],b[0][1]+0.25), (b[1][0],b[1][1]+0.25), (b[2][0],b[2][1]-0.25), (b[3][0],b[3][1]-0.25)])
        return thinBenchPoly
    else:
        return bench

# Function which returns false when the proposed location of an obstacle isn't feasible,
# such as if it touches/intersects/overlaps with any existing ones.
# If the position is valid, the obstacle is saved and this function returns True.
def isValidPlacement(current):
    if not obs:
        obs.append(current)
        return True
    else:
        for existing in obs:
            if current.touches(existing) or current.intersects(existing) or current.overlaps(existing):
                return False
        obs.append(current)
        return True

# Simple function to convert the obstacles into XML format.
def convertToXML(obs):
    output = ''
    for ob in obs:
        listForm = list(ob.exterior.coords)
        output += '<Obstacle closed="1">'
        output += '\n\t<Vertex p_x="%f" p_y="%f" />' % (listForm[0][0], listForm[0][1])
        output += '\n\t<Vertex p_x="%f" p_y="%f" />' % (listForm[1][0], listForm[1][1])
        output += '\n\t<Vertex p_x="%f" p_y="%f" />' % (listForm[2][0], listForm[2][1])
        output += '\n\t<Vertex p_x="%f" p_y="%f" />' % (listForm[3][0], listForm[3][1])
        output += '\n</Obstacle>\n'
    return output

# Main function which attempts to build the number of benches and units specified when
# called. While loops are used so that the routine to find an obstacle's position is repeated
# until a valid placement is found.
def constructObs(unitCount, benchCount):
    print ("Constructing Obstacles...")
    for x in xrange(unitCount):
        # print ("Building Unit %d..." % (x+1))
        repeat = True
        unit = buildUnit()
        while (repeat is True):
            if not isValidPlacement(unit):
                unit = buildUnit()
            else:
                # print ('\tUnit %d placed successfully.' % (x+1))
                repeat = False
    for y in xrange(benchCount):
        # print ("Building Bench %d..." % (y+1))
        repeat = True
        bench = buildBench()
        while (repeat is True):
            if not isValidPlacement(bench):
                bench = buildBench()
            else:
                # print ('\tBench %d placed successfully.' % (y+1))
                repeat = False
    print ("Finished constructing obstacles.")
    for x, ob in enumerate(obs):
        if x > unitCount - 1:
            obs[x] = modifyBench(obs[x])

    return obs
