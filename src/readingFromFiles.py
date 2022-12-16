import constants as const
import sys
import globals
#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 546
# 65000 Óscar Adalberto 
# 65015 Miquelina Josefa



def removeHeader (fileName):
    file = open(fileName, "r")
    filecontent = file.readlines()

    # Validate header
    nameOfFile = str(fileName).lower() # make sure is lower case so we can compare
    
    # File name must contain the type of file and the time of the file
    typeOfFileInHeader = filecontent[const.NUM_HEADER_LINES-1].rstrip().lower().split(":")[0] # Remove the : and the \n from the file line. Make sure is lower case
    
    headerDate = filecontent[const.NUM_HEADER_LINES-4].rstrip().lower()
    headerTime = filecontent[const.NUM_HEADER_LINES-2].rstrip().lower().replace(":", "h")
    
    # File name must contain the time of the header provided we replace the : with h to match time format
    if( headerTime.replace(":", "h") not in nameOfFile ):
        print ("Error: File " + fileName + " is not valid. The time of the file does not match the header.")
        file.close()
        sys.exit(-1)
    
    # File name must contain the type of file of the header
    if typeOfFileInHeader not in nameOfFile:
        print ("Error: File " + fileName + " is not valid. The name of the file does not match the header.")
        file.close()
        sys.exit(-1)
    
    # The header date must match the date of last RUN. 
    # If last run is empty then safe to assume last run date is the same as the header date of this file
    if( globals.LAST_RUN_DATE == "" ):
        globals.LAST_RUN_DATE = headerDate
        globals.LAST_RUN_TIME = headerTime.replace("h", ":") # Convert back to the time standard format
        globals.CURRENT_RUN_DATE = headerDate
        globals.CURRENT_RUN_TIME = headerTime.replace("h", ":") 
    else:
        if( headerDate != globals.LAST_RUN_DATE or headerTime != globals.LAST_RUN_TIME.replace(":", "h")):
            print ("Error: File " + fileName + " is not valid. The date of the file does not match the last run date " + 
                   globals.LAST_RUN_DATE + ", " + globals.LAST_RUN_TIME + ".")
            file.close()
            sys.exit(-1)    
    
    # Header validated we can now remove the header    
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
            skippersDict[skipper[const.SKIPPER_NAME_IDX]]= {"name": skipper[const.SKIPPER_NAME_IDX], "licenceType": skipper[const.SKIPPER_LICENCE_TYPE], "languages": skipper[const.SKIPPER_LANGUAGES],
                                   "tariff": float(skipper[const.SKIPPER_TARIFF]), "speciality": skipper[const.SKIPPER_SPECIALITY], 
                                   "timeMax": float(skipper[const.SKIPPER_TIME_MAX]), "accumulatedTime": float(skipper[const.SKIPPER_ACCUMULATED_TIME])}
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
   
    return requestsList


def readSchedulesFile (fileName):
    
    inFile = removeHeader(fileName)

    scheduleList = []
    for scheduleRaw in inFile:
        scheduleData = scheduleRaw.rstrip().split(", ")
        scheduleList.append(scheduleData)

    scheduleDict = {}
    for schedule in scheduleList:
        if( schedule != "" ):
            scheduleDict[schedule[const.SCHEDULE_DATE]+"|"+schedule[const.SCHEDULE_TIME]+"-"+schedule[const.SCHEDULE_SKIPPER_NAME]] = \
                        [schedule[const.SCHEDULE_DATE], \
                        schedule[const.SCHEDULE_TIME], \
                        schedule[const.SCHEDULE_DURATION], \
                        schedule[const.SCHEDULE_SKIPPER_NAME], \
                        schedule[const.SCHEDULE_PRICE], \
                        schedule[const.SCHEDULE_CLIENT_NAME]]

    return scheduleDict


