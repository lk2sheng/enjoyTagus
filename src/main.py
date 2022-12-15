import readingFromFiles
import constants as const

skippersDict = {}
drivers = skippersDict

def getMatchingDrivers(availableDrivers, stars, language, especializaçao, tempo_requesitado):
#funcao para unir condutor e o cliente

    for condutor_pedido in availableDrivers:
        driverStars = drivers[condutor_pedido]["stars"]
        driverEspecializaçao = drivers[condutor_pedido]["especializaçao"]
        driverLanguages = drivers[condutor_pedido]["languages"]
        driverTempo_max = drivers[condutor_pedido]["tempo_max"]
        if(driverSpeaksLanguage(driverLanguages, language) and driverStars == stars and driverEspecializaçao == especializaçao and driverTempo_max <= tempo_requesitado):
            return condutor_pedido

# Funcao auxiliar para verificar se o driver fala a linguagem necessaria  
def driverSpeaksLanguage( spokenLanguages, requiredLanguage):
    for l in spokenLanguages:
        for l1 in requiredLanguage:
            if( l == l1):
                return True
    return False
    
""" availableDrivers = getDriversByDate(2022, 1, 1, 12)
matchingDriver = getMatchingDrivers(availableDrivers, 4, ["English", "French"])
print(matchingDriver)
 """

def readSkippersFromFile ( skippersFileName ): 
    # Ler o ficheiro
    skippersList = readingFromFiles.readSkippersFile(skippersFileName)
    skippersDict = {}

    # Iterar sobre cada linha do ficheiro


mySkipers = readSkippersFromFile ("./data/skippers.txt")
print (mySkipers)

