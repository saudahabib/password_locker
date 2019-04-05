import unittest
from passwords import User
import pyperclip

class TestUser(unittest.TestCase):
    '''
    Test class that defines tests for User class behaviours
    Args:
        unittest.TestCase: TestCase class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test instance
        '''
        self.new_user = User("Saudahabib","Instagram")# Instance of class User

        def test_init(self):
            '''
            Test case to test if object is initialised properly
            '''

            self.assertEqual(self.new_user.username, "Saudahabib")
            self.assertEqual(self.new_user.account, "Instagram")

if __name__ == '__main__':
    unittest.main()
