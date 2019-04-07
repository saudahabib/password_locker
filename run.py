#!/usr/bin/env python3.6
from passwords import User

def create_user(username, account):
    '''
    Function to create a new user
    '''
    new_user = User(username, account)
    return new_user

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


def main():
    print("Hello! Welcome to your Password Locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new account credentials, dc - display account credentials, fc -find an account's credentials, ex -exit Password Locker ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Contact")
                    print("-"*10)

                    print ("Which account is this?...")
                    account = input()

                    print("What's your username? ...")
                    username = input()


                    save_user(create_user(username, account)) # create and save new contact.
                    print ('\n')
                    print(f"New Credentials for {account} created")
                    print ('\n')

            elif short_code == 'dc':

                    if display_users():
                            print("Here is a list of all your account credentials")
                            print('\n')

                            for user in display_users():
                                    print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

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

                            print(f"Account name: {search_contact.phone_number}")

                            print('-' * 20)

                    else:
                            print("That account does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
    main()
