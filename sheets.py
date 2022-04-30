from os.path import exists
import datetime
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
import gspread_formatting



class sheets:
    def __init__(self, sheetName):
        self.sheet = getSpreadsheet(sheetName)
        self.setupSheet(self.sheet)

    def setupSheet(self, sheet):
        setupSheet(sheet)

    def sendHours(self, name, hours):
        sendHours(self.sheet, name, hours)
    def login(self, name):
        login(self.sheet, name)
    def logout(self, name):
        logout(self.sheet, name)

def getSpreadsheet(sheetName):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'AttendanceKey.json', scope)
    client = gspread.authorize(creds)

    # check if sheet exists
    canOpenSheet = False
    try:
        client.open(sheetName).sheet1
        print('opened sheet', sheetName)
        canOpenSheet = True
    except:
        print("could not open sheet", sheetName)
        canOpenSheet = False

    # open and return sheet
    if (canOpenSheet):  # if the sheet exists
        sheet = client.open(sheetName).sheet1
        return sheet
    else:
        print("sheet does not exist or there is error accessing it")
        return None

# first row is "names" second row is "total hours"


def setupSheet(sheet):
    totalNumCols = sheet.col_count
    print("totalNumCols", totalNumCols)

    # insert many new colums until have 365!
    while (totalNumCols < 365):
        try:
            sheet.insert_cols(["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],28)
        except:
            print("error inserting cols but it still works")
        # update col_count
        totalNumCols += 18
        print("totalNumCols", totalNumCols)
        
    

    # create header row
    headerRow = ["Name", "Total Hours","Logged In?"] # total hour summer:
    sheet.update_cell(1, 1, headerRow[0])
    sheet.update_cell(1, 2, headerRow[1])
    sheet.update_cell(1, 3, headerRow[2])

    fmt = gspread_formatting.cellFormat(
        backgroundColor=gspread_formatting.color(1, 0.9, 0.9),
        textFormat=gspread_formatting.textFormat(
            bold=True, foregroundColor=gspread_formatting.color(1, 0, 1)),
        horizontalAlignment='CENTER'
    )
    gspread_formatting.format_cell_range(sheet, '1:1000', fmt)

# row 1 names, row 2 hours

# row 1 names, row 2 hours
# this function finds the row of the name and returns that row
# if the name is not found it creates it and returns the row
def findName(sheet, name):
    # search row 1 for name
    row = 2
    while (True):
        if (sheet.cell(row, 1).value == name):
            return row
        elif (sheet.cell(row, 1).value == "" or sheet.cell(row, 1).value == None):  # if we find a blank row
            sheet.update_cell(row, 1, str(name))  # add name to row
            return row
        row += 1

def sendHours(sheet, name, hours):
    # search row 1 for name
    row = findName(sheet, name)

    # 4th col onward are dates
    col = 4
    todayDate = datetime.datetime.today().strftime("%m/%d/%Y")
    while (True):
        if (sheet.cell(1, col).value == todayDate or sheet.cell(1, col).value == ""or sheet.cell(1, col).value == None):
            sheet.update_cell(1, col, todayDate)
            sheet.update_cell(row, col, str(hours))
            break
        col += 1

    # add hours to row
    #sheet.update_cell(row, 2, str(hours))

#row 3: is logged in
def login(sheet,name):
    row = findName(sheet, name)
    sheet.update_cell(row, 3, "yes")
def logout(sheet,name):
    row = findName(sheet, name)
    sheet.update_cell(row, 3, "no")

# sheetObject = sheets(sheetName)
# sheetObject.sendHours("test", "99")
