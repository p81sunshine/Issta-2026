# connect_and_authenticate(mongo_host, mongo_port, mongo_user, mongo_pwd, mongo_auth):
# Simulates connecting to a MongoDB database and authenticating a user.
#
# Parameters:
#   mongo_host (string): The host address of the MongoDB server.
#   mongo_port (int): The port number of the MongoDB server.
#   mongo_user (string): The username for authentication.
#   mongo_pwd (string): The password for authentication.
#   mongo_auth (string): The authentication source.
#
# Returns:
#   (string) A message indicating the result of the connection and authentication process.
def connect_and_authenticate(mongo_host, mongo_port, mongo_user, mongo_pwd, mongo_auth):
    # Validate inputs
    if mongo_host is None or mongo_host == '':
        return 'Connection failed'
    if mongo_port is None or mongo_port < 1 or mongo_port > 65535:
        return 'Connection failed'
    if mongo_user is None or mongo_user == '':
        return 'Authentication failed: invalid username'
    if mongo_pwd is None or mongo_pwd == '':
        return 'Authentication failed: invalid password'
    if mongo_auth is None or mongo_auth == '':
        return 'Authentication failed: invalid source'

    # Simulate connection to MongoDB
    if mongo_host == 'localhost' and mongo_port == 27017:
        return 'Connection to localhost at port 27017 is established'
    else:
        return 'Connection failed'

    # Simulate authentication to MongoDB
    if mongo_user == 'admin' and mongo_pwd == 'password123' and mongo_auth == 'admin_db':
        return 'Connection successful and authenticated to linkedbooks_dev'
    else:
        return 'Authentication failed'

# Tests