#python can be used to perform some operations on file.(read & write)
#text file - .txt, .docx, .log etc.(data in character form)
#binary file - .mp4, .mov, .jpeg etc.(non character form)
#at the end all files and data are store in the form of binary only(0,1) in the sys.
#default mode to open a file is r:read mode and text mode.
f = open("Input_Output.txt", "r")
data = f.read()
print(data) #hii, my name is neha.
print(len(data)) #21
print(type(data)) #<class 'str'>
f.close()
print(data)

#if we want to print limited character of data
f = open("Input_Output.txt", "r")
data = f.read(8)
print(data) #hii, my name is neha.
print(len(data)) #8
print(type(data)) #<class 'str'>
f.close()




