import re



def validate_input(username, password, role):
    if not username:
        return {'username missing'}
    elif " " in username:
        return False
    elif not re.search("^[a-zA-Z]", username):
        return False
    elif not password:
        return {'password missing'}
    elif " " in password:
        return False
    elif not re.search(r"^(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$])[a-zA-Z0-9@#$]{6}$", password):
        return False
    elif not username:
        return {'username missing'}
    elif " " in username:
        return False
    elif not re.search("^[a-zA-Z]", username):
        return False
    else:
        return True
   

def validate_password(password):
    if not password:
        return False
    elif " " in password:
        return False
    elif not re.search(r"^(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$])[a-zA-Z0-9@#$]{6}$", password):
        return False
    else:
        return True