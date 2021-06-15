from .. import population

print("\n-- Running Population tests... --\n")

def testPopulation():
    
    randomProfileDict = dict({"User":5, "GeneralUser": 10})

    randomPopulation = population.Population(randomProfileDict)

    print(randomPopulation.profile_dict)

    randomPopulation.generatePopulation()
    randomPopulation.generateMeaningfulLocations()
