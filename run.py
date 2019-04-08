#!/usr/bin/env python3.6
from passwords import User
from passwords import Credentials
import random
from getpass import getpass

def create_user(username, account):
    '''
    Function to create a new user
    '''
    new_user = User(username, account)
    return new_user


def create_password(account, password):
    '''
    Function to create new password
    '''
    new_pass = Credentials(account, password)
    return new_pass


def save_user(user):
    '''
    Function to save users
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    contact.test_delete_user()

def find_user(account):
    '''
    Function that finds a user by account name and returns the  user
    '''
    return User.find_by_account(account)

def check_existing_user(account):
    '''
    Function that checks if a user exists with that account and returns Boolean
    '''
    return User.user_exists(account)

def display_users():
    '''
    Function that returns all saved users
    '''
    return User.display_users()

def save_password(credentials):
    '''
    Function that saves new password
    '''
    return credentials.save_password()

def generate_password():
    '''
    Function that generates a password for the user
    '''
    return Credentials.generatePassword()

def main():
    print("Hello! Welcome to your Password Locker.Sign up below")
    access_name = input("Password Locker Username: ").lower()
    access_pass = getpass("Password Locker sign up key:  ")
    print("Log in using your sign-up credentials")
    login_name = input("Log in with your username: ").lower()
    login_pass = getpass("Please enter registered password: ")
    if access_pass == login_pass:
        print('\n')
        print(f"Welcome back {access_name}. What would you like to do?")
        print('\n')

    else:
        print("Invalid username or password!")

    while access_pass == login_pass:
            print("Use these short codes : cc - create a new account credentials, dc - display account credentials, fc -find an account's credentials, ex -exit Password Locker ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Contact")
                    print("*"*50)

                    print ("Which account is this?...")
                    account = input()

                    print("What's your username? ...")
                    username = input()

                    print("Would you like a generated password or a customised one? Type c for customised and g for generated...")

                    pass_choice = input().lower()

                    if pass_choice == 'c':
                        print("Enter a password here..")
                        custom_pass = input()

                    elif pass_choice == 'g':
                        print("Here's a password we think will work for you...")
                        print('\n')

                        print(generate_password())




                    save_user(create_user(username, account)) # create and save new contact.
                    save_password(create_password(account, username))#create and save new password
                    print ('\n')
                    print(f"New Credentials for {account} created")
                    print ('\n')

            elif short_code == 'dc':

                    if display_users():
                            print("Here is a list of all your account credentials")
                            print('\n')

                            for user in display_users():
                                    print(f"{user.username}  .....{user.account}")

                            print('\n')
                    else:
                            print('\n')
                            print("Please create an account first.")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the account you want to search for")

                    search_account = input()
                    if check_existing_user(search_account):
                            search_account = find_user(search_account)
                            print(f"Username: {search_account.username}")
                            print('-' * 20)

                            print(f"Account name: {search_contact.account}")

                            print('-' * 20)

                    else:
                            print("That account does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("Invalid input. Please try again")
if __name__ == '__main__':
    main()
