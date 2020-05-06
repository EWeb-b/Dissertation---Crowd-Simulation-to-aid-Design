# File to delete and replace the existing goals for the random obstacles

# First delete the display and bench goals already there
def delGoalsXML():
    startMarker = '<!-- Start delete -->'
    endMarker = '<!-- End delete -->'
    deleteFlag = False
    with open('shoppingStreet/shoppingStreetB.xml', 'r') as f1:
        lines = f1.readlines()
    with open('shoppingStreet/shoppingStreetB.xml', 'w') as f2:
        for line in lines:
            if not deleteFlag:
                deleteFlag = startMarker in line
            else:
                deleteFlag = endMarker not in line
                continue
            if not deleteFlag:
                f2.write(line)

# Now write in the new goals
def writeGoalsXML(goalsXML):
    startPoint = '<!-- Start of display and bench goals -->'
    endPoint = '<!-- End of display and bench goals -->'
    writeFlag = False
    with open('shoppingStreet/shoppingStreetB.xml', 'r') as f3:
        lines = f3.readlines()

    with open('shoppingStreet/shoppingStreetB.xml', 'w') as f4:
        for line in lines:
            f4.write(line)
            if startPoint in line:
                f4.write('\t\t<!-- Start delete -->\n')
                f4.write(goalsXML)
                f4.write('\n\t\t<!-- End delete -->\n')
