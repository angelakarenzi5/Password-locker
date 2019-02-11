import unittest # Importing the unittest module from unit import Unit #Importing the unit class
from user import User # Importing the contact class

class TestUnit(unittest.TestCase):
    '''
    Args:
    unittest.TestCase:TestCase class that helps in creating test cases
    '''

    # Items up here ......

     def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Angela")
        self.assertEqual(self.new_user.last_name,"Karenzi")
        self.assertEqual(self.new_user.phone_number,"0787889107")
        self.assertEqual(self.new_user.email,"angelakarenzi5@gmail.com")


if __name__ == '__main__':
    unittest.main()
