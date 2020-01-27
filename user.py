#! usr/bin/python3
# coding = utf-8

from werkzeug import generate_password_hash, check_password_hash

class User:
    ''' 该类用于创建用户账号
    '''

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = self.save_password(password)

    def check_email(self, email):
        return self.email == email

    def save_password(self, password):
        '''生成 hash 密码的方法
        '''
        # TODO

    def check_password(self, password):
        '''检查 hash 密码的方法，返回布尔值
        '''
        # TODO

def main():
    userList = [] #创建用户列表
    print('■■■■■■■■■■ 欢迎 ■■■■■■■■■■')
    while 1:
        choose = int(input('''
        请选择：
        1. 注册
        2. 登录
        3. 退出
        '''))
        if choose == 1:
            # 进入注册流程
            print(' 请输入:')

            # 获取用户输入
            name = input('name:')
            email = input('email:')
            password = input('password:')

            # 根据用户输入，完成：
            # 1. 创建新用户
            # 2. 生成 hash 密码
            # 3. 将用户存入用户列表
            # TODO
            newUser = 

        if choose == 2:
            # 进入登录流程
            print(' 请输入:')
            email = input('email:')
            password = input('password:')

            # 遍历用户列表，判断email、密码是否正确
            # TODO

        if choose == 3:
            break

if __name__ == '__main__':
    main()
