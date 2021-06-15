import importlib
from . import users

class Population:

    def __init__(self, profile_dict):
        self.profile_dict = profile_dict

        # TODO: Might not be necessary?
        for key, value in profile_dict.items():
            self.key = value

    
    def generatePopulation(self):

        id_counter = 1
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
                user.generateMeaningfulLocations()
        except:
            print("ERROR! Population hasn't been generated! Use population.generatePopulation()!")