class User: 
    """
    Class that generates new instances of users
    """
    user_list = [] #Empty user list
    def __init__(self, first_name,last_name,email,phone_number, password):
        
        # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password

        user_list = [] # Empty userlist
 # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    @classmethod
    def user_exist(cls,number):
        '''
        Method that checks if a user exists from the user list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                    return True

        return False
        
    @classmethod
    def display_user(cls):
        '''
        method that returns the User list
        '''
        return cls.user_list
       