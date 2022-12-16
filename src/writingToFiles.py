#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 546
# 65000 Óscar Adalberto 
# 65015 Miquelina Josefa


def createHeader(headerDate, headerTime, headerType = "Schedule"):
    """Create a header for a file of type headerType which by default is Schedule, based on the filename and the header date and time 

    """
    header = "Company:\nTagus Sailing\nDay: \n"+headerDate+"\nTime: \n"+headerTime+"\n"+headerType+":\n"
    return header

def writeScheduleFile(schedule, filename, headerTime, headerDate):
    header = createHeader(headerDate, headerTime, "Schedule")
    print(header)
    file = open(filename, "w")
    file.write(header)
    for line in schedule:
        file.write(line+"\n")
    file.close()



def writeSkippersFile(skippers, header, fileName):
    return