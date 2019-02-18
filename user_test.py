import unittest
from user import User
class TestUnit(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
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

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_User.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    # Items up here...

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_User.save_user()
        test_user = User("Angela","Karenzi","0787889107","angelakarenzi5@gmail.com") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),3)

    # setup and class creation up here

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    # other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_User.save_user()
            test_user = User("Angela","Karenzi","0787889107","angelakarenzi5@gmail.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_User.save_user()
        test_user = User("Angela","Karenzi","0787889107","angelakarenzi5@gmail.com") # new user
        test_user.save_user()

        User_exists = User.user_exist("0787889107")

        self.assertTrue(User_exists)

    def test_display_all_user(self):
        '''
        method that returns a list of all User saved
        '''

        self.assertEqual(User.display_user(),User.user_list)
    
if __name__ ==  '__main__':
    unittest.main()
