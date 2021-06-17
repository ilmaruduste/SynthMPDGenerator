from abc import ABC, abstractmethod
from . import cell_network
import pandas as pd
import random
import datetime
import numpy as np

# TODO: Might have to do some refactoring thanks to naming conventions
# In Python, functions are written as lower_case(), but here I wrote them like it usually is in Java.

class User(ABC):

    def __init__(self, id, cell_network = None):
        self.id = id
        self.profile = "User"
        self.cell_network = cell_network
        self.home_cell = None
        self.work_cell = None
        self.regular_cell_array = []

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

    def generateCDR(self, conf_cdr_generation):
        date_beginning = conf_cdr_generation['TIME PERIOD'][0]
        date_end = conf_cdr_generation['TIME PERIOD'][1]

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

    def __init__(self, id, cell_network = None):
        self.id = id
        self.profile = "GeneralUser"
        self.cell_network = cell_network
        self.home_cell = None
        self.work_cell = None
        self.regular_cell_array = []

    def generateMeaningfulLocations(self, cell_network):
        '''
        Here we'll say that the user has 1 - 5 cells that they visit regularly that are not work nor home cells
        '''

        print(f"\nGenerating meaningful locations for user {self.id} of profile {self.profile}.")
        
        self.home_cell = cell_network.getRandomCell()
        print(f"User {self.id}'s home cell is cellid: {self.home_cell.cellid}, with latitude {self.home_cell.latitude} and longitude {self.home_cell.longitude}")
        
        self.work_cell = cell_network.getRandomCell()
        print(f"User {self.id}'s work cell is cellid: {self.work_cell.cellid}, with latitude {self.work_cell.latitude} and longitude {self.work_cell.longitude}")

        # Assigning the number of regularly visited cells for the user
        regular_cell_count = random.randint(1,5)
        regular_cell_array = []

        for count in range(regular_cell_count):
            regular_cell_array.append(cell_network.getRandomCell())

        self.regular_cell_array = regular_cell_array
        print(f"User {self.id}'s regular cell array: {[cell.cellid for cell in self.regular_cell_array]}")


    def generateCDR(self, conf_cdr_generation):
        '''
        The method here takes into account the CDR tendencies of the general population.
        e.g. more activity during mondays and fridays, less so during other weekends and even less so during the weekends
        e.g. almost no activity during the night and the activity peak is during the day 
        '''

        date_beginning = conf_cdr_generation['TIME PERIOD'][0]
        date_end = conf_cdr_generation['TIME PERIOD'][1]

        date_range = pd.date_range(date_beginning, date_end, freq = 'd')

        cdr_data_array = []

        # TODO: Implement weekend transposing feature (like it is in conf)
        # i.e. When weekend is [Sat, Sun], then Monday is 0, ..., Sun is 6
        # and when weekend is [Fri, Sat], then Sundary is 0, ..., Sat is 6


        for day in date_range:
            daily_mean = int(round(np.random.normal(loc = conf_cdr_generation['DAY ACTIVITY MEAN'][day.weekday()],
                                            scale = conf_cdr_generation['DAY ACTIVITY STANDARD DEVIATION'][day.weekday()],
                                            size = 1)[0] * conf_cdr_generation['DATA DENSITY'], 0))

            # Row for debugging daily records
            # print(f"{day.strftime('%A')} got {daily_mean} records.")

            for index in range(daily_mean):
                # TODO: Add some kind of activity distribution relating to time (e.g. no activity during night, more activity during day)
                
                timestamp = datetime.datetime(day.year, day.month, day.day, random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))

                # TODO: Add some kind of model for predicting whether the user is at home, work or another regular cell dependant on the time of day
                #       This model should have a condition that when someone goes to a meaningful location, they don't randomly switch between these meaningful
                #       locations during the day. They should stay put at one cell for some time. Maybe some kind of HMM would help here with state transitions?
                possible_locations = [self.home_cell, self.work_cell]
                possible_locations.extend(self.regular_cell_array) # extend() gives list values without list

                current_location = random.choice(possible_locations)

                cdr_data_array.append([self.id, str(timestamp), current_location.cellid])
            
        cdr_data = pd.DataFrame(cdr_data_array, columns = ['user', 'timestamp', 'cellid']).sort_values(by = 'timestamp')

        self.cdr_data = cdr_data
        print(f"CDR data generated for User {self.id}, between dates {date_beginning} and {date_end}, with {len(cdr_data)} rows.")



            