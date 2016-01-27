from Tkinter import *

class MainConfig(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.mainUI()

	def mainUI(self):
		self.parent.title("Main Configuration")
		self.pack(fill=BOTH, expand=True)

		# the following is the frame for user input

		# PLC Name label and entry
		self.frame1 = Frame(self)
		self.frame1.pack(fill=X)
		self.label1 = Label(self.frame1, text="PLC Name", width=10)
		self.label1.pack(side=LEFT, padx=5, pady=5)
		self.entry1 = Entry(self.frame1)
		self.entry1.pack(fill=X, padx=5, expand=True)

		# IP address label and entry
		self.frame2 = Frame(self)
		self.frame2.pack(fill=X)
		self.label2 = Label(self.frame2, text="IP Addr", width=10)
		self.label2.pack(side=LEFT, padx=5, pady=5)
		self.entry2 = Entry(self.frame2)
		self.entry2.pack(fill=X, padx=5, expand=True)

		# set up button frames

		# update button 
		self.buttonframe1 = Frame(self)
		self.buttonframe1.pack(fill=X, padx=5, pady=5)
		self.button1 = Button(self.buttonframe1, text="Update") # need to add in command for this button
		self.button1.pack(side=BOTTOM)

		# display button
		self.buttonframe2 = Frame(self)
		self.buttonframe2.pack(fill=X, padx=5, pady=5)
		self.button2 = Button(self.buttonframe2, text="Display") # need to add in command for this button
		self.button2.pack(side=BOTTOM)


def main():
	root = Tk()
	MainConfig(root)
	root.mainloop()

if __name__ == "__main__":
	main()