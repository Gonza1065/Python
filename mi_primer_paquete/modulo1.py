data_base = {}


class Client:
    def __init__(self, name, username, password, address):
        self.name = name
        self.username = username
        self.password = password
        self.address = address

    def register_client():
        acc = 1
        while acc <= 5:
            print(f"Client Number: {acc}")
            name = input("Insert your name: ")
            username = input("Insert your username: ")
            password = input("Insert your password: ")
            address = input("Insert your address: ")
            data_base[name] = {
                "username": username,
                "password": password,
                "address": address,
            }
            acc = acc + 1

    def show_clients():
        for name, info in data_base.items():
            print(
                f"Name: {name}\n Username: {info['username']}\n Password: {info['password']}\n Address: {info['address']}"
            )
