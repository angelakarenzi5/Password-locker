#!/usr/bin/env python3.6
from user import User
from Credentials import Credentials

def create_user(fname,lname,email,phone,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,email,phone,password)
    return new_user

def create_Credentials(website_name,user_name,password):
    '''
    Function to create a new Credentials
    '''
    new_Credentials = Credentials(website_name,user_name,password)
    return new_Credentials

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def save_Credentials(Credentials):
    '''
    Function to save Credentials
    '''
    Credentials.save_Credentials()

def del_Credentials(Credentials):
    '''
    Function to delete a Credentials
    '''
    Credentials.delete_Credentials()

def find_Credentials(name):
    '''
    Function that finds a Credentials by name and returns the Credentials
    '''
    return Credentials.find_by_name(name)

def check_existing_users(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return Contact.contact_exist(number)

def check_existing_Credentials(website_name):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return Credentials.Credentials_exist(website_name)


def display_Credentials():
    '''
    Function that returns all the saved Credentials
    '''
    return Credentials.display_Credentials()

def main():
         print("Hello Welcome to your user list. What is your name?")
         user_name = input()

         print(f"Hello {user_name}. what would you like to do?")
         print('\n')

         while True:
                    print("Use these short codes : cc - create a new user, dc - display users, fc -find a user, ex -exit the user list, cd - Create credentials, fcc - find credentials ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New User")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Email address ...")
                            e_address = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Password ...")
                            password = input ()                            


                            save_user(create_user(f_name,l_name,e_address,p_number,password)) # create and save new user.
                            print ('\n')
                            print(f"New User {f_name} {l_name} created")
                            print ('\n')



                    # elif short_code == 'login':
                    #     print("Enter username and password")
                    #     username=input()
                    #     password=input()
                    #     if username==f_name and password== password:
                    #         print("login successful")
                    #         short_code1=input()
                    elif short_code=='cd':
                                print("Enter website name")
                                website=input()
                                print("Enter username")
                                usern=input()

                                print("Enter password")
                                passw=input()
                                save_Credentials(create_Credentials(website,usern,passw))




                       
                    elif short_code == 'dc':

                                 if display_Credentials():
                                    print("Here is a list of all your Credentials")
                                    print('\n')

                                    for Credentials in display_Credentials():
                                            print(f"{Credentials.website_name} {Credentials.user_name} .....{Credentials.password}")

                                    print('\n')
                                 else:
                                    print('\n')
                                    print("You dont seem to have any Credentials saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_users(search_number):
                                    search_user = find_user(search_number)
                                    print(f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_user.phone_number}")
                                    print(f"Email address.......{search_user.email}")
                            else:
                                    print("That user does not exist")

                    elif short_code == 'fcc':

                            print("Enter the website name you want to search for")

                            search_website_name = input()
                            if check_existing_Credentials(search_website_name):
                                    search_Credentials = find_Credentials(search_website_name)
                                    print(f"{search_Credentials.website_name} {search_Credentials.website_name}")
                                    print('-' * 20)

                                    print(f"website_name.......{search_Credentials.website_name}")
                                    print(f"password.......{search_Credentials.password}")
                            else:
                                    print("That Credentials does not exist")


                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
                    

if __name__ == '__main__':
     main()