import random

def placeBenchGoals(benches):
    output = ''
    output += '\t\t<GoalSet id="5">'
    count = 0
    for bench in benches:
        side = random.randint(0, 1)
        if bench[1][0] - bench[0][0] == 0.5:
            if side is 1:
                output += '\n\t\t\t<Goal capacity="1" id="%d" type="point" weight="1.00" x="%f" y="%f"/>' % (count, bench[0][0]-0.25, bench[0][1]+0.65)
                count = count + 1
                output += '\n\t\t\t<Goal capacity="1" id="%d" type="point" weight="1.00" x="%f" y="%f"/>' % (count, bench[0][0]-0.25, bench[3][1]-0.65)
            elif side is 0:
                output += '\n\t\t\t<Goal capacity="1" id="%d" type="point" weight="1.00" x="%f" y="%f"/>' % (count, bench[1][0]+0.25, bench[0][1]+0.65)
                count = count + 1
                output += '\n\t\t\t<Goal capacity="1" id="%d" type="point" weight="1.00" x="%f" y="%f"/>' % (count, bench[1][0]+0.25, bench[3][1]-0.65)
        elif bench[1][0] - bench[0][0] == 2.0:
            if side is 1:
                output += '\n\t\t\t<Goal capacity="1" id="%d" type="point" weight="1.00" x="%f" y="%f"/>' % (count, bench[0][0]+0.65, bench[0][1]-0.25)
                count = count + 1
                output += '\n\t\t\t<Goal capacity="1" id="%d" type="point" weight="1.00" x="%f" y="%f"/>' % (count, bench[1][0]-0.65, bench[0][1]-0.25)
            elif side is 0:
                output += '\n\t\t\t<Goal capacity="1" id="%d" type="point" weight="1.00" x="%f" y="%f"/>' % (count, bench[0][0]+0.65, bench[3][1]+0.25)
                count = count + 1
                output += '\n\t\t\t<Goal capacity="1" id="%d" type="point" weight="1.00" x="%f" y="%f"/>' % (count, bench[1][0]-0.65, bench[3][1]+0.25)
        count = count + 1
    output += '\n\t\t</GoalSet>'
    return output

def placeDisplayGoals(displays):
    output = ''
    output += '\t\t<GoalSet id="4">'
    count = 0
    for display in displays:
        output += '\n\t\t\t<Goal capacity="8" id="%d" max_x="%f" min_x="%f" max_y="%f" min_y="%f" type="AABB" weight="1.00"/>' % (count, display[1][0]-0.5, display[0][0]+0.5, display[0][1], display[1][1]-0.5)
        output += '\n\t\t\t<Goal capacity="8" id="%d" max_x="%f" min_x="%f" max_y="%f" min_y="%f" type="AABB" weight="1.00"/>' % (count+1, display[1][0]+0.5, display[2][0], display[2][1]-0.5, display[1][1]+0.5)
        output += '\n\t\t\t<Goal capacity="8" id="%d" max_x="%f" min_x="%f" max_y="%f" min_y="%f" type="AABB" weight="1.00"/>' % (count+2, display[1][0]-0.5, display[0][0]+0.5, display[3][1]+0.5, display[2][1])
        output += '\n\t\t\t<Goal capacity="8" id="%d" max_x="%f" min_x="%f" max_y="%f" min_y="%f" type="AABB" weight="1.00"/>' % (count+3, display[0][0], display[0][0]-0.5, display[3][1]-0.5, display[0][1]+0.5)
        count = count + 4
    output += '\n\t\t</GoalSet>'
    return output

def placeNewGoals(newObstacles, numDisplays, numBenches):
    displays = []
    benches = []

    for ob in newObstacles[:numDisplays]:
        displays.append(list(ob.exterior.coords))
    for ob in newObstacles[numDisplays:]:
        benches.append(list(ob.exterior.coords))

    xml = placeDisplayGoals(displays) + '\n' + placeBenchGoals(benches)
    return xml
