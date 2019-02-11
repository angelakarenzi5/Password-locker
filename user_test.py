import unittest # Importing the unittest module from unit import Unit #Importing the unit class

class TestUnit(unittest.TestCase):
    '''
    Args:
    unittest.TestCase:TestCase class that helps in creating test cases
    '''

    # Items up here ......

     def setUp(self):
         '''
         Set up method to run before each test cases.
         '''
         self.new_user = User("Angela","Karenzi","0787889107","angelakarenzi5@gmail.com") # create user object