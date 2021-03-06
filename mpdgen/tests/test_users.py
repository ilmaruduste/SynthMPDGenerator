from .. import users
from .. import cell_network


def testAbstractUser(conf):

    cells_filepath = conf['REFERENCE']['CELLS']

    print("Running abstract user test...")

    testCellNetwork = cell_network.CellNetwork(cells_filepath)

    john = users.User(54, cell_network = testCellNetwork)

    john.generateMeaningfulLocations(john.cell_network)
    john.generateCDR(['2018-01-01', '2018-01-08'])
    print(f"User's CDR data first 5 rows:\n{john.cdr_data.head()}")

    print(f"User's ID: {john.id}")