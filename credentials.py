class Credentials: 
    """
     Class that generates new instances of credentials
    """
    credentials_list = [] #Empty credentials list
    def __init__(self, website_name,account_name,password):
        
        # docstring removed for simplicity

        self.website_name = website_name
        self.account_name = account_name
        self.password = password

    credentials_list = [] # Empty credentials list
 # Init method up here
    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)