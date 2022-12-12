import readingFromFiles, constants as const
import random
import sys

skippersDict = {}

def getMatchingSkipper(availableSkippers, licenceType, language, speciality, requestTime):
#funcao para unir condutor e o cliente
    matchedSkippers = []
    for skipperName in availableSkippers:
        skipper = skippersDict[skipperName]
        if skipperSpeaksLanguage(skipper["languages"], language) and skipper["licenceType"] == licenceType and skipper["speciality"] == speciality and skipper["timeMax"] >= requestTime + skipper["accumulatedTime"]:
            matchedSkippers.append(skipperName)
    
    if len(matchedSkippers) != 0:
        skipperIdx=random.randint(0, len(matchedSkippers)-1)
        return matchedSkippers[skipperIdx]
    else:
        return None

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
    skippersDict = readingFromFiles.readSkippersFile("./data/testSet1/skippers17h00.txt")
    schedules = readingFromFiles.readSchedulesFile("./data/testSet1/schedule17h00.txt")
    requests = readingFromFiles.readRequestsFile("./data/testSet1/requests17h00.txt")


    # For each request
    for request in requests:
        # Compute the matching skipper for the request criteria
        matchedSkipper = getMatchingSkipper(skippersDict,   request[const.REQUEST_SKIPPER_LICENCE_TYPE], 
                                                            request[const.REQUEST_CLIENT_LANGUAGES], 
                                                            request[const.REQUEST_SPECIALITY_TYPE], 
                                                            float(request[const.REQUEST_CRUISE_TIME]))
        print(matchedSkipper)
        # Update the schedule
        updateSchedule(skipperDict[matchedSkipper], request)
        # Update the skipper
        updateSkipper()
    


""""
MAIN PROGRAM
"""

# Read command line arguments ~, va,idate file names and return List of file. [0]is skypperfile, [2]is reuestsfile, [2]is schedulefile
filesList = readCommandLineArguments(sys.argv)

assign(filesList[0], filesList[1], filesList[2])

# Save output files (new schedules, new skippers) 