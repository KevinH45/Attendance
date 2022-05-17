# Attendance
Hour logging program

with Google sheets integration and local backups to prevent data loss

## Running the Program

Run registering program with:
```
python3 registerGui.py
```

Run hour-logging program with: 
```
python3 authGui.py

python3 dataUploader.py

```

## Install all packages

```
pip install gspread oauth2client gspread_formatting pillow
```


## Set up Google Sheets integrations

Download AttendanceKey from google drive into this folder

path: Robot(Students Mentors)/AttendanceInfo/New Attendance System/AttendanceKey.json

**Do NOT push AttendanceKey.json to the repo! this is a private key!**


## Creating a new sheet:

Create a new google sheet and share with the following email: attendance@attendance-188719.iam.gserviceaccount.com

In dataUploader.py change varible sheetName to the name of the sheet you created


## Updating the code

First, in Git BASH:
```git clone https://github.com/Robotiators-888/Attendance.git```

Second, make your changes. 
- pythonClient.py handles the "backend" of the program (login, logout, and register functionality)
- authGui.py and registerGui.py handle the "frontend" of the program (Tkinter GUI)
- dataUploader.py and sheets.py handle the uploading of data from the Python client and the Google sheet
- Streamlit website is on a different repo that can be viewed [here](https://github.com/KevinH45/AttendanceWebsite)
- **DO NOT PUSH AttendanceKey.json ONTO THE GITHUB REPO**

Finally, in Git BASH:

- cd into your directory
- ```git add -A```
-```git commit -m "your message"```
-```git push origin main```

