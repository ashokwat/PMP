"""
#Exercise 11 Overlapping check if at least one element is common
L1 = ["AA", "BB", "CC", "MM"]
L2 =  ["aa","bb","cc","MM", "EE","DD","NN"]
def overlapping(mylist1,mylist2):
    re = 0
    for a in mylist1:
        for b in mylist2:
            if a == b:
                re = 1
    return re
t=overlapping(L1,L2)                     
if t == 1:
    print "Found"
else:
    print "Not found"
   
#Exercise 12 write a function to generate N char
def gen_n_char(n,ch):
    ch1 = ch
    i=1
    while i < n:
        ch1 = ch1 + ch
        i+=1
    return ch1
str01=gen_n_char(7,'Z')
print "Char :" + str01

#EXececise 13 : procedure histogram
mylist = [10,9,8,7,6]
for i in mylist:
    print ""
    j=0
    op = ""
    while j < i:
        print '*',
        j+=1

#Exercise 14 :function max in the list
mylist = [12,15,45,78,17,100]
def max_list(mylist):
    max = 0
    for i in mylist:
        if i > max:
            max = i
    print "Max :" + str(max)
max_list(mylist)

#Exercise 16: find the longest word
mylist =['Ashok','Teju','roshan','veena','venkat kumar']
l = 0
for i  in mylist:
    if len(i) > l:
        l = len(i)
        lword = i
print lword , "Length:" + str(l)

# Exercise 20: 99 bottles of  beer on the wall, 99 bottles of beer,
#take one down and pass it around,
# 98 bottles of beer on the wall
for i in range(99,95,-1):
    print str(i) + " bottles of beer on the wall,", str(i) + " bottles of beer."
    print "take one down and pass it around"

#  Exercise 21: Translation dictionary
dict1 = {"merry":"god",
         "christmas":"jul",
         "and":"och",
         "happy":"gott",
         "new" : "nytt",
         "year":"ur"}
eng_in = ["new","and","year","exit"]
for i in eng_in:
    print i , dict1.get(i,'Not found')

# Exercise 22:  char frequency

input = "abbabcbdbabdbdbabababcbcbab"
new_list = []
for i in input:
    ch = i
    j=0
    if ch not in new_list:
        for k in input:
            if k == ch:
                j+=1
        new_list.extend([ch])
        print ch , "FREQ :" + str(j)

"""
#exercise 23:cryptography, a Caesar cipher 
ROT13 ={'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M', ' ':' '}
input = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
str1 = ""
for i in input:
    str1=str1 + str(ROT13.get(i,i))
print input
print str1


    


    

