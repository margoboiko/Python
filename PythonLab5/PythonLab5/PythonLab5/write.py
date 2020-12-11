import ZODB, ZODB.FileStorage, transaction
from monitor import Monitor

storage = ZODB.FileStorage.FileStorage('monitors')
db = ZODB.DB (storage)
connection = db.open()
root = connection.root()

brand = input('brand: ')
model = input('model: ')
year  = input('year: ')
cost = input('cost: ')
data = input('data: ')
surname = input('surname: ')
name = input('name: ')

monitors = root['monitors']
monitors.append(Monitor(brand, model, year, cost, data, surname, name))
root['monitors'] = monitors

transaction.commit()
storage.close()