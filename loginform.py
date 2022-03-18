print('Create an account ')

username=input("Enter username: ")
password=input("Enter password: ")

print("Your account has been created sucessfully!!!")
print("Login Now")

username2=input("Enter username: ")
password2=input("Enter password: ")

if username==username2 and password==password2:
    print('Login sucessfully')
else:
    print('Invalid id password')