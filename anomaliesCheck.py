import MySQLdb as mdb
from Tkinter import *
import tkMessageBox


# array to hold input, output, tag name values from table anomalies
# value_input = []
# value_data_name = []
# value_output = []
# value_water_level = []

t = ""
# values = ""
# values1 = ""
# values2 = ""
# This function will display an alert window when anolmaly is detected
# def alert():

# 	# get the values from dictCursor module
	# values = ""
	# values1 = ""
	# values2 = ""
# 	for i in range(len(value_spc)):
# 		values = values + str(value_spc[i]) + "\n"

# 	for j in  range(len(value_data_reading)):
# 		values1 = values1 + str(value_data_reading[j]) + "\n"

# 	for k in range(len(value_data_name)):
# 		values2 = values2 + str(value_data_name[k]) + "\n"


# 	root = Tk()



# # this text display window shows tag name
# 	leftSide = Text(root, height=20, width=30) # create a text display
# 	scrollLeft = Scrollbar(root, command=leftSide.yview)
# 	leftSide.configure(yscrollcommand=scrollLeft.set)
# 	leftSide.insert(END, "Tag Name\n\n")
# 	leftSide.insert(END, values2)
# 	leftSide.pack(side=LEFT)
# 	scrollLeft.pack(side=LEFT, fill=Y)

# # this text display window shows the runtime tag value
# 	middle = Text(root, height=20, width=50)
# 	scrollMiddle = Scrollbar(root, command=middle.yview)
# 	middle.configure(yscrollcommand=scrollMiddle.set)
# 	middle.insert(END, 'RunTime Tag Value\n\n')
# 	middle.insert(END, values1)
# 	middle.pack(side = LEFT)
# 	scrollMiddle.pack(side=LEFT, fill=Y)

# # this text display window shows the SPC
# 	rightSide = Text(root, height=20, width=30) # create a text display
# 	scrollRight = Scrollbar(root, command=rightSide.yview)
# 	rightSide.configure(yscrollcommand=scrollRight.set)
# 	rightSide.insert(END, "Set Point Constant\n\n")
# 	rightSide.insert(END, values)
# 	rightSide.pack(side=LEFT)
# 	scrollRight.pack(side=RIGHT, fill=Y)

# 	root.mainloop()

def check():
	value_input = []
	value_data_name = []
	value_output = []
	value_water_level = []
	values = ""
	values1 = ""
	values2 = ""
	con = mdb.connect('localhost', 'root', 'swat', 'swatPLCdb') # connect to the database
	cur = con.cursor(mdb.cursors.DictCursor) # give the data in python dict form
	cur.execute("SELECT tag_value FROM anomalies WHERE tag_name=\'HMI_FIT101.Pv\';") # query HMI_FIT101.Pv reading from SPCchecker
	rows = cur.fetchall()

	cur0 = con.cursor(mdb.cursors.DictCursor) # give the data in python dict form
	cur.execute("SELECT tag_value FROM anomalies WHERE tag_name=\'HMI_FIT201.Pv\';") # query HMI_FIT201.Pv reading from SPCchecker
	rows0 = cur.fetchall()

	cur1 = con.cursor(mdb.cursors.DictCursor) # give the data in  python dict form
	cur1.execute("SELECT tag_value FROM anomalies WHERE tag_name=\'HMI_LIT101.Pv\';") # query tag name 
	rows1 = cur1.fetchall()

	cur2 = con.cursor(mdb.cursors.DictCursor) # give the data in python dict form
	cur.execute("SELECT tag_name FROM anomalies;")
	rows2 = cur.fetchall()

	# store the input values in an array
	for row in rows:
		value_input.append(row["tag_value"])
		print row["tag_value"]

	# store the output value in an array
	for row0 in rows0:
		value_output.append(row0["tag_value"])
		print row["tag_value"]

	# # store water level value in an array
	for row1 in rows1:
		value_water_level.append(row1["tag_value"])
		print row["tag_value"]

	# store the tag name in an array
	for row2 in rows2:
		value_data_name.append(row2["tag_name"])


	con.commit()
	con.close()

# the following is the checker algorithm
# define a valid range for the difference of input and output
# if the value is within the range and water level is increasing,
# something is wrong and it will display a pop up window
	if(len(value_water_level)>=2):
		for i in range(2):
			values = values + str(value_input[len(value_input)-(i+1)]) + '\n\n'
			values1 = values1 + str(value_output[len(value_output)-(i+1)]) + '\n\n'
		# values2 = values2 + str(float(absvalue_output[i] - float(value_input[i]))) + '\n\n'
		# print values
		# print values1

		# I havent decided what values should be use, so I just use a random number


		if(abs(float(value_water_level[len(value_water_level)-1]) - float(value_water_level[len(value_water_level)-2])) >= 3):
			# if(abs((float(value_water_level[1] - float(value_water_level[0] >= 7))))):
			values2 = values2 + str(abs(float(value_water_level[len(value_water_level)-1]) - float(value_water_level[len(value_water_level)-2]))) + '\n\n'
			tkMessageBox.showinfo("Alert!", "anomalies detected")

			root = Tk()



# this text display window shows tag name
			leftSide = Text(root, height=30, width=30, font=("Helvetica",20)) # create a text display
			scrollLeft = Scrollbar(root, command=leftSide.yview)
			leftSide.configure(yscrollcommand=scrollLeft.set)
			leftSide.insert(END, "Tag Name\n\n")
			leftSide.insert(END, value_data_name[1])
			leftSide.pack(side=LEFT)
			scrollLeft.pack(side=LEFT, fill=Y)

# this text display window shows the runtime tag value
			middle = Text(root, height=30, width=30, font=("Helvetica",20))
			scrollMiddle = Scrollbar(root, command=middle.yview)
			middle.configure(yscrollcommand=scrollMiddle.set)
			middle.insert(END, 'Increase in Water Level Value\n\n')
			middle.insert(END, values2)
			middle.pack(side = LEFT)
			scrollMiddle.pack(side=LEFT, fill=Y)

			rightMiddle = Text(root, height=30, width=30,font=("Helvetica",20))
			scrollMiddle = Scrollbar(root, command=middle.yview)
			rightMiddle.configure(yscrollcommand=scrollMiddle.set)
			rightMiddle.insert(END, 'Input Flow Rate\n\n')
			rightMiddle.insert(END, values)
			rightMiddle.pack(side = LEFT)
			scrollMiddle.pack(side=LEFT, fill=Y)

# this text display window shows the SPC
			rightSide = Text(root, height=30, width=30,font=("Helvetica",20)) # create a text display
			scrollRight = Scrollbar(root, command=rightSide.yview)
			rightSide.configure(yscrollcommand=scrollRight.set)
			rightSide.insert(END, "Ouput Flow Rate\n\n")
			rightSide.insert(END, values1)
			rightSide.pack(side=LEFT)
			scrollRight.pack(side=RIGHT, fill=Y)

			root.mainloop()
# 		elif(abs(float(value_water_level[len(value_water_level)-1]) - float(value_water_level[len(value_water_level)-2])) == 0):
# 	# if(abs((float(value_water_level[1] - float(value_water_level[0] >= 7))))):
# 			values2 = values2 + str(abs(float(value_water_level[len(value_water_level)-1]) - float(value_water_level[len(value_water_level)-2]))) + '\n\n'
# 			tkMessageBox.showinfo("Alert!", "anomalies detected")

# 			root = Tk()



# # this text display window shows tag name
# 			leftSide = Text(root, height=30, width=30, font=("Helvetica",20)) # create a text display
# 			scrollLeft = Scrollbar(root, command=leftSide.yview)
# 			leftSide.configure(yscrollcommand=scrollLeft.set)
# 			leftSide.insert(END, "Tag Name\n\n")
# 			leftSide.insert(END, value_data_name[1])
# 			leftSide.pack(side=LEFT)
# 			scrollLeft.pack(side=LEFT, fill=Y)

# # this text display window shows the runtime tag value
# 			middle = Text(root, height=30, width=30, font=("Helvetica",20))
# 			scrollMiddle = Scrollbar(root, command=middle.yview)
# 			middle.configure(yscrollcommand=scrollMiddle.set)
# 			middle.insert(END, 'Increase in Water Level Value\n\n')
# 			middle.insert(END, values2)
# 			middle.pack(side = LEFT)
# 			scrollMiddle.pack(side=LEFT, fill=Y)

# 			rightMiddle = Text(root, height=30, width=30, font=("Helvetica",20))
# 			scrollMiddle = Scrollbar(root, command=middle.yview)
# 			rightMiddle.configure(yscrollcommand=scrollMiddle.set)
# 			rightMiddle.insert(END, 'Input Flow Rate\n\n')
# 			rightMiddle.insert(END, values)
# 			rightMiddle.pack(side = LEFT)
# 			scrollMiddle.pack(side=LEFT, fill=Y)

# # this text display window shows the SPC
# 			rightSide = Text(root, height=30, width=30, font=("Helvetica",20)) # create a text display
# 			scrollRight = Scrollbar(root, command=rightSide.yview)
# 			rightSide.configure(yscrollcommand=scrollRight.set)
# 			rightSide.insert(END, "Ouput Flow Rate\n\n")
# 			rightSide.insert(END, values1)
# 			rightSide.pack(side=LEFT)
# 			scrollRight.pack(side=RIGHT, fill=Y)

# 			root.mainloop()

			
			
			# value_input = []
			# value_data_name = []
			# value_output = []
			# value_water_level = []

	# clear the array for next comparison
		# value_input = []
		# value_data_name = []
		# value_output = []
		# value_water_level = []
		# print float(value_water_level[len(value_water_level)-1]) 
  #       print float(value_water_level[len(value_water_level)-2])

