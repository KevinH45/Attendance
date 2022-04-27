import datetime as dt
from csv import writer, DictReader

global tempHour
tempHour = {
    # 'pin': loginTime
}

def login(pin):
    user = getUserFromPin(pin)

    if user is None:
        return "Invalid Pin"
    else:
        tempHour[pin] = dt.datetime.now()
        return "Logged in "+user+" at "+str(tempHour[pin])

def logout(pin):
    user = getUserFromPin(pin)

    if user is None:
        return "Invalid Pin"
    else:
        sendToSheet(user,dt.datetime.now()-tempHour[pin])
        tempHour.clear(pin)
        return "Logged out "+user+" at "+str(tempHour[pin])

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
        return True
    except Exception as e:
        print(e)
        return False


def sendToSheet(name,hours):
    return True


register('John',1234)
