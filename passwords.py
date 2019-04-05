class User :
    '''
    Class that generates new instances of a User
    '''
    user_list = []
    def __init__(self, username, account):
        self.username = username
        self.account = account

    def save_user(self):
        '''
        save_user method saves user names into the user list
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        delete_contact method deletes the user info from contact_list
        '''
