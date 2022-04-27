from tkinter import *
from pythonClient import register

def registerUser():
	global username,pin

	user = username.get()
	pinLog = pin.get()
	msg.configure(text=register(user,pinLog))
	

# Make a tkinter form for registering users using username and pin
# Display a sucess message if the user is registered else display failure message
window = Tk()
window.title("Register")
window.geometry("500x500")

msg = Label(window)
msg.grid(row=5, column=1)

# Make a label for username
lbl_username = Label(window, text="Username")
lbl_username.grid(column=0, row=0)	
	
# Make a label for pin
lbl_pin = Label(window, text="Pin")
lbl_pin.grid(column=0, row=1)

# Make a textbox for username
global username
username = Entry(window, width=10)
username.grid(column=1, row=0)

# Make a textbox for pin
global pin
pin = Entry(window, width=10)
pin.grid(column=1, row=1)


btn_submit = Button(window, text="Submit", command=registerUser)
btn_submit.grid(column=1, row=4)




window.mainloop()

