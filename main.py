# Simulated login system

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Database of authorized users
authorized_users = [
    User("admin", "adminpassword"),
    User("user1", "user1password"),
    User("user2", "user2password")
]

def login(username, password):
    for user in authorized_users:
        if user.username == username and user.password == password:
            return True
    return False

# Main program
if __name__ == "__main__":
    print("Welcome to the secure system.")
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if login(username, password):
        print("Login successful. You have access.")
    else:
        print("Login failed. Unauthorized access.")

