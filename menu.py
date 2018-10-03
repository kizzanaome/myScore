from views import add_new_user, login

import sys


class Menu:
    '''display'''
    def __init__(self):
        self.choices = {
            "1": self.new_user
        }

    def display_menu(self):
        '''Prints to the console options
           Users can select
        Args:
            None
        '''
        print('''
        User Menu (str):
        1. Add User
        2. Login
        3. View Users
        4. Quit
        ''')

    def run(self):
        '''Display the menu and respond to 
           user input choices, 
           a user can choice any of the three printed choices
           on the console.
        '''
        while True:
            '''runs as long as the user doesn't
               choice quit: option three 
            '''
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
    def new_user(self):
        '''Takes user input and adds to the list'''
        name = input("Enter name: ")
        password = input("Enter password: ")
        role = input("enter role: ")
        add_new_user(name, password, role)
        print("User Registration successful")

   

if __name__ == '__main__':
    Menu().run()
