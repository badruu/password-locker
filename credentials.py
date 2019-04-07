import pyperclip
import random
import string
from users import User


class Credential:
    '''
    A class to create account credentials, generate password and save.
    '''

    credentials_list = []
    user_credential_list = []

    @classmethod
    def authenticate_user(cls,first_name,last_name,password):
        '''
        A method that checks if the name and username entered match those in the entries in user_list
        '''

        for user in User.user_list:
            if (user.first_name == first_name and user.last_name == last_name and user.password == password):
                current_user = user.user_name

            return current_user

    def __init__(self,user_name,media_site,account_name,password):
        '''
        A method to define the properties each credential will hold
        '''

        self.user_name = user_name
        self.media_site = media_site
        self.account_name = account_name
        self.password = password