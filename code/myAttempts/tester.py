from shapely.geometry import *
import random
# def doIt(count):
#     for x in xrange(count):
#         print (x)
#
# doIt(4)
# polyList = []
#
# for x in xrange(5):
#     bLX = random.randint(10, 90)
#     bLY = random.randint(14, 21)
#     p = Polygon([(bLX,bLY), (bLX+5,bLY), (bLX+5,bLY+5), (bLX,bLY+5)])
#     print(list(p.exterior.coords))
#     print(list(p.exterior.coords)[0][0])
#     polyList.append(p)
#
#
# s = str(12) + '\n'
# for ob in polyList:
#     listForm = list(ob.exterior.coords)
#     for x in xrange(4):
#         s += str(int(listForm[x][0])) + ' ' + str(int(listForm[x][1]))
#         s += ' ' + str(int(listForm[x+1%4][0])) + ' ' + str(int(listForm[x+1%4][1])) + '\n'
#     s += '\n'
#
# print(s)
#print(p1.intersects(p2))

# listForm = []
# listForm.append((2.0,5.9))
# output = ''
# output += '<Obstacle closed = "1">'
# output += '\n<Vertex p_x="%f" p_y="%f" />' % (listForm[0][0], listForm[0][1])
# print (output)

hello = [0,1,2,3,4,5,6,7,8,9]
displayCount = 3
print (hello)
x = 3
for y, hi in enumerate(hello):
    if y > displayCount - 1:
        hello[y] = hello[y] + 10

print(hello)
