import unittest
from user import User
class TestUnit(unittest.TestCase):
    '''
    Test cloass that defines test cases for the user class behaviours.
    Args:
    unittest.TestCase:TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_User=User("Angela","Karenzi","0787889107","Angelakarenzi5@gmail.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_User.first_name,"Angela")
        self.assertEqual(self.new_User.last_name,"Karenzi")
        self.assertEqual(self.new_User.phone_number,"0787889107")
        self.assertEqual(self.new_User.email,"Angelakarenzi5@gmail.com")


if __name__ == '__main__':
    unittest.main()
