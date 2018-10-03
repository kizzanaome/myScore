
from app.model import User
from validate import validate_input, validate_password
import re


all_users = []
passwords = []


def register():

    username = input("Enter your username: ")
    password = input("Enter your password:")
    role = input("Enter your role:")

    valid = validate_input(username, password, role)
    
    if valid:
        new_user = User(username, password, role)
        all_users.append(new_user)  
    else:
        return False 

    

    print(all_users)


# def login(username, password):
#     if any(user["username"] == username for user in all_users):
#         if any(user["password"] == password for user in all_users):
#             return True
#         return False
    

 