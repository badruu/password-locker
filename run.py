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

    new_credential = Credential(user_name,site_name,account_name,password)
    return new_credential

def save_credential(credential):
    '''
    function that saves a newly created credential
    '''
    Credential.save_credential(credential)

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
    print("\n")

    while True:
        # print("\n")
        print("-"*20)
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
            password = input("Enter a password -- ").strip()

            save_user(create_user(first_name,last_name,password))

            print("")
            print(f"You have created a new account for: {first_name} {last_name} \n This is your password: {password} ")
            continue
        


if __name__ == "__main__":
    main()