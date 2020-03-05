# File for calculating the score of a layout.
# Done using the equation score(s) = |Pa|/tAve, where:
#   Pa is the set of agents who made it to the goal before the time limit.
#   tAve is the average time each agent took.
# Agents who are unsuccesful are assigned the time limit as their time.

import math

timeLimit = 300
dataFile = r'C:\Users\Ed\Desktop\FinalYearProject\code\myAttempts\flow\firstTest\firstTest.flow'
data = []
agentTimes = []

def calcScore(fileName):
    sucAgents = 0
    sTime = 0
    with open(fileName, 'r') as file:
        lines = file.readlines()

    for line in lines:
        data.append(line.split())

    numAgents = int(data[-1][1])

    for x, thisData in enumerate(data[1:]):
        if int(thisData[1]) > sucAgents:
            for i in xrange(int(thisData[1]) - sucAgents):
                agentTimes.append(thisData)
                sTime += int(thisData[0])
            sucAgents += int(thisData[1]) - sucAgents

    print 'sucAgents' + str(sucAgents)
    print agentTimes

    numUnsucAgents = numAgents - int(data[-1][1])

    tAve = float((sTime + numUnsucAgents * timeLimit)/numAgents)
    print 'tAve: ' + str(tAve)
    Pa = sucAgents
    print 'sucAgents: ' + str(Pa)
    score = Pa/tAve
    print 'score: %.4f' % score
    return score

#calcScore(dataFile)
