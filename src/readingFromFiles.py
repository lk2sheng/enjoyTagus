import constants

#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 546
# 65000 Óscar Adalberto 
# 65015 Miquelina Josefa

def teste():
  
    print(readRequestsFile("./data/testSet1/requests17h00.txt"))



def removeHeader (fileName):
    file = open(fileName, "r")
    filecontent = file.readlines()
    for x in range(constants.NUM_HEADER_LINES):
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

    return skippersList

def readRequestsFile(fileName):
    """
    Reads a file with a list of requested cruises with a given file name into a collection.

    
    """

    inFile = removeHeader(fileName)     

    requestsList = [] 
    for line in inFile:
        requestData = line.rstrip().split(", ")
        requestsList.append(requestData)        

    return requestsList
