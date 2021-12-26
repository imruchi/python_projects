import string
import random
 
password = []
 
length=int(input('Enter the desired length of your password:'))
length=int(length - 4)
 
uppercaseCount=random.randint(0, length) 
for i in range(uppercaseCount + 1):
   password.append(random.choice(string.ascii_uppercase))
 
length=length-uppercaseCount
lowercaseCount=random.randint(0, length)
for i in range(lowercaseCount + 1):
   password.append(random.choice(string.ascii_lowercase))
 
length=length-lowercaseCount
digitsCount=random.randint(0, length)
for i in range(digitsCount + 1):
   password.append(random.choice(string.digits))
 
punctuationCount=length-digitsCount
for i in range(punctuationCount + 1):
   password.append(random.choice(string.punctuation))
 
random.shuffle(password)
print(''.join(password))