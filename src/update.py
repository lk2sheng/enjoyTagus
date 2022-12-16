import readingFromFiles
import constants as const
#import writingToFiles as writter
import random
import utils
import sys
import scheduling

skippersDict = {}

def getMatchingSkipper(availableSkippers, licenceType, language, speciality, requestTime):
#funcao para unir condutor e o cliente
    matchedSkippersName = []
    for skipperName in availableSkippers:
        skipper = availableSkippers[skipperName]
        if skipperSpeaksLanguage(skipper["languages"], language) and skipper["licenceType"] == licenceType and skipper["speciality"] == speciality and skipper["timeMax"] >= requestTime + skipper["accumulatedTime"]:
            matchedSkippersName.append(skipperName)
    
    if len(matchedSkippersName) != 0:
        skipperIdx=random.randint(0, len(matchedSkippersName)-1)
        return matchedSkippersName[skipperIdx]
    else:
        return []

# Funcao auxiliar para verificar se o driver fala a linguagem necessaria  
def skipperSpeaksLanguage(spokenLanguages, requiredLanguage):
    for l in spokenLanguages:
        for l1 in requiredLanguage:
            if( l == l1):
                return True
    return False


def assign(skippersFileName, scheduleFileName, requestsFileName):
    """
    Runs the enjoyTagus application.

    Requires:
    skippersFileName is a str with the name of a .txt file containing a list
    of skippers, organized as in the examples provided;
    scheduleFileName is a str with the name of a .txt file containing a list
    of cruises assigned to skippers as in the examples provided;
    requestsFileName is a str with the name of a .txt file containing a list
    of cruises requested;
    these input files concern the same company, date and time.
    Ensures:
    writing of two .txt files containing the updated list of cruises assigned
    to skippers and the updated list of skippers, according to 
    the requirements in the general specifications provided (omitted here for 
    the sake of readability);
    these two output files are named, respectively, scheduleXXhYY.txt and
    skippersXXhYY.txt, where XXhYY represents the time and date 30 minutes
    after the time and date indicated in the files skippersFileName,
    scheduleFileName and requestsFileName, and are written in the same directory
    of the latter.
    """

    # Read all the files
    # skippersDict = readingFromFiles.readSkippersFile("./data/testSet1/skippers17h00.txt")
    skippersDict = readingFromFiles.readSkippersFile(skippersFileName)
    # schedules = readingFromFiles.readSchedulesFile("./data/testSet1/schedule17h00.txt")
    schedulesDict = readingFromFiles.readSchedulesFile(scheduleFileName)
    # requests = readingFromFiles.readRequestsFile("./data/testSet1/requests17h00.txt")
    requestsList = readingFromFiles.readRequestsFile(requestsFileName)


    # For each request
    for request in requestsList:
        # Compute the matching skipper for the request criteria
        matchedSkipper = getMatchingSkipper(skippersDict,   request[const.REQUEST_SKIPPER_LICENCE_TYPE], 
                                                            request[const.REQUEST_CLIENT_LANGUAGES], 
                                                            request[const.REQUEST_SPECIALITY_TYPE], 
                                                            float(request[const.REQUEST_CRUISE_TIME]))
        if matchedSkipper == []:
            continue

        # Update the schedule. Give the matched skipper details, the request he was just assigned to and the existing schedules
        # this function returns the new schedule
        newSchedule = scheduling.getNewSchedule(skippersDict[matchedSkipper], request, schedulesDict)
        schedulesDict[newSchedule[const.SCHEDULE_DATE]+"|"+newSchedule[const.SCHEDULE_TIME]+"-"+matchedSkipper] = newSchedule
        
        # Update the skipper. Given the macthed skypper details return a new updated skipper record based on the travel request
        scheduling.updateSkipper(skippersDict[matchedSkipper], newSchedule)

    return (skippersDict, schedulesDict)

""""
MAIN PROGRAM
"""

# Read command line arguments
filesList = utils.readCommandLineArguments()

#(newSchedule, newSkippers) = assign(filesList[0], filesList[1], filesList[2])~

## Test with hard codeed files
(skippers, schedules) = assign("./data/testSet1/skippers17h00.txt", 
                                    "./data/testSet1/schedule17h00.txt",
                                    "./data/testSet1/requests17h00.txt")
print(skippers)
print(schedules)

# Save output files (new schedules, new skippers) 
#writter.writeScheduleFile(newSchedule)
#writter.writeSkippersFile(newSkippers)
