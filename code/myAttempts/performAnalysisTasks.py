import os
import errno
import sys
import MengeUtils.AnalysisTask as AnalysisTask
import numpy as np
import pylab as plt

def main(scbFileName, workFolderName):
    currWD = os.getcwd()
    scbFilePath = os.path.join(currWD, scbFileName)
    print(scbFilePath)

    if not os.path.isfile(scbFilePath):
        raise IOError(errno.ENOENT, os.strerror(errno.ENOENT), scbFileName +
                        " Invalid file name. Enter the name of the SCB file you'd like to analyse.")

    print ("Results will be saved to " + os.path.join(currWD, workFolderName))

    # Perform the analysis tasks
    tasks = AnalysisTask.readAnalysisProject(os.path.join(currWD, 'masterConfig.cfg'))
    for task in tasks:
            task.setSCBFile(scbFilePath)
            task.setWorkFolder(os.path.join(currWD, workFolderName))
            task.execute()
    plt.close('all')

if __name__ == '__main__':
    if len(sys.argv) is not 3:
        raise IOError(errno.E2BIG, os.strerror(errno.E2BIG),
                        "Usage: python performAnalysisTasks.py scbFileName.scb outputFileName")
    if len(sys.argv) < 3:
        raise IOError(errno.EINVAL, os.strerror(errno.EINVAL),
                        "Please enter the name of the folder you'd like to save the analysis results to.")
    scbFileNameArg = str(sys.argv[1])
    workFolderNameArg = str(sys.argv[2])
    main(scbFileNameArg, workFolderNameArg)
