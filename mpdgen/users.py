from abc import ABC, abstractmethod
from . import cell_network
import pandas as pd
import random
import datetime

# TODO: Might have to do some refactoring thanks to naming conventions
# In Python, functions are written as lower_case(), but here I wrote them like it usually is in Java.

class User(ABC):

    def __init__(self, id, cell_network = None):
        self.id = id
        self.profile = "User"
        self.cell_network = cell_network
        self.home_cell = None
        self.work_cell = None

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

    def generateCDR(self, time_period):
        date_beginning = time_period[0]
        date_end = time_period[1]

        date_range = pd.date_range(date_beginning, date_end, freq = 'd')

        cdr_data_array = []

        for day in date_range:
            # Adding morning home, day work and evening home

            # TODO: Very primitive solution to generating timestamps atm, try to fix this!
            morning_timestamp = datetime.datetime(day.year, day.month, day.day, random.randint(6, 9), random.randint(0, 59), random.randint(0, 59))
            day_timestamp = datetime.datetime(day.year, day.month, day.day, random.randint(10, 17), random.randint(0, 59), random.randint(0, 59))
            evening_timestamp = datetime.datetime(day.year, day.month, day.day, random.randint(18, 23), random.randint(0, 59), random.randint(0, 59))

            cdr_data_array.append([self.id, str(morning_timestamp), self.home_cell.cellid])
            cdr_data_array.append([self.id, str(day_timestamp), self.work_cell.cellid])
            cdr_data_array.append([self.id, str(evening_timestamp), self.home_cell.cellid])
        
        cdr_data = pd.DataFrame(cdr_data_array, columns = ['user', 'timestamp', 'cellid'])

        self.cdr_data = cdr_data
        print(f"CDR data generated for User {self.id}, between dates {date_beginning} and {date_end}, with {len(cdr_data)} rows.")


class GeneralUser(User):
    '''
    Use this for generalising a population or if you don't want any special classes.
    '''

    def __init__(self, id):
        self.id = id
        self.profile = "GeneralUser"

    pass