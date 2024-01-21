import os

with open("mydata2.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more")

with open("mydata2.txt", encoding="utf-8") as myFile:
# read() readline() readlines():
    print(myFile.read())

#print(myFile.closed)
print(myFile.name)
print(myFile.mode)
# os.rename("mydata.txt", "mydata2.txt")
# os.remove("mydata2.txt")
os.mkdir("mydir")
os.chdir("mydir")
print("Current Directory :", os.getcwd())