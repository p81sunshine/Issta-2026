from collections import defaultdict

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

registered_users = defaultdict(list)

def simple_login_system(operations):
    results = []
    for operation in operations:
        if operation[0] == 'register':
            if registered_users[operation[1]]:
                results.append(f'Error: Username already taken')
            else:
                registered_users[operation[1]].append(User(operation[1], operation[2], operation[3]))
                results.append('User registered successfully')
        elif operation[0] == 'authenticate':
            if registered_users[operation[1]]:
                for user in registered_users[operation[1]]:
                    if user.password == operation[2]:
                        results.append('User authenticated successfully')
                        break
                else:
                    results.append('Error: Invalid username or password')
            else:
                results.append('Error: User not found')
        elif operation[0] == 'get_info':
            if registered_users[operation[1]]:
                user = registered_users[operation[1]][0]
                results.append(f'Username: {user.username}, Email: {user.email}')
            else:
                results.append('Error: User not found')
    return results