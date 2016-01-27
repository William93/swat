import MySQLdb as mdb
from Tkinter import *
import tkMessageBox
import tkFont


# array to hold values from table data01 and table SPCchecker
value_data_reading = []
value_data_name = []
value_spc = []
error = {}

t = ""

# This function will display an alert window when anolmaly is detected
def alert():

	# get the values from dictCursor module
	values = ""
	values1 = ""
	values2 = ""
	for i in range(len(value_spc)):
		values = values + str(value_spc[i]) + "\n"

	for j in  range(len(value_data_reading)):
		values1 = values1 + str(value_data_reading[j]) + "\n"

	for k in range(len(value_data_name)):
		values2 = values2 + str(value_data_name[k]) + "\n"


	root = Tk()



# this text display window shows tag name
	leftSide = Text(root, height=70, width=80) # create a text display
	scrollLeft = Scrollbar(root, command=leftSide.yview)
	leftSide.configure(yscrollcommand=scrollLeft.set)
	leftSide.insert(END, "Tag Name\n\n")
	leftSide.insert(END, values2)
	leftSide.pack(side=LEFT)
	scrollLeft.pack(side=LEFT, fill=Y)

# this text display window shows the runtime tag value
	middle = Text(root, height=70, width=80)
	scrollMiddle = Scrollbar(root, command=middle.yview)
	middle.configure(yscrollcommand=scrollMiddle.set)
	middle.insert(END, 'RunTime Tag Value\n\n')
	middle.insert(END, values1)
	middle.pack(side = LEFT)
	scrollMiddle.pack(side=LEFT, fill=Y)

# this text display window shows the SPC
	rightSide = Text(root, height=70, width=80) # create a text display
	scrollRight = Scrollbar(root, command=rightSide.yview)
	rightSide.configure(yscrollcommand=scrollRight.set)
	rightSide.insert(END, "Set Point Constant\n\n")
	rightSide.insert(END, values)
	rightSide.pack(side=LEFT)
	scrollRight.pack(side=RIGHT, fill=Y)

	root.mainloop()

def check():
	error_list_name = ""
	error_list_runtime = ""
	error_list_golden = ""
	con = mdb.connect('localhost', 'root', 'swat', 'swatPLCdb')
	cur = con.cursor(mdb.cursors.DictCursor) # give the data in python dict form
	cur.execute("SELECT tag_value FROM SPCchecker WHERE module=\"P1\"") # query SPC from SPCchecker
	rows = cur.fetchall()

	cur1 = con.cursor(mdb.cursors.DictCursor) # give the data in  python dict form
	cur1.execute("SELECT * FROM data01") # query data01
	rows1 = cur1.fetchall()

	# store the spc values in an array
	for row in rows:
		value_spc.append(row["tag_value"])
		print row["tag_value"]

	# store the tag name in an array
	for row in rows1:
		value_data_name.append(row["Tag_Name"])
		print row["Tag_Name"]

	# # store data01 value in an array
	for row in rows1:
		value_data_reading.append(row["Tag_Value"])
		print row["Tag_Value"]

	print len(value_data_reading)
	print len(value_spc)
	con.commit()
	con.close()
	for k in range(8):
		# if ((value_data_reading[k] - value_spc[k]) != 0 ):
		# if(len(value_data_reading)==12):
		# print "number of elements in the array: " + lx`en(value_data_reading)
		# else:

		if(abs((float(value_spc[k]) - float(value_data_reading[k]))) >= 0.015):
			error[value_data_name[k]] = [value_data_reading[k], value_spc[k]]
		print (float(value_spc[k]) - float(value_data_reading[k]))
		print (float(value_spc[k]) )
		print (float(value_data_reading[k]))
	if(len(error) != 0):
		for h in range(len(error)):
			error_list_name = error_list_name + str(error.keys()[h]) + "\n\n"
			error_list_runtime = error_list_runtime + str(error.get(error.keys()[h])[0]) + "\n\n"
			error_list_golden = error_list_golden + str(error.get(error.keys()[h])[1]) + "\n\n"
		tkMessageBox.showinfo("Alert!", "Set Point Constant has been changed")

		root = Tk()
			



# this text display window shows tag name
		leftSide = Text(root, height=30, width=40, font=("Helvetica",20)) # create a text display
		scrollLeft = Scrollbar(root, command=leftSide.yview)
		leftSide.configure(yscrollcommand=scrollLeft.set)
		leftSide.insert(END, "Tag Name\n\n")
		leftSide.insert(END, error_list_name)
		leftSide.pack(side=LEFT)
		scrollLeft.pack(side=LEFT, fill=Y)

# this text display window shows the runtime tag value
		middle = Text(root, height=30, width=40, font=("Helvetica",20))
		scrollMiddle = Scrollbar(root, command=middle.yview)
		middle.configure(yscrollcommand=scrollMiddle.set)
		middle.insert(END, 'RunTime Tag Value\n\n')
		middle.insert(END, error_list_runtime)
		middle.pack(side = LEFT)
		scrollMiddle.pack(side=LEFT, fill=Y)

# this text display window shows the SPC
		rightSide = Text(root, height=30, width=40, font=("Helvetica",20)) # create a text display
		scrollRight = Scrollbar(root, command=rightSide.yview)
		rightSide.configure(yscrollcommand=scrollRight.set)
		rightSide.insert(END, "Set Point Constant(Golden)\n\n")
		rightSide.insert(END, error_list_golden)
		rightSide.pack(side=LEFT)
		scrollRight.pack(side=RIGHT, fill=Y)

		root.mainloop()

		value_data_reading[:] = []
		value_data_name[:] = []
		value_spc[:] = []
		error.clear()
		error_list_name = ""
		error_list_runtime = ""
		error_list_golden = ""
			
		
	# clear the array for next comparison
	value_data_reading[:] = []
	value_data_name[:] = []
	value_spc[:] = []
	error.clear()
	error_list_name = ""
	error_list_runtime = ""
	error_list_golden = ""


