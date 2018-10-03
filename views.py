from models import User, Score

all_users = []


def add_new_user(name, password, role):
    new_user = User(name, password, role)
    all_users.append(new_user)
    return True


def login(name, password):
    if any(user["name"] == name for user in all_users):
        if any(user["password"] == password for user in all_users):
            return True
        return False
        
score = []

def add_score():
    new_score = Score( failure, unsatisfied,nuetral , satisfied, very_satisfised)
    score.append(new_score)
    return True

