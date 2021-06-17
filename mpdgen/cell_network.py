import pandas as pd
import random


class Cell:
    def __init__(self, cellid, latitude, longitude):
        self.cellid = cellid
        self.latitude = latitude
        self.longitude = longitude

class CellNetwork:

    def __init__(self, cells_filepath):

        # TODO: static variables atm, this could be specified in config later on
        cells_df = pd.read_csv(cells_filepath, sep = ';')

        self.cells_df = cells_df
        self.cells = None

    def generateCellNetwork(self):

        # TODO: Think of a better system to specify column names
        # TODO: Make 
        # TODO: This list comprehension for sure could be optimised

        # Create a Cell object for each cell in ref data
        cells_array = [Cell(row[0], row[1], row[2]) for row in zip(self.cells_df['cell'], self.cells_df['lat'], self.cells_df['lon'])]
        self.cells = cells_array

    def getRandomCell(self):

        if self.cells == None:
            self.generateCellNetwork()

        random_number = random.randint(0, len(self.cells))

        return self.cells[random_number]
