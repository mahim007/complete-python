username = input("enter username: ")
password = input("enter password: ")

password_length = len(password)
password_star = '*' * password_length

print(f'hey {username}, your password {password_star} is {password_length} characters long!')
