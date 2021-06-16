from abc import ABC, abstractmethod
from . import cell_network

# TODO: Might have to do some refactoring thanks to naming conventions
# In Python, functions are written as lower_case(), but here I wrote them like it usually is in Java.

class User(ABC):

    def __init__(self, id, cell_network = None):
        self.id = id
        self.profile = "User"
        
        if cell_network != None:
            self.cell_network = cell_network

    # TODO: Implement possibility to use generateMeaningfulLocations without upper passing of CellNetwork variable
    # Refer to self.cell_network
    def generateMeaningfulLocations(self, cell_network):
        '''
        Since this is basically a dummy user, then the meaningful locations here are chosen randomly.
        '''

        print(f"\nGenerating meaningful locations for user {self.id} of profile {self.profile}.")
        
        self.home_cell = cell_network.getRandomCell()
        print(f"User {self.id}'s home cell is cellid: {self.home_cell.cellid}, with latitude {self.home_cell.latitude} and longitude {self.home_cell.longitude}")
        
        self.work_cell = cell_network.getRandomCell()
        print(f"User {self.id}'s work cell is cellid: {self.work_cell.cellid}, with latitude {self.work_cell.latitude} and longitude {self.work_cell.longitude}")


class GeneralUser(User):
    '''
    Use this for generalising a population or if you don't want any special classes.
    '''

    def __init__(self, id):
        self.id = id
        self.profile = "GeneralUser"

    pass