#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 221
# 60253 Hugo Silva 
# 60284 Kaisheng Li
import constants as const
import globals
import dateTime as dt
from operator import itemgetter

def getSortableSchedule (schedulesDict):
    """Gets a schedule that can be sorted by the key. Key is an integer representing the datetime in int format.
       Schedules older than the last run date and time are removed from the schedule"""
       
    sortedScheduleDict = {}
    for scheduleKey in schedulesDict:
        scheduleDateInt = dt.dateToInt(schedulesDict[scheduleKey][const.SCHEDULE_DATE])
        lastRunDateInt  = dt.dateToInt(globals.LAST_RUN_DATE)
        scheduleTimeInt = dt.hourToInt(schedulesDict[scheduleKey][const.SCHEDULE_TIME]) + dt.minutesToInt(schedulesDict[scheduleKey][const.SCHEDULE_TIME])
        lastRunTimeInt  = dt.hourToInt(globals.CURRENT_RUN_TIME) + dt.minutesToInt(globals.CURRENT_RUN_TIME)
       
        # If schedule is before last run date then we can remove from schedule, do nothing and continue to the next key
        if scheduleDateInt < lastRunDateInt:
            continue
        elif scheduleDateInt == lastRunDateInt and scheduleTimeInt < lastRunTimeInt:
            continue

        # Schedule is in the future (i.e bigger than the last rundatetime), we can proceed to sort it
        scheduleString = schedulesDict[scheduleKey][const.SCHEDULE_DATE] + ", " +\
                        schedulesDict[scheduleKey][const.SCHEDULE_TIME]+ ", " + \
                        str(int(schedulesDict[scheduleKey][const.SCHEDULE_DURATION]))+ ", " + \
                        schedulesDict[scheduleKey][const.SCHEDULE_SKIPPER_NAME]+ ", " + \
                        str(int(schedulesDict[scheduleKey][const.SCHEDULE_PRICE]))+ ", " + \
                        schedulesDict[scheduleKey][const.SCHEDULE_CLIENT_NAME]
        
        # In order to sort by date and time we need to create a key that is the sum of the date and time                
        key = dt.dateToInt(schedulesDict[scheduleKey][const.SCHEDULE_DATE]) + dt.hourToInt(schedulesDict[scheduleKey][const.SCHEDULE_TIME])
        sortedScheduleDict[key] = scheduleString
        
    
    return sortedScheduleDict
    
def createHeader(headerDate, headerTime, headerType = "Schedule"):
    """Create a header for a file of type headerType which by default is Schedule, based on the filename and the header date and time 

    """
    header = "Company:\nTagus Sailing\nDay: \n"+headerDate+"\nTime: \n"+headerTime+"\n"+headerType+":"
    return header

def writeScheduleFile(schedule, notAssignedList, filename, headerTime, headerDate):
    """ Save all schedules sorted by date provided that the not assigned List comes first in the file """
    header = createHeader(headerDate, headerTime, "Schedule")
    file = open(filename, "w")
    file.write(header)
    for notAssignedLine in notAssignedList:
        file.write("\n"+notAssignedLine)
        
    sortedSchedule = getSortableSchedule(schedule)
    for key in sorted(sortedSchedule.keys()):
        file.write("\n"+sortedSchedule[key])
    file.close()



def writeSkippersFile(skippers, fileName, headerDate, headerTime):
    """ Save all skipper information in a file """
    
    header = createHeader(headerDate, headerTime, "Skippers")
    file = open(fileName, "w")
    file.write(header)
    for key in skippers:
        skipperDataString = skippers[key]["name"]+", "+skippers[key]["languages"]+", "+ \
                            skippers[key]["licenceType"]+", "+str(int(skippers[key]["tariff"]))+", "+ \
                            skippers[key]["speciality"]+", "+str(int(skippers[key]["timeMax"]))+ ", "+ \
                            str(int(skippers[key]["accumulatedTime"]))+", "+ \
                            "("+skippers[key]["dateLastCruise"]+", "+skippers[key]["timeLastCruise"]+")"
        file.write("\n"+skipperDataString)
    file.close()
