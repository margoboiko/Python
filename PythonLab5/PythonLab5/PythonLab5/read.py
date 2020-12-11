import ZODB, ZODB.FileStorage, BTrees.OOBTree, transaction
from monitor import Monitor


storage = ZODB.FileStorage.FileStorage('monitors')
db = ZODB.DB (storage)
connection = db.open()
root = connection.root()

brand = input('brand:')

chosen_brand = list(filter(lambda s: s.brand.lower() == brand.lower(), root['monitors']))

if len(chosen_brand) == 0 :
    print("This brand can't be found. Please, try one more time!")
    exit()

younger = max(chosen_brand, key=lambda s: int(s.year))
count = sum(int(monitor.cost) for monitor in chosen_brand)

print("The newest monitor: ", younger)
print("Count monitors: ", count)