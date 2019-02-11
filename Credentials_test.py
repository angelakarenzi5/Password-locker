import unittest
from Credentials import Credentials
class TestUnit(unittest.TestCase):
    '''
    Test class that defines test cases for the Credentials class behaviours.
    Args:
    unittest.TestCase:TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_Credentials=Credentials("angelakarenzi5@gmail.com","angelakarenzi5","0787889107")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_Credentials.website_name,"angelakarenzi5@gmail.com")
        self.assertEqual(self.new_Credentials.user_name,"angelakarenzi5")
        self.assertEqual(self.new_Credentials.password,"0787889107")
    

    def test_save_Credentials(self):
        '''
        test_save_Credentials test case to test if the Credentials object is saved into
        the Credentials list
        '''
        self.new_Credentials.save_Credentials() # saving the new Credentials
        self.assertEqual(len(Credentials.Credentials_list),1)

    # Items up here...

    def test_save_multiple_Credentials(self):
        '''
        test_save_multiple_Credentials to check if we can save multiple Credentials
        objects to our Credentials_list
        '''
        self.new_Credentials.save_Credentials()
        test_Credentials = Credentials("angelakarenzi5@gmail.com","angelakarenzi5","0787889107") # new Credentials
        test_Credentials.save_Credentials()
        self.assertEqual(len(Credentials.Credentials_list),3)

    # setup and class creation up here

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.Credentials_list = []

    # other test cases here
    def test_save_multiple_Credentials(self):
            '''
            test_save_multiple_Credentials to check if we can save multiple Credentials
            objects to our Credentials_list
            '''
            self.new_Credentials.save_Credentials()
            test_Credentials = Credentials("angelakarenzi5@gmail.com","angelakarenzi5","0787889107") # new credentials
            test_Credentials.save_Credentials()
            self.assertEqual(len(Credentials.Credentials_list),2)

    # More tests above
    def test_delete_Credentials(self):
            '''
            test_delete_Credentials to test if we can remove a credentials from our credentials list
            '''
            self.new_Credentials.save_Credentials()
            test_Credentials = Credentials("angelakarenzi5@gmail.com","angelakarenzi5","0787889107") # new Credentials
            test_Credentials.save_Credentials()

            self.new_Credentials.delete_Credentials()# Deleting a Credentials object
            self.assertEqual(len(Credentials.Credentials_list),1)

            def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0711223344")

        self.assertEqual(found_contact.email,test_contact.email)

    
if __name__ ==  '__main__':
    unittest.main()
