import re
s= "Bangladesh"
# in regular expression we can find matched string by using '.' until \n
#search() module is used
match = re.search('.',s)
print(match.group())
match = re.search('B.n',s)
print(match.group())
match = re.search('B.n...',s)
print(match.group())
s = "Bangladesh is our homeland"
match = re.search('..............',s)
print(match.group())
#to skip space in string we use \w
match = re.search('o\w\w',s)
print(match.group())
match = re.search('i\w',s)
#in above line we can not write i\w\w because after i there is only one char
#i\w\w means 3 chars without space.
print(match.group())
match = re.search('B\w+h',s)
#this is used to find B then go on until h without 'space'
print(match.group())
match = re.search('B.+h',s)
#this will return string start from B until the last h including space.
#because regular expression is greedy. It will go on to the last findings.
print(match.group())
match = re.search('B.+?h',s)
#this will end in the first finding of h
print(match.group())

