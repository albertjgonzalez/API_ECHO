import json


class Client:
    def __init__(self, data):
        self.id = data["id"]
        self.dev = data["dev"]
        self.preprod = data["preprod"]
        self.prod = data["prod"]

    def get_endpoint(self, environment, endpoint_type):
        return self.__dict__[environment][endpoint_type]


def load_clients():
    with open("../data/clients.json", "r") as file:
        data = json.load(file)
    return [Client(client_data) for client_data in data["clients"]]
