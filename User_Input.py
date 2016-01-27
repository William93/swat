#!/usr/bin/python

from Tkinter import *

class UserInput(Frame):


	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initUI()

	def initUI(self):
		self.choices = ['Constant', 'Variable']
		self.var = StringVar()
		self.var.set('')

		self.parent.title("Sample")
		self.pack(fill=BOTH, expand=True)

		# first frame
		self.frame1 = Frame(self)
		self.frame1.pack(fill=X)

		# first label
		self.label1 = Label(self.frame1, text = "PLC", width = 13)
		self.label1.pack(side = LEFT, padx=5, pady=5)

		# first text field
		self.entry1 = Entry(self.frame1)
		self.entry1.pack(fill=X, padx=5, expand=True)

		self.frame2 = Frame(self)
		self.frame2.pack(fill=X)

		self.label2 = Label(self.frame2, text="IP Address", width = 13)
		self.label2.pack(side=LEFT, padx=5, pady=5)

		self.entry2 = Entry(self.frame2)
		self.entry2.pack(fill=X, padx=5, expand=True)

		self.frame3 = Frame(self)
		self.frame3.pack(fill=X)

		self.label3 = Label(self.frame3, text="Tag Name", width=13)
		self.label3.pack(side=LEFT, padx=5, pady=5)

		self.entry3 = Entry(self.frame3)
		self.entry3.pack(fill=X, padx=5, expand=True)

		self.frame4 = Frame(self)
		self.frame4.pack(fill=X)

		self.label4 = Label(self.frame4, text="Tag Type", width=13)
		self.label4.pack(side=LEFT, padx=5, pady=5)

		self.dropdown = OptionMenu(self.frame4, self.var, *self.choices)
		self.dropdown.pack(side=LEFT, padx=5, pady=5)

		self.frame5 = Frame(self)
		self.frame5.pack(fill=X)
		self.label5 = Label(self.frame5, text="Tag Value", width=13)
		self.label5.pack(side=LEFT, padx=5, pady=5)

		self.entry5 = Entry(self.frame5)
		self.entry5.pack(fill=X, padx=5, expand=True)

		self.frame6 = Frame(self)
		self.frame6.pack(fill=X)
		self.label6 = Label(self.frame6, text="Maximum Value", width=13)
		self.label6.pack(side=LEFT, padx=5, pady=5)

		self.entry6 = Entry(self.frame6)
		self.entry6.pack(fill=X, padx=5, expand=True)

		self.frame7 = Frame(self)
		self.frame7.pack(fill=X)
		self.label7 = Label(self.frame7, text="Minimum Value", width=13)
		self.label7.pack(side=LEFT, padx=5, pady=5)

		self.entry7 = Entry(self.frame7)
		self.entry7.pack(fill=X, padx=5, expand=True)
		# self.frame6 = Frame(self).pack(fill=X)
		# self.label6 = Label(self.frame6, text="Max Value", width=8).pack(side=LEFT, padx=5, pady=5)
		# self.entry6 = Entry(self.frame6).pack(fill=X, padx=5, expand=True)


		# self.listframe = Frame(self)
		# self.listbox = Listbox(self.listframe, selectmode=EXTENDED)
		# self.listbox.pack(side=LEFT, fill=BOTH, expand=1)
		# self.listframe.pack(fill=BOTH, expand=1)

		self.buttonframe = Frame(self)
		self.button = Button(self.buttonframe, text="Enter", command=self.enter)
		self.button.pack(side=BOTTOM)
		self.buttonframe.pack(fill=X, padx=10, pady = 10)

	def enter(self):
		# global self.initUI().entry1, self.initUI().entry2, self.initUI().entry3
		str1 = self.entry1.get()
		str2 = self.entry2.get()
		str3 = self.entry3.get()
		# str1 = entry1.get()
		# str2 = entry2.get()
		# str3 = entry3.get()
		self.listbox.insert(END, str1)
		self.listbox.insert(END, str2)
		self.listbox.insert(END, str3)

		# from here I can think about calling the checker and put in the user input as parameter.

def main():
	root = Tk()
	root.geometry("300x300+300+300")
	UserInput(root)
	root.mainloop()

if __name__ == '__main__':
	main()

