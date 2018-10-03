import unittest
from ..views import add_new_user, login


class Test_Views(unittest.TestCase):

    def setUp(self):
        self.name = "araali"
        self.password = "farooq"
        self.role = "admin"
        
    def test_add_user(self):
        new_user = add_new_user(self.name, self.password, self.role)
        self.assertEqual(new_user, True)

   
    def test_login(self):
        login_resp =  login(self.name, self.password)
        self.assertEqual(login_resp, True)
