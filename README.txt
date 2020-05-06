
***Installation***

The program is written in Python 2.7 and as such will need to be run in an appropriate environment.
The required external libraries can be found in the requirements.txt file.

Menge will need to be installed and built if the included build does not work on your system.
Instructions on how to do so can be found here: https://github.com/MengeCrowdSim/Menge

    IF you needed to install Menge:
      make sure that the 'Menge-master' directory is on the same level as the 'project' directory this README file is in.

The MengeUtils library of Python functions is included in this folder, in the 'MengeUtils' subdirectory.
I do not make any claim as to their creation - they are included here for ease of use.


***Usage***

main.py can be run via the command line command of:

    python main.py

This executes one iteration of the workflow. This will execute the Menge crowd simulator on the shoppingStreet/shoppingStreet.xml
file, which specifies the scene file as shoppingStreet/shoppingStreetS.xml and the behaviour file as shoppingStreet/shoppingStreetB.xml.
The simulation will output its agent trajectory data as an scb file.
If the simulation has loaded but appears paused, press the spacebar to un-pause it. The simulation can be stopped at any time by pressing
Ctrl + Q. You can press the H key to see additional commands - they will be printed to the terminal screen.

When the simulator has been terminated by pressing Ctrl + Q, the analysis tools will be run on its scb file.
Firstly, the analysis tools from MengeUtils will be run using performAnalysisTasks.py and their graphs will be saved.
The average walking time for agents to walk the length of the road will be calculated through main.py, calling the averageWalkingTimes.py file.

Afterwards, the modObsGoalsRoadmap.py file will be called by main.py to automatically move the random obstacles and edit the roadmap to fit around them.

This completes one iteration of the main.py workflow. By running main.py again, the simulator will be run using the scene configuration which
was altered by the previous iteration's call to modObsGoalsRoadmap.py.


***Running aspects separately***

performAnalysisTasks.py and averageWalkingTimes.py can be called separately via the command line too. You'll need to supply the path/name of an
scb file and the name of a subdirectory in which to save the graphs:

    performAnalysisTasks.py scbFile<filename> outputFolder<string>
    averageWalkingTimes.py scbFile<filename> outputFolder<string>

modObsGoalsRoadmap.py can also be run separately through the command line by specifying the number of unit and bench obstacles to place, as so:

    modObsGoalsRoadmap.py numUnits<int> numBenches<int>

The Menge simulator itself can also be run separately by first navigating to the Menge-master/Exe directory. Once there it can be run using

    ./menge -p <pathToshoppingStreet.xml>
