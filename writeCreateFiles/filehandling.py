f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after te appending:
f = open("demofile2.txt", "r")
print(f.read())
