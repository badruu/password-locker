#!/usr/bin/env python3.7

from users import User
from credentials import Credential
import pyperclip

def create_user(fname,lname,password):
    '''
    function that creates a new user account
    '''

    new_user = User(fname,lname,password)
    return new_user

def save_user(user):
    '''
    function that saves a new user account
    '''

    User.save_user(user)

def authentication(first_name,password):
    '''
    function to authenticate a user that they have an account
    '''

    authenticate_user = Credential.authenticate_user(first_name,password)
    return authenticate_user

def generate_password():
    '''
    Function to generate a password randomly
    '''

    gen_pass = Credential.generate_password()
    return gen_pass

def create_credential(user_name,media_site,account_name,password):
    '''
    function creating a new credential
    '''

    new_credential = Credential(user_name,media_site,account_name,password)
    return new_credential

def save_credential(credential):
    '''
    function that saves a newly created credential
    '''
    Credential.save_credentials(credential)

def display_credentials(user_name):
    '''
    function to display credentials saved by a user
    '''

    return Credential.display_credentials(user_name)

def copy_credential(media_site):
    '''
    function to copy a credential on the clipboard
    '''

    return Credential.copy_credential(media_site)


def main():
    print("\n")
    print("Hello there (!) \n welcome to password locker!")

    while True:
        # print("\n")
        print("-"*50)
        print("""What would you like to do?
         \n
          Use the codes below
           \n
            1) ca- to create an account
            2) lg - to login to your account
            3) ex - Exit
        """)
        short_code = input("Enter a code: ").strip().lower()

        if short_code == "ex":
            break

        elif short_code == "ca":
            print("-"*50)
            print("")
            print("To create a new account, fill in the following: ")
            first_name = input("Enter your first name -- ").strip()
            last_name = input("Enter your last name -- ").strip()

            while True:
                print(" ")
                print("-"*50)
                print("""How would you like you password to be genrated:
                    1) exp - for enter an existing password
                    2) gn - for generate a password automatically
                    3) ex - exit
                """)
                password_choice = input("Enter an option: ").lower().strip()
                print("-"*50)
                if password_choice == "exp":
                    print(" ")
                    password = input("Enter your password: ").strip()
                    break

                elif password_choice == "gn":
                    password = generate_password()
                    break

                elif password_choice == "ex":
                    break

                else:
                    print("Damn! Why don\'nt you follow simple instruction(!)")

            # password = input("Enter a password -- ").strip()
            # password = password_choice

            save_user(create_user(first_name,last_name,password))

            print("")
            print("-"*50)
            print(f"You have created a new account for: {first_name} {last_name} \n This is your password: {password} ")
            

        elif short_code == "lg":
            print("-"*50)
            print("\n")
            print("To login, provide you account information: ")

            user_name = input("Enter your first name -- ").strip()
            password = input("Enter your password -- ").strip()

            user_exists = authentication(user_name,password)

            if user_exists == user_name:
                print(" ")
                print(f"Welcome {user_name}. We are glad to have you again.")
                print(" ")
                while True:
                    print("-"*50)
                    # print("Navigation: \n cc")
                    print("""Choose an Option from the list below: \n
                        1) cc - create a credential
                        2) dc - display credentials
                        3) cp - copy password of a credential
                        4) ex - exit
                    """)
                    short_code = input("Option chosen: ").lower().strip()
                    print("-"*50)

                    if short_code == "ex":
                        print(" ")
                        print(f"Goodluck {user_name}")
                        break

                    elif short_code == "cc":
                        print(" ")
                        print("Enter the details of the account you would like to create:")
                        print("-"*50)
                        media_site = input("Enter the site\'s name -- ").strip()
                        account_name = input("Enter your account name -- ").strip()
                        while True:
                            print(" ")
                            print("-"*50)
                            print("""How would you like you password to be genrated:
                                1) exp - for enter an existing password
                                2) gn - for generate a password automatically
                                3) ex - exit
                            """)
                            password_choice = input("Enter an option: ").lower().strip()
                            print("-"*50)
                            if password_choice == "exp":
                                print(" ")
                                password = input("Enter your password: ").strip()
                                break

                            elif password_choice == "gn":
                                password = generate_password()
                                break

                            elif password_choice == "ex":
                                break

                            else:
                                print("Damn! Why don\'nt you follow simple instruction(!)")

                        save_credential(create_credential(user_name,media_site,account_name,password))
                        print(" ")
                        print(f"""You have created the following credential:
                        Media site: {media_site}
                        Account name: {account_name}
                        Password: {password}""")
                        print(" ")

                    elif short_code == "dc":
                        print(" ")
                        if display_credentials(user_name):
                            print("Below is a list of all your credentials")
                            print(" ")
                            for credential in display_credentials(user_name):
                                print(f"""
                                media site: {credential.media_site}
                                account name: {credential.account_name}
                                password: {credential.password}
                                """)
                            print(" ")

                        else: 
                            print(" ")
                            print("You haven\'t yet saved any credentials. \n TIP: Use cc to create and save a new credential")
                            print(" ")

                    elif short_code == "cp":
                        print(" ")
                        chosen_site = input("Enter the site name for the credential password you want to copy: ")
                        # if chosen_site = Credential.media_site:

                        copy_credential(chosen_site)

                        
                        print(" ")
                        # print(f"The password for {chosen_site} has been copied. \n This is the password: {copy_credential.password}")

                    else: 
                        print("""You don\'t seem to follow instructions, do you?
                        Enter choices from the given options only!!
                        """)
                        break

            else:
                print("-"*50)
                print(" ")
                print("Try again or create an account!")
                print(" ")

        else: 
            print(" ")
            print("You haven\'nt entered options provided")



if __name__ == "__main__":
    main()