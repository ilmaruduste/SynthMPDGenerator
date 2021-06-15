from .. import users

print("\n-- Running User tests... --\n")

def testAbstractUser():
    print("Running abstract user test...")

    john = users.User(54)
    john.generateMeaningfulLocations()
    print(f"User's ID: {john.id}")