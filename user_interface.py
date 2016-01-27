#!/usr/bin/python

from Tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Testing")

textframe = Frame(root)
listframe = Frame(root)

# add content into listbox
def Enter():
	textContent = textbox.get()
	listbox.insert(END, textContent)
	textbox.delete(0, END)

# remove content in listbox
def Remove():
	listbox.delete(ANCHOR)

# save content in listbox into a file
def Save():
	pass

# the following are mouse event

#
def ReturnInsert(event):
	Enter()

def DeleteCurrent(event):
	Remove()

def CopyToText(event):
	textbox.delete(0, END)
	currentNote = listbox.get(ANCHOR)
	textbox.insert(0, currentNote)

# def Paste(envent):
	


# def Button1():
# 	listbox.insert(END, "button 1 pressed")

# def Button2():
# 	listbox.insert(END, "button 2 pressed")

# def Button3():
# 	textContent = textbox.get()
# 	listbox.insert(END, textContent)
# 	textbox.delete(0, END)

#create buttons
# button1 = Button(textframe, text="button 1", command=Button1)
# button2 = Button(textframe, text="button 2", command=Button2)
# button3 = Button(textframe, text="button 3", command=Button3)

enter_button = Button(textframe, text="Enter", command=Enter)
remove_button = Button(textframe, text="Remove", command=Remove)
save_button = Button(textframe, text="Save", command=Save)

textbox = Entry(textframe)

#add a scroll bar to for the list box
scrollbar = Scrollbar(listframe, orient=VERTICAL)
listbox = Listbox(listframe, yscrollcommand=scrollbar.set, selectmode=EXTENDED)
scrollbar.configure(command=listbox.yview)

textbox.bind("<Return>", ReturnInsert)
listbox.bind("<Double-Button-3>", DeleteCurrent)
listbox.bind("<Double-Button-1>", CopyToText)
enter_button.pack(side=LEFT)
remove_button.pack(side=LEFT)
save_button.pack(side=LEFT)

# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
textbox.pack(side=LEFT, fill=X, expand=1)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
scrollbar.pack(side = RIGHT, fill=Y)

textframe.pack(fill=X)
listframe.pack(fill=BOTH, expand=1)


root.mainloop()