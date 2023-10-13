import re
#pgm to check if a number is valid or not
def check_phone(num):
    pattern=r"\b[+]\d{1,3}\s\d{10}\b|\b\d{10}\b"
    exp=re.compile(pattern)
    matching=exp.findall(num)
    if not matching:
        print("invalid phone no")
    else:
        print("valid phone no",num)
        
#match date of birth
pattern=re.compile("^(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])/\d{4}$")
x=pattern.findall(input("enter your date of birth"))
if not x:
    print(" wrong format")
else:
    print("valid")
    
import re

#check if passowrd is valid opr not
pattern=re.compile("^(?=.*[A-Z])(?=.*\d).{8,}$)")
x=pattern.findall(input("enter your password"))
if not x:
    print(" valid")
else:
    print("invalid")
    
#pgm to remove all the html tags
html_tag=input("enter a html tag")
print("removing all html tags")
print(re.sub(r'<.*?>','',html_tag))
      
#pgm to check whether the ip address is valid or not

x=input("enter an ip address")
pattern="[192]+\.[168]+\.\d\d?\d?\.\d\d?\d?"
if re.findall(pattern,ip)!=[]:
    print(x,"is valid")
else:
    print("invalid ip address")
      
#progrm to remvoe hashtags
x=input("enter a social media content")
patter="(#\w*)"
print("extracct hashtags")
print(re.findall(pattern,x))
      
#pgm to extract domain from url

url=input("Enter a url: ") 
pattern="[https]+\:\/{2}w{3}\.\w*\.[com]+\/?\w*" 
if re.findall(pattern,url)!=[]: 
    print("Extracting domain from url") 
    pattern2="[https]+\:\/{2}w{3}\.(\w*\.[com]+)\/\w*" 
    print(re.findall(pattern2,url)) 
 else: 
    print("Invalid url")
      
#extracting numbers

text=input("Enter a text: ") 
pattern="(\d+)" 
print("Extracting numbers:") 
print(re.findall(pattern,text))




