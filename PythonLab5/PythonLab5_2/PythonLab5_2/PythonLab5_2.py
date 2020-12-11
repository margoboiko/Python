import sqlite3

FILENAME = 'monitors.db'


def getConnection():
    return sqlite3.connect(FILENAME)


def migrateTable():
    with getConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS monitors")
        cursor.execute("""CREATE TABLE monitors
                          (brand text, model int, year int, cost int, data date, surname text, name text)
                       """)

def readData():
    with getConnection() as conn:
        cursor = conn.cursor()
        brand = input('brand: ')
        cursor.execute("""SELECT brand, model, MAX(year), cost, data, surname, name FROM monitors WHERE brand LIKE ?""", (brand, ))
        print("The newest monitor: """, cursor.fetchone())

        cursor.execute("""SELECT SUM(cost) as sum FROM monitors""")
        print("Count monitors:: ", cursor.fetchone()[0])


def inputData():
    with getConnection() as conn:
        cursor = conn.cursor()

        brand = input('brand: ')
        model = int(input('model: '))
        year = int(input('year: '))
        cost = int(input('cost: '))
        data = input('data: ')
        surname = input('surname: ')
        name = input('name: ')

        cursor.execute('INSERT INTO monitors VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (brand, model, year, cost, data, surname, name))


def processCommand(cmd):
    if cmd == 'migrate':
        migrateTable()
    elif cmd == 'read':
        readData()
    elif cmd == 'write':
        inputData()
    else:
        print('Unknown command')

    return True


print('> Available commands: migrate, read, write')

continueLoop = True
while continueLoop:
    command = input('> Enter command: ')
    continueLoop = processCommand(command)