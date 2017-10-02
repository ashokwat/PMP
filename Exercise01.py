"""
read line one and replace * with space.
f = open(filename,'r')
f.seek(-1,2)     # go to the file end.
eof = f.tell()   # get the end of file location
f.seek(0,0)      # go back to file beginning

while(f.tell() != eof):
    <body>

The above does not work to check eof.
"""
import os
os.remove("ashok800.txt")# remove o/p file if exist
with open('ashok500.txt','r')as f:
    while 1 :
        line1= f.readline()
        if ("" == line1):
            break;  # if eof exit the loop
        line2 = ""
        y = len(line1)# fine how long is the string
        for i in range(0,y,1):
            if (line1[i]== "*"):
                line2 = line2 + " "
            else:
                line2 = line2 + line1[i]
        with open('ashok800.txt','a') as g:
            g.writelines(line2)
    g.close()  
    f.close()
