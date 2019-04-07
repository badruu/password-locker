
class User:
    '''
    Class that generates instances of users.
    '''

    user_list = []

    def __init__(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        method that saves objects intp user list
        '''

        User.user_list.append(self)

if __name__ == '__main__':
    main()