import datetime
import uuid


class User(object):
    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role

    def __getscore__(self, score):
        return getattr(self, score)

    def __repr__(self):
        return repr(self.__dict__)


class Score(object):
    def __init__(self, failure, unsatisfied,nuetral , satisfied, very_satisfised):
        self.failure = failure
        self.unique_code = uuid.uuid4()
        self. unsatisfied =  unsatisfied
        self.nuetral = nuetral
        self.created_at = datetime.datetime.now()
        self.satisfied= satisfied
        self.very_satisfied = very_satisfised
