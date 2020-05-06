# File to delete and replace the existing obstacles XML for the new random obstacles XML

# First delete the random obstacles already there
def delObsXML():
    startMarker = '<!-- Start delete -->'
    endMarker = '<!-- End delete -->'
    deleteFlag = False
    with open('shoppingStreet/shoppingStreetS.xml', 'r') as f1:
        lines = f1.readlines()
    with open('shoppingStreet/shoppingStreetS.xml', 'w') as f2:
        for line in lines:
            if not deleteFlag:
                deleteFlag = startMarker in line
            else:
                deleteFlag = endMarker not in line
                continue
            if not deleteFlag:
                f2.write(line)

# Now write in the new obstacles
def writeObsXML(obsXML):
    startPoint = '<!-- Start of random obstacles -->'
    endPoint = '<!-- End of random obstacles -->'
    writeFlag = False
    with open('shoppingStreet/shoppingStreetS.xml', 'r') as f3:
        lines = f3.readlines()

    with open('shoppingStreet/shoppingStreetS.xml', 'w') as f4:
        for line in lines:
            f4.write(line)
            if startPoint in line:
                f4.write('\t\t<!-- Start delete -->\n')
                f4.write(obsXML)
                f4.write('\t\t<!-- End delete -->\n')
