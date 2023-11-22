import itertools

def toString(type):
 string=''
 for i in type:
  string+=f'{i}'
 return string

passLen=int(input('Enter Password Length:'))
digits=[0,1,2,3,4,5,6,7,8,9]
passlist=itertools.permutations(digits,passLen)
digits=digits*passLen
repeatedPasswords=itertools.permutations(digits,passLen)
print(digits)

with open('passlist.txt','a') as f:
    for i in passlist:
        u=toString(i)
        f.write(f'{u} \n')
    for i in repeatedPasswords:
        u=toString(i)
        f.write(f'{u} \n')
       
