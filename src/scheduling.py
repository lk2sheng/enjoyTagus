#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 546
# 65000 Óscar Adalberto 
# 65015 Miquelina Josefa
import constants as const
import utils

# Update the skipper. Given the macthed skypper details return a new updated skipper record based on the travel request
def updateSkipper(skipperRecord, request):
    """ TODO: Implement this"""


# Update the schedule. Give the matched skipper details, the request he was just assigned to and the existing schedules
# this function returns the new schedule
def updateSchedule(skippersRecord, request, schedulesDict):
    """
        This function takes the skipper record, the request and the schedules dictionary and 
        returns the updated schedules dictionary
        
    """
    dateTimeOfLastTrip = "01:01:0001|00:00"
    for schedulesKeys in schedulesDict.keys():
        if skippersRecord["name"] == schedulesKeys.split("-")[1]: 
            if utils.biggestDate(schedulesKeys.split("-")[0], dateTimeOfLastTrip) != dateTimeOfLastTrip:
                dateTimeOfLastTrip = schedulesKeys.split("-")[0]
    lastSchedule = schedulesDict[dateTimeOfLastTrip+"-"+skippersRecord["name"]]
    newTripDateTime = utils.addTimeToDateTime(dateTimeOfLastTrip, lastSchedule[2])
    newSchedule = []
    newSchedule[const.SCHEDULE_TIME] = newTripDateTime.split("|")[1] #new time 
    newSchedule[const.SCHEDULE_SKIPPER_NAME] = skippersRecord["name"] #skipper name
    newSchedule[const.SCHEDULE_PRICE] = skippersRecord["tariff"] #tariff
    newSchedule[const.SCHEDULE_CLIENT_NAME] = request[const.REQUEST_CLIENT_NAME_IDX] # client name
    newSchedule[const.SCHEDULE_DATE] = newTripDateTime.split("|")[0]#new date
    newSchedule[const.SCHEDULE_DURATION] = request[const.REQUEST_CRUISE_TIME] #new cruise duration duration

    schedulesDict[newSchedule[const.SCHEDULE_DATE]+"|"+newSchedule[const.SCHEDULE_TIME]+"-"+skippersRecord["name"]] = newSchedule

    return schedulesDict


def updateSchedule(skippers, schedule, requests, previousDate, previousHour):
	"""
        Update cruises' schedule assigning the cruises requested given
        to the skippers given taking into account a previous schedule.
	
	Requires:
	skippers is a list of lists with the structure as in the output of
	readingFromFiles.readSkipersFile concerning the previous update time;
	schedule is a list of lists with the structure as in the output of
	readingFromFiles.readScheduleFile concerning the previous update time;
	requests is a list of lists with the structure as in the output of 
	readingFromFiles.readRequestsFile concerning the current update time;
	date is string in format DD:MM:YYYY with the previous update date;
	hour is string in format HH:MN: with the previous update hour;
	Ensures:
	a list of cruises, representing the schedule updated at
	the current update time (= previous update time + 30 minutes),
	assigned according to the conditions indicated in the general specification
	(omitted here for the sake of readability).
	"""



def updateSkippers(skippers, schedule):




