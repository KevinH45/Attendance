import datetime as dt
from csv import writer, DictReader
import sheets
import localStorage


useLocalStorage = False
try:
    sheetName = "AttendanceOffSeason2022"
    sheetObject = sheets.sheets(sheetName)
except ValueError:
    useLocalStorage = True

global tempHour
tempHour = {
    # 'pin': loginTime
}

def login(pin):
    user = getUserFromPin(pin)

    if user is None:
        return "Invalid Pin"
    else:
        sheetObject.login(user)
        tempHour[pin] = dt.datetime.now()
        return "Logged in "+user+" at "+str(tempHour[pin])

def logout(pin, ignoreHours=False):
    if ignoreHours:
        user = getUserFromPin(pin)

        if user is None:
            return ""
        else:
            sheetObject.sendHours(user,0)
            tempHour.pop(pin)
            return ""
    else:
        user = getUserFromPin(pin)

        if user is None:
            return "Invalid Pin"
        else:
            try:
                
                currentSeconds = (dt.datetime.now() - tempHour[pin]).total_seconds()

                if not useLocalStorage:
                    sheetObject.logout(user)
                    sheetObject.sendHours(user ,round(currentSeconds/3600,2))
                else: 
                    localStorage.sendHours(user, round(currentSeconds/3600,2))
                tempHour.pop(pin)
            except KeyError:
                return "Not logged out, you are not logged in"
            return "Logged out "+user+" at "+str(dt.datetime.now())




def getUserFromPin(pin):
    '''
    Returns the name of the user from the pin
    Returns None if the pin is not found
    '''

    with open('pins.csv','r') as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            if row['pin'] == pin:
                return row['name']

    return None

def register(name,pin):
    try:
        with open('pins.csv','a') as file:
            csv_writer = writer(file)
            csv_writer.writerow([pin,name])
        return "Registered "+name
    except Exception as e:
        print(e)
        return "Error in registering: "+e


