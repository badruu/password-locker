import pyperclip
import random
import string
from users import User


class Credential:
    '''
    A class to create account credentials, generate password and save.
    '''

    credentials_list = []
    user_credentials_list = []

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

    def save_credentials(self):
        '''
        method that saves newly created credentials
        '''

        Credential.credentials_list.append(self)

    def generate_password(self):
        '''
        method that generates a random password
        '''
        letters = string.ascii_letters + string.digits
        gen_pass = ''.join(random.choice(letters) for i in range (10))
        return gen_pass

    @classmethod
    def display_credentials(cls,user_name):
        '''
        A method to show list of credentials saved
        '''

        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def find_by_media_site(cls,media_site):
        '''
        A method that returns the media site by taking in name of the site
        '''

        for credential in cls.credentials_list:
            if credential.media_site == media_site:
                return credential

    @classmethod
    def copy_credential(cls,media_site):
        '''
        Method that copies credential's password
        '''

        find_credential = Credential.find_by_media_site(media_site)
        return pyperclip.copy(find_credential.password)
                