import unittest
from credentials import Credential
from users import User
import pyperclip

class TestCredentials(unittest.TestCase):
    '''
    A test class that defines test cases for credentials class behavior
    Args:
        unittest.TestCase: helps in creating test cases

    '''
    def test_authenticate_user(self):
        '''
        Function to check whether authenicate_user is working properly
        '''
        
        self.new_user = User("badar","badar124")
        self.new_user.save_user()
        another_user = User("salax","salaax234")
        another_user.save_user()

        for user in User.user_list:
            if user.first_name == another_user.first_name and user.password == another_user.password:
                current_user = user.first_name
        return current_user

        self.assertEqual(current_user,Credential.authenticate_user(another_user.password,another_user.first_name))


    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''

        self.new_credential = Credential("kamal","favebook","badar110","badar124")

    def test_init(self):
        '''
        Test case to check if the initialization of account credentials are properly done
        '''

        self.assertEqual(self.new_credential.user_name,"kamal")
        self.assertEqual(self.new_credential.media_site,"favebook")
        self.assertEqual(self.new_credential.account_name,"badar110")
        self.assertEqual(self.new_credential.password,"badar124")


    def test_save_credentials(self):
        '''
        A test case to test whether new credentials are saved into creentials_list
        '''

        self.new_credential.save_credentials()
        twitter = Credential("Badar","Twitter","badar1","badar123")
        twitter.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)


    def tearDown(self):
        '''
        A method clearing the credentials list after testing
        '''
        Credential.credentials_list = []
        User.users_list = []

    def test_display_credentials(self):
        '''
        A test case to check display_credentials, displays the required credentials
        '''

        self.new_credential.save_credentials()
        twitter = Credential("Badar","Twitter","badar","badar110")
        twitter.save_credentials()

        facebook = Credential("Badar","facebook","badruu","badruu110")
        facebook.save_credentials()
        self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)

    def test_find_by_media_site(self):
        '''
        A test case to check whether find_by_media_site returns a credential
        '''

        self.new_credential.save_credentials()
        twitter = Credential("Badar","Twitter","badar","badar110")
        twitter.save_credentials()
        credential_exists = Credential.find_by_media_site("Twitter")
        self.assertEqual(credential_exists,twitter)

    
    def test_copy_credential(self):
        '''
        Test to show whether copy_credential method copies credential correctly
        '''

        self.new_credential.save_credentials()
        twitter = Credential("Badar","Twitter","badar","badar124")
        twitter.save_credentials()
        find_credential = None
        for credential in Credential.user_credentials_list:
            find_credential = Credential.find_by_media_site(credential.media_site)
            return pyperclip.copy(find_credential.password)
        Credential.copy_credential(self.new_credential.media_site)
        self.assertEqual("badar124",pyperclip.paste())
        print(pyperclip.paste())

if __name__ == '__main__':
    unittest.main()