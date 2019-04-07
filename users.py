
class User:
    '''
    Class that generates instances of users.
    '''

    user_list = []

    def __init__(self,user_name,password):

        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        method that saves objects intp user list
        '''

        User.user_list.append(self)

if __name__ == '__main__':
    main()