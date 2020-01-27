#! usr/bin/python3
# coding = utf-8

from werkzeug import generate_password_hash, check_password_hash

class User:
    '''
    该类用于创建用户账号
    '''

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = self.save_password(password)

    def check_email(self, email):
        return self.email == email

    def save_password(self, password):
        '''
        生成 hash 密码的方法
        '''
        # TODO
        return generate_password_hash(password)

    def check_password(self, password):
        '''
        检查 hash 密码的方法，返回布尔值
        '''
        # TODO
        return check_password_hash(self.password_hash, password)

def main():
    userList = [] #创建用户列表
    print('■■■■■■■■■■ 欢迎 ■■■■■■■■■■')
    while 1:
        try:
            choose = int(input('''
请选择：
1. 注册
2. 登录
3. 退出
            '''))
            pass
        except ValueError:
            print("Please a int number between 1 and 3!")
            continue
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
            newUser = User(name, email, password)
            userList.append(newUser)
            print("Successful sign up!")

        if choose == 2:
            # 进入登录流程
            print(' 请输入:')
            email = input('email:')
            password = input('password:')

            # 遍历用户列表，判断email、密码是否正确
            # TODO
            inList = False
            for user in userList:
                if user.check_email(email):
                    if user.check_password(password):
                        inList = True
                        print("Successful sign in!")
                        pass
                    pass
                pass
            if inList == False:
                print("Please check up your email and password!")
                pass


        if choose == 3:
            break

if __name__ == '__main__':
    main()

