
class Account():
    id = None
    name = None
    account_number = None

    def __init__(self, name, account_number, id = None) -> None:
        self.id = id
        self.name = name
        self.account_number = account_number

