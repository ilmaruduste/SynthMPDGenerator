from abc import ABC, abstractmethod
from . import cell_network

class User(ABC):

    def __init__(self, id, cell_network = None):
        self.id = id
        self.profile = "User"
        
        if cell_network != None:
            self.cell_network = cell_network

    # TODO: Implement possibility to use generateMeaningfulLocations without upper passing of CellNetwork variable
    # Refer to self.cell_network
    def generateMeaningfulLocations(self, cell_network):
        print(f"Generating meaningful locations for user {self.id} of profile {self.profile}.")
        self.home_cell = cell_network.getRandomCell()

        print(f"User {self.id}'s home cell is cellid: {self.home_cell.cellid}, with latitude {self.home_cell.latitude} and longitude {self.home_cell.longitude}")


class GeneralUser(User):
    '''
    Use this for generalising a population or if you don't want any special classes.
    '''

    def __init__(self, id):
        self.id = id
        self.profile = "GeneralUser"

    pass