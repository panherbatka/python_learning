correct_password = "python123"
name = input("Enter name: ")
surname = input("Enter surname: ")
password = input("Enter password: ")

while correct_password != password:
     password = input("Wrong password! Try again: ")

print("Hi %s %s, you are logged in" % (name, surname))