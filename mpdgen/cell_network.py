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

    def generateCellNetwork(self):

        # TODO: Think of a better system to specify column names
        cells_array = [Cell(row['cell'], row['lat'], row['lon']) for row in self.cells_df]
        self.cells = cells_array

    def getRandomCell(self):

        random_number = random.randint(0, len(self.cells))

        return self.cells[random_number]
