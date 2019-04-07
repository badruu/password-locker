import unittest
from users import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behavior.

    Args:
        unittest.Testcase: helps in creating test cases
    '''

    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_user = User("badar","badar124")

    def test_init(self):
        '''
        test case to check if the object is initialized properly.
        '''
        self.assertEqual(self.new_user.user_name,"badar")
        self.assertEqual(self.new_user.password,"badar124")

    def test_save_user(self):
        '''
            test case to check if the user object is saved into the user list
        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

if __name__ =='__main__':
    unittest.main()
