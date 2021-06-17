from mpdgen.tests import test_users, test_population
import yaml
import time

start_time = time.time()

conf = yaml.safe_load(open("config.yaml", "r"))

conf_time = time.time()
print(f"Config time: {round(conf_time - start_time, 2)} seconds.")

# TODO: At the moment, main.py is basically the same as testPopulation. Should make this different somehow.

# test_users.testAbstractUser(cells_filepath)
test_population.testPopulation(conf)

conf_time = time.time()
print(f"Test Population time: {round(conf_time - start_time, 2)} seconds.")