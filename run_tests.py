from mpdgen.tests import test_users, test_population
import yaml

conf = yaml.safe_load(open("config.yaml", "r"))
cells_filepath = conf['REFERENCE']['CELLS']
time_period = conf['CDR GENERATION']['TIME PERIOD']

# test_users.testAbstractUser(cells_filepath)
test_population.testPopulation(cells_filepath, time_period)