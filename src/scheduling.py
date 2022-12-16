#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 546
# 65000 Óscar Adalberto 
# 65015 Miquelina Josefa
import constants as const
import utils
import globals

# Update the skipper. Given the macthed skypper details return a new updated skipper record based on the travel request
def updateSkipper(skipperRecord, schedule):
   # Add accumulated time to the skipper record
   skipperRecord["accumulatedTime"] += float(schedule[const.SCHEDULE_DURATION])
   # Add last trip from schedule to the skipper record
   skipperRecord["lastTrip"] = schedule[const.SCHEDULE_DATE] + "|" + schedule[const.SCHEDULE_TIME]



# Update the schedule. Give the matched skipper details, the request he was just assigned to and the existing schedules
# this function returns the new schedule
def getNewSchedule(skippersRecord, request, schedulesDict):
    """
        Update the schedule. Give the matched skipper details, the request he was just assigned to and the existing schedules
        this function returns the new schedule
        
    """
    # If no trip has been assigned to this skipper yet, then the new trip will be at the same time as the LAST_RUN_DATE + 1 hour 
    # so we give enough time for the skipper to get to the boat :)
    dateTimeOfLastTrip = utils.addHoursToDateTime(globals.LAST_RUN_DATE+"|"+globals.LAST_RUN_TIME, 1)
    for key in schedulesDict.keys():
        if skippersRecord["name"] == key.split("-")[1]: 
            if utils.biggestDate(key.split("-")[0], dateTimeOfLastTrip) != dateTimeOfLastTrip:
                dateTimeOfLastTrip = key.split("-")[0]
    if( dateTimeOfLastTrip == utils.addHoursToDateTime(globals.LAST_RUN_DATE+"|"+globals.LAST_RUN_TIME, 1)):
        # No trip has been assigned to this skipper yet, create the trip in the schedule assigning it a key
        schedulesDict[dateTimeOfLastTrip+"-"+skippersRecord["name"]] = []
        newTripDateTime = dateTimeOfLastTrip
    else:
        # A trip has been assigned to this skipper, get the last trip and add the cruise duration to it
        lastSchedule = schedulesDict[dateTimeOfLastTrip+"-"+skippersRecord["name"]]
        newTripDateTime = utils.addHoursToDateTime(dateTimeOfLastTrip, int(lastSchedule[2]))
        
    # Now compute the new schedule attributes
    newSchedule = ["","","","","",""]
    newSchedule[const.SCHEDULE_TIME] = newTripDateTime.split("|")[1] #new time 
    newSchedule[const.SCHEDULE_SKIPPER_NAME] = skippersRecord["name"] #skipper name
    newSchedule[const.SCHEDULE_PRICE] = skippersRecord["tariff"] #tariff
    newSchedule[const.SCHEDULE_CLIENT_NAME] = request[const.REQUEST_CLIENT_NAME_IDX] # client name
    newSchedule[const.SCHEDULE_DATE] = newTripDateTime.split("|")[0]#new date
    newSchedule[const.SCHEDULE_DURATION] = request[const.REQUEST_CRUISE_TIME] #new cruise duration duration

    return newSchedule


def updateSkippers(skippers, schedule):
    """wedas """
    return None



