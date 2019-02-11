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


    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

if __name__ ==  '__main__':
    unittest.main()
