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
    # create header row
    headerRow = ["Name", "Total Hours"]
    sheet.update_cell(1, 1, headerRow[0])
    sheet.update_cell(1, 2, headerRow[1])
    # add Yellow fill color to header row
    sheet.update_cell(1, 1, "Name")
    sheet.update_cell(1, 2, "Total Hours")

    fmt = gspread_formatting.cellFormat(
        backgroundColor=gspread_formatting.color(1, 0.9, 0.9),
        textFormat=gspread_formatting.textFormat(
            bold=True, foregroundColor=gspread_formatting.color(1, 0, 1)),
        horizontalAlignment='CENTER'
    )
    gspread_formatting.format_cell_range(sheet, '1:1000', fmt)

# row 1 names, row 2 hours


def sendHours(sheet, name, hours):
    # search row 1 for name
    row = 2
    while (True):
        print('search row', row)
        if (sheet.cell(row, 1).value == name):
            sheet.update_cell(row, 2, str(hours))  # add hours to row
            break
        elif (sheet.cell(row, 1).value == "" or sheet.cell(row, 1).value == None):  # if we find a blank row
            sheet.update_cell(row, 1, str(name))  # add name to row
            sheet.update_cell(row, 2, str(hours))  # add hours to row
            break
        row += 1

# sheetObject = sheets(sheetName)
# sheetObject.sendHours("test", "99")