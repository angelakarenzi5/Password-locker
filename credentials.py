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