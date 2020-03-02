# Pattern Matching
"""n=10
for i in range(n):
    for j in range(i):
        print('*',end=" ")
    print(' ')
for i in range(n,0,-1):
    for j in range(i):
        print('*', end=" ")
    print(' ') """
from pip._vendor.distlib.compat import raw_input

"""# Lines like Upper case
line=[]
while True:
    l=input()
    if l:
        line.append(l.upper())
    else:
        break;
for l in line:
    print(l)"""

#Bubble sort

"""arraylist=[23,45,1,23,44,55,77,3,2,3,2,4,67,990]
for j in range(len(arraylist)):
    swapflag= False
    i = 0
    while i<len(arraylist)-1:
        if arraylist[i] > arraylist[i+1]:
            arraylist[i],arraylist[i+1]=arraylist[i+1],arraylist[i]
            swapflag=True
        i=i+1
    if swapflag == False:
        break
print(arraylist)"""


"""arraylist=[12,24,67,22,33,12,11,2,6,8]
for j in range(len(arraylist)):
    swapflag = False
    i = 0
    while i<len(arraylist)-1:
        if arraylist[i] > arraylist[i+1]:
            arraylist[i],arraylist[i+1]=arraylist[i+1],arraylist[i]
            swapflag = True
        i = i+1
    if swapflag == False:
        break
print(arraylist)"""


"""list=[89,55,2,3,4,55,66,22,11,2,3,4,1,1,2,2,3]
for j in range(len(list)):
    swapflag= False
    i=0
    while i<len(list)-1:
        if list[i] > list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
            swapflag= True
        i=i+1
    if swapflag == False:
        break
print(list)"""


"""string=raw_input("Enter string:")
char=0
word=1
for i in string:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)"""


"""string = raw_input('enter string:')
char=0
word=1
for i in string:
      char=char+1
      if (i== ' '):
            word=word+1
print('the characters:')
print(char)
print('the words:')
print(word) """

"""flag =True
if flag == True:
      print('this is python if statement')
      print('this is initial program for python code')
"""

"""num = 10
if num%2 == 1:
      print('even number')
else:
      print('this is not even number')"""

"""#n=int(input("enter number to check:")
n=3000
if n < 500:
      print('the number is lesser one')
elif n < 1000:
      print('the number is medium')
elif n ==1500:
      print('the number is near to')
elif n > 3000:
      print('the number is greater ')
else:
      print('the number is invalid') """

"""num = 1122
if 9 < num < 99:
    print("Two digit number")
elif 99 < num < 999:
    print("Three digit number")
elif 999 < num < 9999:
    print("Four digit number")
else:
    print("number is <= 9 or >= 9999")"""

"""num=-90
if num >0:
      print('positive number')
else:
      print('the number is negative')
      if -99 < num:
            print('the two digit negative number')"""
"""
set=[12,3,4,55,66,'uma']
12 in set
print('yes i am in set') """


#pattern matching
"""n=10
for i in range(n):
      for j in range(i):
            print('*',end=" ")
      print(' ')
for i in range(n,0,-1):
      for j in range(i):
            print('*',end=" ")
      print(' ')"""

"""for val in range(10):
	print(val)
else:
	print("The loop has completed execution")"""

"""for num1 in range(4):
	for num2 in range(10, 15):
		print(num1, ",", num2)"""

#LInes is Upper case

"""line=[]
while True:
      l=input()
      if l:
            line.append(l.upper())
      else:
            break;
for l in line:
      print(l)"""

'''while True:
   print("hello")'''

'''num = 1
while num<5:
   print(num)'''

'''i = 1
j = 5
while i < 4:
    while j < 8:
        print(i, ",", j)
        j = j + 1
        i = i + 1'''
'''num = 10
while num > 6:
   print(num)
   num = num-1
else:
   print("loop is finished")'''

"""for num in [23,34,45,56,78,2,3]:
   print(num)
   if (num==45):
      print('the number is found')
      print('terminate the block')
      break"""

'''for num in [11, 9, 88, 10, 90, 3, 19]:
   print(num)
   if(num==88):
	   print("The number 88 is found")
	   print("Terminating the loop")
	   break'''

'''for num in [22,34,54,6,8,9,89]:
     if num %2 == 0:
      continue
     print (num)'''

'''for num in [20, 11, 9, 66, 4, 89, 44]:
    # Skipping the iteration when number is even
    if num%2 == 0:
        continue
    # This statement will be skipped for all even numbers
    print(num)'''

'''for num in [20, 11, 9, 66, 4, 89, 44]:
    if num%2 == 1:
        pass
    else:
        print(num)'''

'''string=raw_input("Enter string:")
string=string.replace(' ','-')
print("Modified string:")
print(string)'''


# Replace Characters from a string
'''string=raw_input('enter the string:')
string=string.replace('$','@')
print('the modified string:')
print(string)'''

# Remove nth index character from a non-empty string
"""def remove(string, n):
   first = string[:n]
   last = string[n + 1:]
   return first + last
string = raw_input ("Enter the sring:")
n = int (input ("Enter the index of the character to remove:"))
print ("Modified string:")
print (remove (string, n)) """

#declaring a variable
'''a=1000
print(a)'''

'''# re declaring a variable
a=1000
print(a)
a='this is re declaring a variable'
print(a)

f='hi this is uma'
print(str(1000)+' '+ f)'''

'''f=100
print(f)
def somefunction():
   f='hi this is uma'
   print(f)
somefunction()
print(f)'''

'''f=11
print(f)

del f
print(f)
'''
'''
var1 = "hi this is uma!"
var2 = "Software Testing"
print ("var1[0]:",var1[8:])
print ("var2[1:7]:",var2[1:6])'''

'''old_string='here i am writing c program'
print(old_string.upper())'''

'''f='i am uma'
print('@ '.join(f))'''
'''
string='my favorate star is gujun pyo'
print(string.split(' '))'''

#tuple=('Robert', 'Carlos','Terminator', 'Actor','Florida')
#tup2 = (1,2,3,4,5,6,7);
#print(tup1[0])
#print(tup1[1:4])
#print(tup2[1:5])

'''x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(company)
print(emp)
print(profile)'''

'''x=('uma','devi')
(name,sur_name) = x
print(name,sur_name)
'''
'''
a=(2,4)
b=(3,7)
if (a>b): print('a is greater')
else:
   print('b is greater')'''


'''x=('uma','devi','ram')
print(x[2])
'''


'''dict={1:'uma',2:'devi',3:'ram'}
print(dict)
print(dict.items())
print(dict.values())
print(dict.keys())
print(dict[3])'''

'''Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
studentX=Boys.copy()
studentY=Girls.copy()
print (studentX)
print (studentY)'''

'''Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
del dict['Charlie']
print(dict)
'''
'''Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("student name:%s" %dict.items())
'''

'''dict ={1:'uma',2:'devi',3:'laxmi',4:'ram'}
boys_in_dict={4:'ram'}
girls_in_dict={1:'uma',2:'devi',3:'laxmi'}
for key in list(dict.key()):
   if key in list(boys_in_dict.key()):
      print(True)
   else:
      print(False)
'''

'''Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in list(Dict.keys()):
    if key in list(Boys.keys()):
        print(True)
    else:
        print(False)
        '''

'''Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
student =dict.key()
student.sort()
for s in student:
   print(":".join((s,str(dict[s]))))'''

'''i = sum = 0

while i <= 4:
    sum += i
    i = i+1

print(sum)
'''
'''for char in 'PYTHON STRING':
   if char == ' ':
      break

   print (char, end='')

   if char == 'O':
      continue
'''
'''# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)'''

'''def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(10)
'''

'''def printme(str):
   'this is first function define'
   print(str)
   return
printme('here function cals one time')
printme('here functions cals second time')
'''

'''def fun_1(x,y):
   """this is the sum of two numbers"""
   a=x+y
   print(a)
def func_2(x,y):
   """this is substraction"""
   a=x-y
   print(a)
print(fun_1(5,6))
print(func_2(10,4))
print(fun_1(11,2))
print(func_2(30,20))'''

def fun_sum(a,b):
   x=a+b
   print(x)
