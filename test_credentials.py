import unittest
from credentials import Credential
from users import User

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
        
        self.new_user = User("badar","noor","badar124")
        self.new_user.save_user()
        another_user = User("salax","noor","salaax234")
        another_user.save_user()

        for user in User.user_list:
            if user.first_name == another_user.first_name and user.last_name == another_user.last_name and user.password == another_user.password:
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

if __name__ == '__main__':
    unittest.main()