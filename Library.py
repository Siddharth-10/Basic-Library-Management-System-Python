from User import User
import os


class Library:

#    def __init__(self):
#        if not os.path.exists(r"C:\Users\Admin\Desktop\Library Management\Library Data"):
#           os.makedirs(r"C:\Users\Admin\Desktop\Library Management\Library Data")
#            with open(r"C:\Users\Admin\Desktop\Library Management\Library Data\User_list.txt", 'w'):
#                pass
#        with open(r"C:\Users\Admin\Desktop\Library Management\Library Data\User_list.txt", 'r') as user_list_file:
#            self.user_list = [x.strip('\n') for x in user_list_file.readlines()]

    def introPage(self):
        print("\n====================================")
        print("Welcome to Library Management System")
        print("====================================")
        exit_condition = False
        while exit_condition == False:
            choice = 0
            print("Choose one of the following options in numbers")
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            try:
                choice = int(input("Waiting for input\n"))
            except ValueError:
                print("(Error) Invalid Input. Enter a number")
            if isinstance(choice,int) and choice is not 0:
                if choice == 1:
                    self.login()
                elif choice == 2:
                    self.register()
                elif choice == 3:
                    print("Thank you for using this software")
                    exit_condition = True
                else:
                    print("Enter Number from the options")

    def login(self):
        print("\n----------------------")
        print("This is the Login Page")
        print("----------------------")

    def register(self):
        print("\n-------------------------")
        print("This is the Register Page")
        print("-------------------------")

        # Entering Name
        name = input("Enter name\n")

        # Entering Age
        exit_condition = False
        while exit_condition == False:
            try:
                age = int(input("Enter Age in numbers\n"))
                if age < 130:
                    exit_condition = True
                else:
                    print("Age should be smaller than 130")
            except ValueError:
                print("Invalid Input. Enter a number")

        # Entering Username
        exit_condition = False
        while exit_condition == False:
            match_found = False
            username = input("Enter Username\n")
            while True:
                try:
                    with open("user.txt", 'r') as user_file:
                        user_list = [x.strip('\n')for x in user_file.readlines()]
                        for user in user_list:
                            file_username = user.split(',')
                            if username == file_username[0]:
                                match_found = True
                except FileNotFoundError:
                    with open("user.txt", 'w'):
                        pass
                    continue
                break
            if match_found == False:
                exit_condition = True
            else:
                print("Username already in use. Try a different one")


        # Entering Password
        password = input("Enter Password\n")

        # Saving User
        User(name, username, str(age), password)


#        with open(r"C:\Users\Admin\Desktop\Library Management\Library Data\User_list.txt", 'a') as user_list_file:
#            user_list_file.write(new_user.username+'\n')
#        with open(r"C:\Users\Admin\Desktop\Library Management\Library Data\User_list.txt", 'r') as user_list_file:
#            self.user_list = [x.strip('\n')for x in user_list_file.readlines()]
        print("user Registered\nGoing back to the main page")

def main():
    library = Library()
    library.introPage()


if __name__ == '__main__':
    main()
