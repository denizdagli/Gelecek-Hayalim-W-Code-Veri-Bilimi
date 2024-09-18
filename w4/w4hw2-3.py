print("Ödev-2,3")

user_name=input("Enter your name: ")
while True:
   password=input("Enter your password: ")
   if 5< len(password)<10:
      print("Welcome",user_name, "your password is saved")
      break
   else:
        print("Please enter a password between 5 and 10 characters")
        
