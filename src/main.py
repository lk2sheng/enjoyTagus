import readingFromFiles, constants as const
import random

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



""""
MAIN PROGRAM
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

# Save output files (new schedules, new skippers) 



