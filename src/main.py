import readingFromFiles

skippersDict = {}

def getMatchingSkippers(availableSkippers, licenceType, language, speciality, requestTime):
#funcao para unir condutor e o cliente
    for skipperName in availableSkippers:
        skipper = skippersDict[skipperName]
        if skipperSpeaksLanguage(skipper["languages"], language) and skipper["licenceType"] == licenceType and skipper["speciality"] == speciality and skipper["timeMax"] <= requestTime+skipper["accumulatedTime"]:
            return skipper

# Funcao auxiliar para verificar se o driver fala a linguagem necessaria  
def skipperSpeaksLanguage( spokenLanguages, requiredLanguage):
    for l in spokenLanguages:
        for l1 in requiredLanguage:
            if( l == l1):
                return True
    return False

avalableSkippers = ["Ana Amaral","Carlos Santos"]



skippersDict = readingFromFiles.readSkippersFile("./data/testSet1/skippers17h00.txt")

print(getMatchingSkippers(avalableSkippers, "3*", "portuguese", "speed", "10"))


