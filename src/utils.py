import sys
import os
import constants as const
import globals
import dateTime as dt
from datetime import datetime


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
    skypperfile = sys.argv[1]
    requestsfile = sys.argv[2]
    schedulefile = sys.argv[3]
    print (sys.argv)
    
    for fileArgIndex in range(1, 4):    
        # Check whether a path pointing to a file
        file = sys.argv[fileArgIndex]
        print(file)
        if os.path.isfile(file) != True:
            print("Error: File " + file + " does not exist.")
            sys.exit(-1)
    return (skypperfile, requestsfile, schedulefile)

def init():
    """
    This function initialises the program global variables CURRENT_RUN_DATE, CURRENT_RUN_TIME
    """
    #print the current date and time in the format dd:mm:yyyy|hh:mm
    globals.CURRENT_RUN_DATE = datetime.now().strftime("%d:%m:%Y")
    globals.CURRENT_RUN_TIME = datetime.now().strftime("%H:%M")
    
    currentMinute = int(globals.CURRENT_RUN_TIME.split(":")[1])
    currentHour = int(globals.CURRENT_RUN_TIME.split(":")[0])
    if currentMinute > 30 and currentMinute < 60:
        globals.CURRENT_RUN_TIME = dt.intToTime(currentHour+1, 0)
    else:
        globals.CURRENT_RUN_TIME = dt.intToTime(currentHour, 30)

    
def addHoursToDateTime(dateTime, hours):
    """
        Function adds a time to a datetime.It only adds hours not minutes
        Requires: DateTime in the format "dd:mm:yyyy|hh:mm" and hour is the integer representing the number of hours to add. 
                  Unfortunately no validation is done on the dateTime format after adding the hours as it can be bigger than 24.
                  In that case the date will be wrong
        
    """
    date1 = (dateTime.split("|")[0], dateTime.split("|")[1])
    time1 = (date1[1].split(":")[0], date1[1].split(":")[1])
    
    newHour = dt.hourToInt(time1[0]) + hours
    newHourString = dt.intToTime(newHour, int(time1[1]))
    return date1[0] + "|" + newHourString 



def biggestDate(dateTime1, dateTime2):
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
            return dateTime1
        else:
            return dateTime2
            
