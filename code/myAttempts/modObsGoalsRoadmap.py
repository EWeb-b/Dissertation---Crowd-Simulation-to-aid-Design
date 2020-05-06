import os
import sys
import errno
import modifyRoadmap, modifyObstacles, modifyGoals, replaceObsText, replaceGoalsText


def main(numUnits, numBenches):

    if not isinstance(numUnits, int):
        raise IOError(errno.EINVAL, os.strerror(errno.EINVAL),
                        "Invalid integer entered for the number of units.")
    if not isinstance(numBenches, int):
        raise IOError(errno.EINVAL, os.strerror(errno.EINVAL),
                        "Invalid integer entered for the number of benches.")

    if (numUnits > 10):
        raise IOError(errno.EINVAL, os.strerror(errno.EINVAL),
                        "The number of units is too high. Max number 10.")
    if (numBenches > 70):
        raise IOError(errno.EINVAL, os.strerror(errno.EINVAL),
                        "The number of benches is too high. Max number 70.")

    newObstacles = modifyObstacles.constructObs(numUnits, numBenches)
    modifyRoadmap.resetRoadmap()

    obsXML = modifyObstacles.convertToXML(newObstacles)
    replaceObsText.delObsXML()
    replaceObsText.writeObsXML(obsXML)

    goalsXML = modifyGoals.placeNewGoals(newObstacles, numUnits , numBenches)
    replaceGoalsText.delGoalsXML()
    replaceGoalsText.writeGoalsXML(goalsXML)

    modifyRoadmap.calculateRoadmap(newObstacles)

if __name__ == '__main__':
    if len(sys.argv) is not 3:
        raise IOError(errno.EINVAL, os.strerror(errno.EINVAL),
                        "Usage: python moveObsAndRoadMap.py numUnits<int> numBenches<int>")
    numUnits = int(sys.argv[1])
    numBenches = int(sys.argv[2])
    main(numUnits, numBenches)
