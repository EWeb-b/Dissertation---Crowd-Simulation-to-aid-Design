import imp
import errno
import os
import sys
import subprocess
import averageWalkingTimes
import performAnalysisTasks
import modObsGoalsRoadmap

pedModels = ['helbing', 'pedvo', 'orca', 'zanlungo', 'gcf', 'karamouzas', 'johannson']

if len(sys.argv) != 4:
    raise IOError(errno.EINVAL, os.strerror(errno.EINVAL),
        "Usage: python performAnalysisTasks.py numUnits<int> numBenches<int> pedModel<string>")
numUnits = int(sys.argv[1])
numBenches = int(sys.argv[2])
pedModel = sys.argv[3]
if not isinstance(numUnits, int):
    raise IOError(errno.EINVAL, os.strerror(errno.EINVAL),
                    "Invalid integer entered for the number of units.")
if not isinstance(numBenches, int):
    raise IOError(errno.EINVAL, os.strerror(errno.EINVAL),
                    "Invalid integer entered for the number of benches.")
if (int(sys.argv[1]) > 10):
    raise IOError(errno.EINVAL, os.strerror(errno.EINVAL),
                    "The number of units is too high. Max number 10.")
if (int(sys.argv[2]) > 70):
    raise IOError(errno.EINVAL, os.strerror(errno.EINVAL),
                    "The number of benches is too high. Max number 70.")
if (pedModel not in pedModels):
    raise IOError(errno.EINVAL, os.strerror(errno.EINVAL),
                    "Invalid pedestrian model entered. Options: " + pedModels)

currWD = os.getcwd()
mengePath = (os.path.join(os.path.dirname(currWD), 'Menge-master', 'Exe', 'menge.exe'))
shoppingStreetXMLPath = (os.path.join(currWD, 'shoppingStreet', 'shoppingStreet.xml'))
scbPath = os.path.join(currWD, 'shoppingStreet', 'shoppingStreetSCB.scb')
workPath = os.path.join(currWD, 'analysisResults')

#Run the simulator
subprocess.check_call([mengePath, "-p", shoppingStreetXMLPath, "-o", scbPath, "-m", pedModel])

# Perform the flow lines, density, and fundamental diagrams analyses tasks
performAnalysisTasks.main(scbPath, workPath)

# Calculate the Walking data and plot the graphs
data, aveTime = averageWalkingTimes.main(scbPath)
averageWalkingTimes.plotWalkingData(data, aveTime, workPath)

# Move the random obstacles and adjust the roadmap to fit around them.
modObsGoalsRoadmap.main(numUnits,numBenches)
