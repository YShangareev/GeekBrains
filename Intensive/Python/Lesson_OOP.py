class User():
    user_count = 0

    def __init__(self, name, login, password):
        User.user_count += 1
        self.name = name
        self.__login = login
        self.__password = password


    # def get_login(self):
    #     return self.__login
    #
    # def set_password(self, value):
    #     if len(value) >= 5:
    #         self.__password = value
    #
    # login_and_password = property(fget=get_login, fset=set_password)

    @property
    def login(self):
        return self.__login
    try:
        @password.setter
        def password(self, value):
            if len(value) >= 5:
                self.__password = value
            else:
                print('Invalid password length(mast be lenght >= 5 symbol')
    except NameError:
        ''

    def show_info(self):
        return f'User name - {self.name}, User Login - {self.__login}'

user1 = User(name='Alexey', login='ASmirnov', password='12345')
user2 = User(name='Andrey', login='AAlekseev', password='67890')
user3 = User(name='Ivan', login='IFedorov', password='qwerty')
users = User.user_count

class SuperUser(User):
    admin_count = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self.__role = role
        SuperUser.admin_count += 1

    def show_info(self):
        return f'User login - {self.__login}, User role - {self.__role}'

# user1 = User(name='Alexey', login='ASmirnov', password='12345')
# user2 = User(name='Andrey', login='AAlekseev', password='67890')
# user3 = User(name='Ivan', login='IFedorov', password='qwerty')
admin = SuperUser(name='Liana', login='LKarimova', password='secure', role='admin')
# users = User.user_count
admins = SuperUser.admin_count
print(f'Всего пользователей - {users}')
print(f'Всего администраторов - {admins}')

print()
