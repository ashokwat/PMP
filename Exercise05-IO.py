"""
f=open('ashok.txt','w')
f.write('my nmae is  Ashok')
f.write('new line')
f.close()

#wrirelines accepts only one argumnet..
f=open('ashok.txt','w')
f.writelines(['This is is Ashok','\n new new line'])
f.close()


f=open('ashok100.txt','w')
f.writelines('XXXXXXXXXXX')
f.close()

#Exercise 35: read each line from file and  chcek  for palindromes
f=open('ashok200.txt','r')
for line in f.readlines():
    str1= line
#    str1="Rise to vote sir"
    str2 =""
    y=len(str1)
    for i in range(-1,-(y+1),-1):
        str2 = str2 + str1[i];
    str11= str1.replace(" ","")
    str22= str2.replace(" ","")
    A1=""
    A2=""
    A1 = str11.lower()
    A2 = str22.lower()
    print A1
    print A2
    if (A1 == A2):
        print "Yes"
    else :
        print "No"
f.close()

# Exercise 37:  char frequency  by reading a text from file

#input = "abbabcb  dbabdbdbab  ababcbcbA B"
f=open('ashok200.txt','r')
for input in f.readlines():
    input1=input.lower()
    input2=input1.replace(" ","")
    new_list = []
    for i in input2:
        ch = i
        j=0
        if ch not in new_list:
            for k in input2:
                if k == ch:
                    j+=1
            new_list.extend([ch])
            print ch , "FREQ :" + str(j)

f.close()

#Exercise 40 : program that given a text file will create a new
#text file in which all the lines from the original file are
# numbered from 1 to n
file = open('testfile.txt','w') 
 
file.write("Hello World \n"); 
file.write("This is our new text file \n") 
file.write("and this is another line.\n") 
file.write("Why? Because we can.\nThis is great") 
 
file.close()

with open('testfile.txt','r') as g:
    for line in g:
        print line

with open('testfile.txt','r') as g:
    data = g.readlines()
    for line in data:
        words=line.split()
        print words
"""
g= open('testfile.txt','r');
h= open('testfile1.txt','w');
data = g.readlines()
n=1
for line in data:
    h.write(str(n));
    h.write( line );
    n+=1
g.close()
h.close()

    

    
