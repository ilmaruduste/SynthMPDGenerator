import importlib
from . import users
from datetime import datetime
import os
import pandas as pd

class Population:

    def __init__(self, profile_dict, cell_network = None, time_period = None):
        self.profile_dict = profile_dict
        self.users = None
        self.cell_network = cell_network
        self.time_period = time_period
        self.time_generated = datetime.now().strftime(format = "%Y%m%d%H%M%S")

        # TODO: Might not be necessary?
        for key, value in profile_dict.items():
            self.key = value

    
    def generatePopulation(self, id_counter = 1):

        users_array = []

        for profile, profile_n in self.profile_dict.items():
            
            # TODO: This assumes that the input is always an int, not a 0..1 coefficient as first devised
            for iteration in range(profile_n):
                
                userClass = getattr(importlib.import_module("mpdgen.users"), profile)
                newUser = userClass(id_counter)

                users_array.append(newUser)

                id_counter += 1

        self.users = users_array

    
    def generateMeaningfulLocations(self):

        try:
            for user in self.users:
                user.generateMeaningfulLocations(self.cell_network)
        except:
            print("ERROR! Population hasn't been generated! Doing population.generatePopulation() and trying to move on!")
            self.generatePopulation()
            print("Population generated, moving on!")
            for user in self.users:
                user.generateMeaningfulLocations(self.cell_network)

    def generateCDR(self, time_period):

        print("\nGenerating CDR for entire population...")
        try:
            for user in self.users:
                user.generateCDR(time_period)
        except:
            print("ERROR! Meaningful locations haven't been generated! Doing population.generateMeaningfulLocations() and trying to move on!")
            self.generateMeaningfulLocations
            print("Population and meaningful locations generated, moving on!")
            for user in self.users:
                user.generateCDR(self.cell_network)


    def outputCDR(self, output_cdr_folder):
        output_df = pd.concat([user.cdr_data for user in self.users])

        output_filepath = os.path.join(output_cdr_folder, 'synthCDR_' + str(self.time_generated) + '.csv')
        output_df.to_csv(output_filepath, sep = ';')

    def outputMetadata(self, output_metadata_folder):
        pass

    def outputCells(self, output_cells_folder):

        output_filepath = os.path.join(output_cells_folder, 'cell_locations_' + str(self.time_generated) + '.csv')
        self.cell_network.cells_df.to_csv(output_filepath, sep = ';')
        print(f"Exported cell data to {output_filepath}!")
        