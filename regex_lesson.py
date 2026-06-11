import re
while True:
 username = input("enter your username:\n")
 valid_username = re.match(r"^[a-zA-Z]\w{5,12}$", username)
 if valid_username:
    print("successfully added")
    break
 else:
    print("invalid credentials")
   

while True:
  email = input("enter your email:\n")
  valid_email = re.match(r"^[a-zA-Z\d][a-zA-Z\d._+%-]*@[a-zA-Z\d]+\.(com|net|org)$", email)
  if valid_email:
    print("Valid email")
    break
  else:print("email doesnt exist")

 
while True:
   phone_number = input("enter your phone number:\n")
   valid_number = re.match(r"^07\d{8}$", phone_number)
   if valid_number:
    print("Number recognised")
    break
   else:print("Phone number doesnt work in this country")
   

if valid_username and  valid_email and  valid_number:
    print("succefull registration")
else:
    print("Failed registration")
 