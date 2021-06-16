from .. import users
from .. import cell_network


def testAbstractUser(cell_filepath):
    print("Running abstract user test...")

    testCellNetwork = cell_network.CellNetwork(cell_filepath)

    john = users.User(54, cell_network = testCellNetwork)

    john.generateMeaningfulLocations(john.cell_network)
    
    print(f"User's ID: {john.id}")