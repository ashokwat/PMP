"""
str = 'Hello World!'

print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string
#######
#Exercise 02: Max of ..
def maxi(a,b):
   if a > b:
      print "The greater no.is :" +str(a)
   else:
      print "The greater no.is :" +str(b)
maxi(80,60)

######
#Exercise 03: max of 3 ..
def max_of3 (a,b,c):
   if a > b:
      great = a
   else:
      great = b
   if c > great:
      great = c
   return(great)
gr=max_of3(32,15,40)
print"The largest no.is :"+str(gr)

######
#Exercise 04:  Compute lenth of a given string

cnt=0
for i in 'find length':
    print i
    cnt+=1
     
#Exercise 05 :take input as char and chcek vowel yes or NO.
# how to restrict input to one char..
str01= raw_input("Enter any char: ");
print "Recd input is ",str01
if str01 in ("aeiou"):
    print "vowel";
else :
    print "No vowel" ;

## Exercise 06 :Robbers language
str01 = raw_input("Enter few words:");
print "You entered :",str01
y=len(str01)
str02 =""
i=0
for i in range(0,y,1):
    if str01[i] not in ("aeiou"):
        if str01[i]== " ":
            str02=str02 + str01[i];
        else:
            str02=str02 + str01[i] +"o" + str01[i];
    else:
        str02=str02 + str01[i]
print str02
   
#exercise07 define function SUM & multiply..
def sum1(a,b,c,d):
    op=a+b+c+d
    return op
oop = sum1(1,2,3,4)
print oop

def mult(a,b,c,d):
    op1=a*b*c*d
    return op1
oop1=mult(1,2,3,4)
print oop1

#Exercise 08: print reverse of string.
str01 = raw_input("Enter text");
str02 =""
print  str01
y=len(str01)
for i in range(-1,-(y+1),-1):
    str02 = str02 + str01[i];
print str02

#Exercise 09 chcek  for palindromes
str01 = raw_input("Enter text");
str02 =""
print  str01
y=len(str01)
for i in range(-1,-(y+1),-1):
    str02 = str02 + str01[i];
print str02
if (str01==str02):
    print "Yes it is palindrome"
else:
    print "No paindrome"
"""
#Exercise 10 check if a element is a member of list
str01 = raw_input("Enter the text: ")
mylist = ["AA", "BB", "CC", "DD"]
def is_member(str01,mylist):
    i=0
    j=0
    while i < len(mylist):
        if mylist[i] == str01:
            j=j+1
        i=i+1
    if j > 0 :
        return 1
    else:
        return  0
val = is_member(str01,mylist)
if val == 1:
    print "TRUE"
else:
    print "FALSE"
