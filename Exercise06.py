"""
# Exercise 41. Write a program that will calculate the average
#word length of a te(i.e the sum of all the lengths of the word
#tokens in the text,divided by the number of word tokens).
word_len=0.0
word_no = 0.0
with open('testfile.txt','r') as g:
    data = g.readlines()
    for line in data:
        words=line.split()
        for word in words:
            word_no+=1
            word_len=word_len + len(word)
ave_len=(word_len/word_no)
print "Average Word Length:",format(ave_len,'0.4f')
"""
#Exercise 44: Game of  lingo
#create a dict of animal names of length FIVE
#let computer pickone and you have to guess animal
#letter in () is present but position not correct
#letter in [] letter is in correct position
animals={1:'zebra',
         2:'snake',
         3:'tiger',
         4:'whale',
         5:'panda',
         6:'camel',
         7:'sheep',
         8:'camel',
         9:'hippo',
         10:'horse'}
import random
N =random.randint(1,10)
if N==0:
    N=10
str1=animals.get(N,N)
s2=len(str1)
new_l=[]
for i in str1:
    new_l.append(i)
flag=1
while flag:
    g_str=raw_input("Guess Animal:")
    s3=len(g_str)
    l1=[]
    for j in g_str:
        l1.append(j)
    l2=[]+l1
    for m,n in enumerate(l1):
        if n in new_l:
            l2[m]='('+n+')'
    x=0
    for k,v in enumerate(l1):
        if k > (s2-1):
            pass
        elif new_l[k] == v:
            l2[k]='['+v+']'
            x=x+1
    print l2
    if x==len(l1):
        print "congratulations"
        flag=0
    else:
        s1=raw_input("want one more chance(y/n):")
        if s1=='n':
            flag=0
##End of program








