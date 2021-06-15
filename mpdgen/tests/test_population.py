from .. import population

print("\n-- Running Population tests... --\n")

def testPopulation():
    
    randomProfileDict = dict({"User":5, "GeneralUser": 10})

    randomPopulation = population.Population(randomProfileDict)

    # It is also possible to have the syntax as simply print(f"{randomPopulation.profile_dict=}"), but this feature is Python 3.8+ only and I'm on 3.7.4
    print(f"randomPopulation.profile_dict = {randomPopulation.profile_dict}")

    randomPopulation.generatePopulation()
    randomPopulation.generateMeaningfulLocations()
