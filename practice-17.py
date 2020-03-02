# a
i = 1
while i <= 4:
    print( "*" * i)
    i = i + 1

# b
i = 1
j = 2
while i >= 1:
    b = " " * j + "*" * i + " " * j
    print(b)
    i = i + 2
    j = j - 1
    if i > 5:
        break
i = 3
j = 1
while i >= 1:
    c = " " * j + "*" * i + " " * j
    print(c)
    i = i - 2
    j = j + 1


"""n=5;
for i in range(n):
	 for j in range(i):
          print ('* ', end="")
	 print('')

for i in range(n,0,-1):
	 for j in range(i):
	      print('* ', end="")
      print('')"""

"""n=10
for i in range(n):
    for j in range(i):
      print ('*', end=" ")
    print(' ')
for i in range(n,0,-1):
    for j in range(i):
        print('*', end=" ")
    print('')"""

"""lines = []
while True:
    l = input ()
    if l:
        lines.append (l.upper ())
    else:
        break;

for l in lines:
    print (l)"""

"""result_str="";
for row in range(0,7):
    for column in range(0,7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str); """

"""result_str="";
for row in range(0,7):
    for column in range(0,7):
        if (column == 1 or ((row == 0 or row == 3) and column > 1 and column < 5)
                or (column == 5 and row != 0 and row < 3) or (column == row - 1 and row > 2)):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str);"""


"""a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
k=0
num=int(input("Enter the number to be counted:"))
for j in a:
    if(j==num):
        k=k+1
print("Number of times",num,"appears is",k)"""






"""string="";
for row in range(0,10):
    for column in range(0,10):
        if (column == 1 or ((row == 0 or row == 4) and column > 1 and column < 8) or (column == 8 and row !=0 and row < 4) or (column == row - 1 and row > 2)):
            string=string+"*"
        else:
            string=string+" "
    string=string+"\n"
print(string);"""


"""n=10
for i in range(n):
    for j in range(i):
        print('*',end=" ")
    print(' ')
for i in range(n,0,-1):
    for j in range(i):
        print('*', end=" ")
    print(' ')"""


"""line =[]
while True:
    l= input()
    if l:
        line.append(l.upper())
    else:
        break;
for l in line:
    print(l)"""

"""line=[]
while True:
    l=input()
    if l:
        line.append(l.upper())
    else:
        break;
for l in line:
    print(l)"""


#return type function
def add_r(a, b):
  """ return type function to find sum """
  x = a + b
  return x

#non return type function
def add_n(a, b):
  """ non return type function to return sum """
  x = a + b
  print (x)

#call the return type function and print
print (add_r(2,3))

#call the non return type function
add_n(2,3)






