# File for changing the config file which the analyser reads.


def changeConfig(fileName, num):

    # Read the config file
    with open(fileName, 'r') as file:
        lines = file.readlines()

    # Modify the workName line
    lines[6] = lines[6].rstrip() + str(num) + '\n'

    # Write back to file
    with open(fileName, 'w') as file:
        file.writelines(lines)


#changeConfig(r'C:\Users\Ed\Desktop\FinalYearProject\code\myAttempts\prototype\flowConfig.cfg', 1)
