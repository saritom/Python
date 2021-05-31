#Opening and Reading Text Files
f = open ('D:\Dev\Python\\myfile.txt', 'r')

firstline = f.readline()
secondline = f.readline()
print(firstline)
print(secondline)
f.close()

#Using a For Loop to Read Text Files
f = open ('D:\Dev\Python\\myfile.txt', 'r')
for line in f:
    print (line, end = '')
f.close()

#Writing to text file
f = open ('D:\Dev\Python\\myfile.txt', 'a')
f.write('\nThis sentence will be appended.')
f.write('\nPython is Fun')
f.close()

#Opening and Reading Text Files by Buffer Size
inputFile = open ('D:\Dev\Python\\myfile.txt', 'r')
outputFile = open ('myoutputfile.txt', 'w')
msg = inputFile.read(10)
while len(msg):
    outputFile.write(msg + '\n') 
    msg = inputFile.read(10)
inputFile.close()
outputFile.close()

#Opening, Reading and Writing Binary Files
inputFile = open ('D:\Dev\Python\\myimage.jpg', 'rb')
outputFile = open ('myoutputimage.jpg', 'wb')
msg = inputFile.read(10)
while len(msg):
    outputFile.write(msg) 
    msg = inputFile.read(10)
inputFile.close()
outputFile.close()