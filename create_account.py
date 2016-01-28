from Tkinter import *

def accountChecking():
	# get the user input and store into variables
	username = entry1.get()
	password = entry2.get()
	re_enter = entry3.get()

# we need to set some constraint for password
	# try:
	if password == re_enter:
		sub = Tk()
		sub.title("Congratulation")
		subframe1 = Frame(sub)
		subframe1.pack(fill=X)
		msg = Message(subframe1, text="Successfully created account!")
		msg.pack()
		sub.mainloop()



root = Tk()

# window title
# root.geometry("600x400")
root.title("Create Account")

# username text frame
frame1 = Frame(root)
frame1.pack(fill=X)

# username label
label1 = Label(frame1, text="Username", width = 15)
label1.pack(side=LEFT, padx=3, pady=7)

# username entry
entry1 = Entry(frame1)
entry1.pack(fill=X, padx=5, pady=5, expand=False)

# password text frame
frame2 = Frame(root)
frame2.pack(fill=X)

# password label
label2 = Label(frame2, text="Password", width = 15)
label2.pack(side=LEFT, padx=3, pady=7)

# password entry
entry2 = Entry(frame2,show="*")
entry2.pack(fill=X, padx=5, pady=5)

# re-enter password text frame
frame3 = Frame(root)
frame3.pack(fill=X)

# re-enter password label
label3 = Label(frame3, text="Re-enter Password", width=15)
label3.pack(side=LEFT, padx=3, pady=7)

# re-enter password entry
entry3 = Entry(frame3,show="*")
entry3.pack(fill=X, padx=5, pady=5)

# button frame
frame4 = Frame(root)
frame4.pack(fill=X)

# button
button1 = Button(frame4, text="Create", command=accountChecking)
button1.pack(side=RIGHT, padx=5, pady =5)


root.mainloop()
