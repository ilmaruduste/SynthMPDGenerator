from mpdgen.tests import test_users, test_population
import yaml

conf = yaml.safe_load(open("config.yaml", "r"))


# test_users.testAbstractUser(cells_filepath)
test_population.testPopulation(conf)