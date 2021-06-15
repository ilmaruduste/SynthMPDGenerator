from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, id):
        self.id = id
        self.profile = "User"


    def generateMeaningfulLocations(self):
        print(f"Generating meaningful locations for user {self.id} of profile {self.profile}.")

class GeneralUser(User):
    '''
    Use this for generalising a population or if you don't want any special classes.
    '''

    def __init__(self, id):
        self.id = id
        self.profile = "GeneralUser"


    pass