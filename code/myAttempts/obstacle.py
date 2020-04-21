import sys, random
from shapely.geometry import Polygon
sys.path.insert(1, 'C:/Users/Ed/Desktop/FinalYearProject/code/MengeUtils')
import obst2XML
obs = []


def buildDisplay():
    print ('Building display...')
    bLX = random.randint(10, 90) - 0.5
    bLY = random.randint(14, 16) - 0.5
    displayPoly = Polygon([(bLX,bLY), (bLX+5,bLY), (bLX+5,bLY+5), (bLX,bLY+5)])
    print (list(displayPoly.exterior.coords))
    return displayPoly

def buildBench():
    print('Building bench...')
    bLX = random.randint(10, 90) - 0.5
    bLY = random.randint(14, 19) - 0.5
    portrait = random.randint(0,1)
    if portrait is 1:
        benchPoly = Polygon([(bLX,bLY), (bLX+1,bLY), (bLX+1,bLY+2), (bLX,bLY+2)])
    else:
        benchPoly = Polygon([(bLX,bLY), (bLX+2,bLY), (bLX+2,bLY+1), (bLX,bLY+1)])
    print (list(benchPoly.exterior.coords))
    return benchPoly

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


# def buildBench():
#     print('Building bench...')
#     portrait = random.randint(0,1)
#     if portrait is 1:
#         bLX = random.randint(10, 90) - 0.25
#         bLY = random.randint(14, 19) - 0.5
#         benchPoly = Polygon([(bLX,bLY), (bLX+0.5,bLY), (bLX+0.5,bLY+2), (bLX,bLY+2)])
#     else:
#         bLX = random.randint(10, 90) - 0.5
#         bLY = random.randint(14, 19) - 0.25
#         benchPoly = Polygon([(bLX,bLY), (bLX+2,bLY), (bLX+2,bLY+0.5), (bLX,bLY+0.5)])
#     print (list(benchPoly.exterior.coords))
#     return benchPoly


def isValidPlacement(current):
    print ('isValidPlacement start')
    if not obs:
        print ('obs is empty')
        obs.append(current)
        return True
    else:
        for existing in obs:
            if current.touches(existing) or current.intersects(existing) or current.overlaps(existing):
                print ('***NOT VALID PLACE***')
                return False
        print ('Valid place found!')
        obs.append(current)
        return True

def writeOut(total):
    s = str(total) + '\n'
    for ob in obs:
        listForm = list(ob.exterior.coords)
        for x in xrange(4):
            s += str((listForm[x][0])) + ' ' + str((listForm[x][1]))
            s += ' ' + str((listForm[x+1%4][0])) + ' ' + str((listForm[x+1%4][1])) + '\n'
        s += '\n'
        print ('S IS: ')
        print(s)
    with open("temp.txt", "w") as f:
        f.write(s)
    xml = obst2XML.convert("temp.txt")
    print (xml)
    return xml

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

def constructObs(displayCount, benchCount):
    for x in xrange(displayCount):
        repeat = True
        display = buildDisplay()
        while (repeat is True):
            if not isValidPlacement(display):
                display = buildDisplay()
            else:
                print ('no probs found\n')
                repeat = False
    for y in xrange(benchCount):
        repeat = True
        bench = buildBench()
        while (repeat is True):
            if not isValidPlacement(bench):
                bench = buildBench()
            else:
                print ('no probs found\n')
                repeat = False

    for x, ob in enumerate(obs):
        if x > displayCount - 1:
            obs[x] = modifyBench(obs[x])
    return obs
    #return writeOut(displayCount + benchCount)
    #return convertToXML()
