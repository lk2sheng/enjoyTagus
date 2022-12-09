import constants as const

#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 546
# 65000 Óscar Adalberto 
# 65015 Miquelina Josefa

def teste():
  
    print(readSkippersFile("./data/testSet1/skippers17h00.txt"))



def removeHeader (fileName):
    file = open(fileName, "r")
    filecontent = file.readlines()
    for x in range(const.NUM_HEADER_LINES):
        del filecontent[0]
    file.close()
    return filecontent





def readSkippersFile(fileName):
    """
    Reads a file with a list of skippers into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of skippers organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a skipper listed in
    the file fileName (with all the info pieces belonging to that skipper),
    following the order provided in the lines of the file.
    """
    inFile = removeHeader(fileName)

    skippersList = []
    for skipper in inFile:
        skipperData = skipper.rstrip().split(", ")
        skippersList.append(skipperData)
    
    skippersDict = {}
    for skipper in skippersList:
        if( skipper != "" ):
            # Fazer split da linha
            # Adicionar o skipper ao dicionario
            skippersDict[skipper[const.SKIPPER_NAME_IDX]]= {"licenceType": skipper[const.SKIPPER_LICENCE_TYPE], "languages": skipper[const.SKIPPER_LANGUAGES],
                                   "tariff": skipper[const.SKIPPER_TARIFF], "specialities": skipper[const.SKIPPER_SPECIALTIES], 
                                   "timeMax": skipper[const.SKIPPER_TIME_MAX], "accumulatedTime": skipper[const.SKIPPER_ACCUMULATED_TIME]}
    return skippersDict


def readRequestsFile(fileName):
    """
    Reads a file with a list of requested cruises with a given file name into a collection.

    
    """

    inFile = removeHeader(fileName)     

    requestsList = [] 
    for line in inFile:
        requestData = line.rstrip().split(", ")
        requestsList.append(requestData)        
   
   
    requestDict = {}
    for request in requestsList:
        if( request != "" ):
            requestDict[request[const.REQUEST_CLIENT_NAME_IDX]]= {"requestLicenceType": request[const.SKIPPER_LICENCE_TYPE],
                                 "languages": request[const.REQUEST_CLIENT_LANGUAGES],
                                "specialities": request[const.REQUEST_SPECIALITY_TYPE], 
                                   "requestTime": request[const.REQUEST_CRUISE_TIME]}
    return requestDict


teste()