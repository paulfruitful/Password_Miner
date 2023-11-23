import itertools

def toString(type):
 string=''
 for i in type:
  string+=f'{i}'
 return string

passLen=int(input('Enter Password Length:'))
digits=[0,1,2,3,4,5,6,7,8,9]
digits=digits*passLen
repeatedPasswords=itertools.permutations(digits,passLen)

def isCode_inFile(code):
  file=open('passlist.txt','r')
  file=file.read()
  if code in file:
   return True
  else:
   return False


with open('passlist.txt','a') as f:
    for i in repeatedPasswords:
        u=toString(i)
        f.write(f'{u} \n')
       


