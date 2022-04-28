from tkinter import *
from pythonClient import register

class RegisterForm:
	def __init__(self):
		window = Tk()
		window.title("Register")
		window.geometry("500x500")

		self.msg = Label(window)
		self.msg.grid(row=5, column=1)

		# Make a label for username
		lbl_username = Label(window, text="Username")
		lbl_username.grid(column=0, row=0)	
			
		# Make a label for pin
		lbl_pin = Label(window, text="Pin")
		lbl_pin.grid(column=0, row=1)

		# Make a textbox for username
		self.username = Entry(window, width=10)
		self.username.grid(column=1, row=0)

		# Make a textbox for pin
		self.pin = Entry(window, width=10)
		self.pin.grid(column=1, row=1)


		btn_submit = Button(window, text="Submit", command=self.registerUser)
		btn_submit.grid(column=1, row=4)

		window.mainloop()

	def registerUser(self):

		user = self.username.get()
		pinLog = self.pin.get()
		self.msg.configure(text=register(user,pinLog))


# Start the application
RegisterForm()