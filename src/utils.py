import sys
import constants as const
import dateTime
# Read command line arguments from sys.argv and validate file names and return List of file.
# Executing this program should in the form: python3 update.py inputFile1 inputFile2 inputFile3
# The return List should be the followng
#  [0] - is skypperfile
#  [1] - is requestsfile,
#  [2] - is schedulefile
# If the files do not conform to the file naming standard then the program needs to stop with an error message
def readCommandLineArguments():
    """
    Read command line arguments from sys.argv and validate file names and return List of file.
    Executing this program should in the form: python3 update.py inputFile1 inputFile2 inputFile3
     The return List should be the followng
          [0] - is skypperfile
          [1] - is requestsfile,
          [2] - is schedulefile
        If the files do not conform to the file naming standard then the program needs to stop with an error message
    """
    """TODO: Implement this"""
    return None # TODO: Return a List of files after implementing this function


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
            if BiggestDate(schedulesKeys.split("-")[0], dateTimeOfLastTrip) != dateTimeOfLastTrip:
                dateTimeOfLastTrip = schedulesKeys.split("-")[0]
    lastSchedule = schedulesDict[dateTimeOfLastTrip+"-"+skippersRecord["name"]]
    newTripDateTime = addTimeToDateTime(dateTimeOfLastTrip, lastSchedule[2])
    newSchedule = []
    newSchedule[0] = newTripDateTime.split("|")[1] #new time 
    newSchedule[1] = skippersRecord["name"] #skipper name
    newSchedule[2] = skippersRecord["tariff"] #tariff
    newSchedule[3] = request[const.REQUEST_CLIENT_NAME_IDX] # client name
    newSchedule [4] = newTripDateTime.split("|")[0]#new date
    newSchedule[5] = request[const.REQUEST_CRUISE_TIME] #new cruise duration duration

    schedulesDict[newSchedule[4]+"|"+newSchedule[0]+"-"+skippersRecord["name"]] = newSchedule

    return schedulesDict

# Update the skipper. Given the macthed skypper details return a new updated skipper record based on the travel request
def updateSkipper(skipperRecord, request):
    """ TODO: Implement this"""


def BiggestDate(dateTime1, dateTime2):
    """
    This function takes two dates and times and returns the biggest one.
    Requires: The dates and times to be in the format: dd:mm:yyyy|hh:mm
    
    
    Ensures: When the dates are the same, the function returns one of them
    
    """
    date1 = dateTime1.split("|")[0]
    date2 = dateTime2.split("|")[0]
    day1 = date1.split(":")[0]
    month1 = date1.split(":")[1]
    year1 = date1.split(":")[2]
    day2 = date2.split(":")[0]
    month2 = date2.split(":")[1]
    year2 = date2.split(":")[2]
    time1 = dateTime1.split("|")[1]
    time2 = dateTime2.split("|")[1]
    hour1 = time1.split(":")[0]
    min1 = time1.split(":")[1]
    hour2 = time2.split(":")[0]
    min2 = time2.split(":")[1]

    if date1 == date2 :
        if int ( hour1 + min1 )  >  int( hour2 + min2 ):
            return dateTime1
        else:
            return dateTime2
        
    else:
        if int(year1+month1+day1) > int(""+year2+month2+day2):
            print(int(year1+month1+day1))
            print(int(year2+month2+day2))
            return dateTime1
        else:
            return dateTime2
            


print(BiggestDate("01:12:2023|15:30", "01:12:2023|15:00"))