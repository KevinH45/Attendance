from tkinter import *
from pythonClient import login,logout

def loginUser(pin):
	msg.configure(text=login(pin))

def logOutUser(pin):
    msg.configure(text=logout(pin))

def chooser():
    global pin,loggedIn

    pinLog = pin.get()
    
    if pinLog in loggedIn:
        logOutUser(pinLog)
    else:
        loginUser(pinLog)
        loggedIn.append(pinLog)

global loggedIn
loggedIn = []	

# Make a tkinter form for registering users using username and pin
# Display a sucess message if the user is registered else display failure message
window = Tk()
window.title("Log Hours")
window.geometry("500x500")

msg = Label(window)
msg.grid(row=5, column=1)


# Make a label for pin
lbl_pin = Label(window, text="Pin")
lbl_pin.grid(column=0, row=0)


# Make a textbox for pin
global pin
pin = Entry(window, width=10)
pin.grid(column=1, row=0)


btn_submit = Button(window, text="Submit", command=chooser)
btn_submit.grid(column=1, row=4)

window.mainloop()

