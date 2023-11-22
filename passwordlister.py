import time 
import sys 
import os 
import itertools  
def animatedtext(text):
 load_str =text 
 ls_len = len(load_str) 
  
  
    # String for creating the rotating line 
 animation = "|/-\\"
 anicount = 0
 counttime = 0        
 i = 0                     
  
 while (counttime != 100): 
          
        time.sleep(0.095)  
                              
        load_str_list = list(load_str)  
          
        x = ord(load_str_list[i]) 
    
        y = 0                             
  
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
      
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
animatedtext("starting the password lister...")

os.system('cls')



print('''                
                         YOU ARE WELCOME TO PASSWORDLISTER
                         
MAKE SURE YOU READ THE FOLLOWING INSTRUCTIONS TO USE THE TOOL:
      
    **                                                           **  
  **   1.Make Sure You Answer Every Prompt                       //** 
 **    2. Make Sure You add every interest of your target         //**
/**    interests for example: Their Favourite Footballer,          /**
/**    their favourite tv character,                              /**
//**   their favourite game etc.                                  ** 
 //**  Make sure you specify the number of interests the have    **  
  //                                                           //   
      
''')


time.sleep(5)

os.system('cls')


def toString(type):
 string=''
 for i in type:
  string+=f'{i}'
 return string
print('!!!!!!!!!!!USE   TO SEPERATE THE FIRSTNAME AND LASTNAME!!!!!!!!!!!!!!!!!!')
name=input('Your Target Name:')
print('!!!!!!!!!!!USE / TO SEPERATE THE Day/Month/Yead!!!!!!!!!!!!!!!!!!')

year=input('Their Date of Birth:')
parameterRange=int(input('How Many Parameters Do You Have?'))
interests=[]

for i in range(1,parameterRange+1):
     interest=input(f'Add Interest {i}:  ')
     
     interests.append(interest)

name=name.split(' ')
year=year.split('/')
interests=name+year+interests
os.system('cls')
print('All Interests and Parameters Are Successfully Compiled!')
os.system('cls')

animatedtext('Your Password List Is Being Generated It Might Take A While....')
wordlist=itertools.combinations(interests,2)


j=list()
with open('passwordlist.txt','w') as f:
    for i in wordlist:
        u=''.join(i)
     
        j.append(itertools.permutations(u,len(u)))
        parse=''.join(u)

        string=f'{parse}\n'
        f.write(string)
with open('passwordlist.txt','a') as a:
 for i in j:
    for k in i:
        u=toString(k)
        a.write(f'{u}\n')
    animatedtext('Loading....')  
print('\n \n YOU ARE DONE!!')