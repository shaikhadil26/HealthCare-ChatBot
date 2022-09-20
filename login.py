import getpass

users_pass = {'abc': '123',
              'xyz': '456'}
ch1 = input('New customer?\n(enter y else press any key): ').lower()
temp = []
if ch1 == 'y':

    while 1:
        user_name = input("enter new username: ")
        if user_name in users_pass:
            print('User already exists')
        else:
            break
    password = getpass.getpass("enter new password: ")
    users_pass[user_name] = password
    print('Account created\nPlease login again\n')

count = 3
name = ''
while count >= 0:
    user = input("enter username: ")
    pass1 = getpass.getpass("enter password: ")
    if user in users_pass and users_pass[user] == pass1:
        name = user
        print('success')
        break
    else:
        print(f'Incorrect id/pass\nYou have {count} valid retries left')
        count -= 1
