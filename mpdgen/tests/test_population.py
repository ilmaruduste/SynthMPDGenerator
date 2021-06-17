from .. import population
from .. import cell_network


def testPopulation(conf):

    cells_filepath = conf['REFERENCE']['CELLS']

    testCellNetwork = cell_network.CellNetwork(cells_filepath)

    randomProfileDict = dict({"User":5, "GeneralUser": 10})

    randomPopulation = population.Population(randomProfileDict, cell_network = testCellNetwork)

    # It is also possible to have the syntax as simply print(f"{randomPopulation.profile_dict=}"), but this feature is Python 3.8+ only and I'm on 3.7.4
    print(f"randomPopulation.profile_dict = {randomPopulation.profile_dict}")

    randomPopulation.generatePopulation()
    randomPopulation.generateMeaningfulLocations()
    randomPopulation.generateCDR(conf)

    randomPopulation.outputCDR(conf)
    randomPopulation.outputCells(conf)
    randomPopulation.outputMetadata(conf)
