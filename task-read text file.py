'''with open('list.txt','r') as reader:
    print(reader.read())
'''
'''with open('list.txt', 'r') as reader:
  for line in reader.readlines():
       print(line, end='')'''

def simple_interest(p,t,r):
    return (p*t*r)/100
print('the simple interest:',simple_interest(p=10,t=10,r=1900))