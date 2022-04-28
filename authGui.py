from tkinter import *
from pythonClient import login,logout



class LogHourForm:

    def __init__(self):
        self.loggedIn = []	

        # Make a tkinter form for registering users using username and pin
        # Display a sucess message if the user is registered else display failure message
        window = Tk()
        window.title("Log Hours")
        window.geometry("500x500")

        window.bind("<Return>",lambda x: self.chooser())

        self.msg = Label(window)
        self.msg.grid(row=5, column=1)


        # Make a label for pin
        lbl_pin = Label(window, text="Pin")
        lbl_pin.grid(column=0, row=0)


        # Make a textbox for pin
        self.pin = Entry(window, width=10)
        self.pin.grid(column=1, row=0)


        btn_submit = Button(window, text="Submit", command=self.chooser)
        btn_submit.grid(column=1, row=4)

        window.mainloop()

    def loginUser(self,pin):
        self.msg.configure(text=login(pin))

    def logOutUser(self,pin):
        self.msg.configure(text=logout(pin))

    def chooser(self):

        pinLog = self.pin.get()
        
        if pinLog in self.loggedIn:
            self.logOutUser(pinLog)
            self.pin.delete(0,END)
        else:
            self.loginUser(pinLog)
            self.loggedIn.append(pinLog)
            self.pin.delete(0,END)


# Start the application
LogHourForm()


