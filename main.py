from cryptography.fernet import fernet
print("password manager")


print("password manager")nput("what is the master of password")

def view():
    with open('passwords.txt' , 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("#")
            print("user:",user , "password:" , passw)


def add():
    name= input ("account name:")
    password = input ("password:")

    with open('passwords.txt' , 'a') as f:
        f.write(name + "" + pwd + "\n")





while True:
     mode = input("would you like to add a new password or view existing ones(view,add)?")
     if mode == "view" :
         view()
     elif mode == "add" :
         add()
     else :
         print("invalid mode")
         continue

