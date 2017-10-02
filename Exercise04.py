"""
#Exercise 23 Spelling corrction function correct()
input = "This    is very  funny and cool.Indeed!"
str1 = ""
for i in input:
    if (i==" " and pr == 1):
        pass
    else:
        str1= str1 + i
    if i == " ":
        pr = 1
    else :
        pr = 0
print input
print str1

#Exercise 25..
#26.	If the verb ends in y, remove it and add ies
#27.	If the verb ends in o, ch, s, sh, x or z, add es
#28.	By default just add s

ch = raw_input("Enter Verb:")
l=len(ch)
n = 1
str1 = ""
if ch[-1]  ==  "y":
    for i in ch:
        if len(str1)== (l-1):
            str1 = str1 + "ies"
            break
        else:
            str1 = str1 + i
elif ch[-1]  in  ["o","s","x","z"]:
    str1=str1+ch+"es"
elif ch[-1]== "h" and (ch[-2] in ["c","s"]):
    str1=str1+ch+"es"
else:
    str1=str1+ch+"s"
print ch
print str1

#Exercise 28 ..  find max from the list  use reduce function..
f = (lambda a,b: a if a > b else b)
l= [12,15,25,11,9,88]
print reduce(f,l)

#exercise 29 that maps a list of words into a list of integers
#representing the lengths of the correponding words. 
l1 = ["map","junk","prince","miscleneous"]
l2 =[11,6,3,4]
tu = ();
for i in l1:
    for j in l2:
        if len(i) == j:
            tu = tu + (i,j)
print tu


#Exercise 30 : find longest word..

f= (lambda a,b: a if len(a) > len(b) else b )
l=["one","two","ten","Hundred"]
print len(reduce(f,l))

#Exercise 31 # function that returns a word longer than n
#print list(map(lambda x:x**2,[1,2,3,4]))
#print list(map(lambda x,y:x+y,[1,2,3,4],[10,20,30,40]))
def return_word(l,n):
    l1=list(filter(lambda a:len(a)> n,l))
    return  l1
l=["one","two","ten","Hundred","to","banglore"]
print l
print return_word(l,2)

#Exercise 32: Translation dictionary
dict1 = {"merry":"god",
         "christmas":"jul",
         "and":"och",
         "happy":"gott",
         "new" : "nytt",
         "year":"ur"}
eng_in = ["new","and","year","exit"]
l=list (map(lambda x:dict1.get(x,x),eng_in))
print eng_in
print l
"""
#exercise 29 that maps a list of words into a list of integers
#representing the lengths of the correponding words. 
l1 = ["map","junk","prince","miscleneous"]
l2 =[11,6,3,4]
tu = ();
for i in l1:
    for j in l2:
        if len(i) == j:
            tu = tu + ((i,j),)
print tu



    


    
