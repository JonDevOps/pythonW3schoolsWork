import os
#Check if file exists
if os.path.exists("demoFile.txt"):
#delete a file
	os.remove("demoFile.txt")
else:
	print("The file does not exist")
