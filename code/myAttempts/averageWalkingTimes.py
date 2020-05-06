# File for calculating the average time it takes an agent to walk the length
# of the shopping street.
# Uses some of the functionality present in MengeUtils.
import numpy as np
import sys
import pylab as plt
import os
import errno
from MengeUtils.trajectory.scbData import FrameSet
from MengeUtils.trajectory.scbData import NPFrameSet
from MengeUtils.domains import RectDomain

def main(scbFileName):
    frameSet = NPFrameSet(scbFileName)
    bigRect = RectDomain( (0.5, -1.0), (99.5, 40.0))
    timeStep = frameSet.simStepSize
    walkDataList = []
    allowed = [2.0, 3.0]
    countDNF = 0
    totalNumFrames = frameSet.totalFrames()
    frameSet.setNext( 0 )
    inRegion = {}   # map from the agent id to the time it entered

    enterPt = np.empty( ( frameSet.agentCount(), 2 ), dtype=np.float32 )

    while ( True ):
        try:
            frame, idx = frameSet.next()
        except StopIteration:
            break
        IDs = frameSet.getFrameIds()  # a mapping from frame ID to frameSet ID
        posData = frame[:, :2 ]
        BFSMStateData = frame[:, 3]
        isInside = bigRect.pointsInside( posData )
        for fID, state in enumerate( isInside ):
            simID = IDs[ fID ]
            if ( state ):
                if ( not inRegion.has_key( simID ) and BFSMStateData[fID] in allowed and (posData[fID, 0] < 1.0 or posData[fID, 0] > 99.0)):
                    inRegion[ simID ] = idx
                    enterPt[ simID, : ] = posData[ fID, : ]

            else:
                if ( inRegion.has_key( simID ) and BFSMStateData[fID] in allowed):
                    enter = inRegion.pop( simID ) * timeStep
                    if (enter == 0): continue
                    elapsed = (idx * timeStep) - enter
                    exit = posData[ fID, : ]
                    delta = exit - enterPt[ simID, : ]
                    distSq = np.dot( delta, delta )
                    sqrtDistance = np.sqrt(distSq)
                    if (sqrtDistance > 90.0 and elapsed > 65):
                        aveSpeed = sqrtDistance / elapsed
                        walkDataList.append([ enter, elapsed, sqrtDistance, aveSpeed ])

            if (idx == totalNumFrames-1):
                if (simID in inRegion):
                    enter = inRegion.pop(simID) * timeStep
                    elapsed = (idx * timeStep) - enter
                    if (elapsed > 105):
                        countDNF = countDNF + 1
                        exit = posData[ fID, : ]
                        delta = exit - enterPt[ simID, : ]
                        distSq = np.dot( delta, delta )
                        sqrtDistance = np.sqrt(distSq)
                        aveSpeed = sqrtDistance / elapsed
                        walkDataList.append([ enter, elapsed, sqrtDistance, aveSpeed])

    walkDataArray = np.array(walkDataList)
    if walkDataArray.size is 0:
        raise ValueError, "No walking data available. You might need to run the simulation for longer."

    numAgents = len(walkDataArray)
    percentDNF = (float(countDNF) / numAgents) * 100
    aveWalkTime = np.mean(walkDataArray, axis=0)[1]

    print ("Data collected for %d agents. Average time to walk street = %.2fs. Number of successful agents = %d." +
                "Number of agents who did not make it across = %d. Percentage of whole = %.2f%%."
                    % (numAgents, aveWalkTime, numAgents - countdDNF, countDNF, percentDNF))
    return walkDataArray, aveWalkTime


def plotWalkingData(data, aveWalkTime, folderName):

    try:
        os.makedirs(folderName)
        print("Creating folder %s to put graphs in." % folderName)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    print ("Plotting walking graph distance vs. time.")
    plt.title('Walking The Whole Street - Distance vs. Time')
    plt.plot(data[:,1], data[:,2], 'o')
    plt.xlabel('Time taken (s)')
    plt.ylabel('Distance travelled (m)')
    ax = plt.gca()
    plt.text(0.75, 0.9,'Average Walk Time = %.2fs' % aveWalkTime,
                 horizontalalignment='center',
                 verticalalignment='center',
                 transform = ax.transAxes)
    plt.savefig(folderName + '/walk_dist_time.png')
    plt.clf()
    print ("Done.")

    print("Plotting walking graph speed vs. time.")
    plt.title('Walking The Whole Street - Speed vs. Time')
    plt.plot(data[:,1], data[:,3], 'o')
    plt.xlabel('Time taken (s)')
    plt.ylabel('Average Speed (m/s)')
    ax = plt.gca()
    plt.text(0.75, 0.9,'Average Walk Time = %.2fs' % aveWalkTime,
                 horizontalalignment='center',
                 verticalalignment='center',
                 transform = ax.transAxes)
    plt.savefig(folderName + '/walk_speed_time.png')
    plt.clf()
    print ("Done.")

if __name__ == '__main__':
    if len(sys.argv) is not 3:
        raise IOError(errno.E2BIG, os.strerror(errno.E2BIG),
                        "Usage: python averageWalkingTimes.py scbFileName.scb outputFileName")
    scbFileNameArg = str(sys.argv[1])
    workFolderNameArg = str(sys.argv[2])
    data, aveTime = main(scbFileNameArg)
    plotWalkingData(data, aveTime, workFolderNameArg)

## TESTING : ASSERT that speed * elapsed = distance
