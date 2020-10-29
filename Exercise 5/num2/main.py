n = int(input("Enter number of items: "))
users ={}
username = str(input("Enter your login name by comma: ")).split(",")
password = str(input("Enter password by comma: ")).split(",")

def for_dict():
    for x in range(n):
        users[username[x]] = password[x]
    print("users = ", users)

for_dict()


def accept_login(users, username, password):
    for_username = input("Enter your username: ")
    for_password = input("Enter the password: ")
    if for_username in users.keys() and for_password == users[for_username]:
        return True
    else:
        return False

def main():
    print(accept_login(users, username, password))

main()




