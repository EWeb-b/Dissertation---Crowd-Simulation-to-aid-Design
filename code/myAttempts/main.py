import obstacle
import modifyGoals
import modifyRoadmap
import replaceObsText
import replaceGoalsText
import imp
import sys
import subprocess
import changeConfig
import calcScore

# TODO: change analysistask.py's main method to shoppingStreet
# make flow config fie forshoppign street

sys.path.insert(1, 'C:/Users/Ed/Desktop/FinalYearProject/code/MengeUtils')
import AnalysisTask

# Run the simulator
subprocess.check_call([r"C:\Users\Ed\Desktop\FinalYearProject\code\Menge-master\Exe\menge.exe",
        "-p", r"C:\Users\Ed\Desktop\FinalYearProject\code\myAttempts\shoppingStreet.xml",
                "-o", r"C:\Users\Ed\Desktop\FinalYearProject\code\myAttempts\shoppingStreet/shoppingStreetSCB.scb"])

# Analyse the flow of the simulation and return the path to the flow file.
# wPath = AnalysisTask.main()
# print 'wpath: ' + wPath

# Calculate the score of the scenario from the flow file.
# score = calcScore.calcScore(wPath)
# print 'Score for ' + wPath + ': %.4f' % score

newObstacles = obstacle.constructObs(4, 26)
modifyGoals.placeNewGoals(newObstacles, 4, 26)
modifyRoadmap.resetRoadmap()

obsXML = obstacle.convertToXML(newObstacles)
replaceObsText.delObsXML()
replaceObsText.writeObsXML(obsXML)

goalsXML = modifyGoals.placeNewGoals(newObstacles, 4 , 26)
replaceGoalsText.delGoalsXML()
replaceGoalsText.writeGoalsXML(goalsXML)

modifyRoadmap.calculateRoadmap(newObstacles)

# Change the analysis output location
# NOTE: could be using something like task.setTaskName( 'lores' ) in AnalysisTask
#changeConfig.changeConfig(r'C:\Users\Ed\Desktop\FinalYearProject\code\myAttempts\prototype\flowConfig.cfg', 1)
