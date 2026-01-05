import sys
class society:
    def __init__(self):

        #Assigning values to attributes
        self.name=''
        self.location=''
        self.loggedin=False
        self.menu()


    def menu(self):
        user_input=input('Welcome to chatbook!! Press the following numbers and continue \n 1. signup\2. Signin\n 3.Write a post\n 4. Exit')

        if(user_input=='3'):
            sys.exit(1)
        
        else:
            self.menu()

obj=society()







