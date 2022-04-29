# Attendance


## Running the Program

Run registering program with:
```
python3 registerGui.py
```

Run hour-logging program with: 
```
python3 authGui.py
```

## Install all packages

```
pip install gspread oauth2client gspread_formatting pillow
```


## Setup google sheets intergrations

Download AttendanceKey from google drive into this folder

path: Robot/AttendanceInfo/New Attendance System/AttendanceKey.json

**Do not commit AttendanceKey.json to the repo! this is a private key!**


## Creating a new sheet:

Create a new google sheet and share with the following email: attendance@attendance-188719.iam.gserviceaccount.com

In pythonClient.py change varible sheetName to the name of the sheet you created