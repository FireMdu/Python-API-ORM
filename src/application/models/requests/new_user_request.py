

class NewUserRequest():
    name = None
    username = None
    password = None
    account_number = None

    def __init__(self, name, username, password, account_number) -> None:
        self.name = name
        self.username = username
        self.password = password
        self.account_number = account_number