from note import Note
from consoleReader import ConsoleReader
from dataMaintainance import DataMaintainance

class Observer:
    def __init__(self):
        self.consoleReader = ConsoleReader()
        self.db = DataMaintainance("db.csv")

    def getDataFromUser(self):
        print('Введите заголовок: ')
        title = self.consoleReader.getData()
        print('Введите сообщение: ')
        message = self.consoleReader.getData()
        print('Введите дату: ')
        date = self.consoleReader.getData()

        return Note(1, title, message, date)
        
        
    def addData(self):
        self.db.add(self.getDataFromUser())

    def deleteData(self, id):
        print(self.db.delete(id))

    def chooseAction(self):
        action = self.consoleReader.getData()
        if action == 'add':
            self.addData()
        elif action == "read":
            self.readData()
        elif action == 'del':
            id = input('Введите id для удаления записи:')
            self.deleteData(id)
        elif action == 'update':
            id = input('Введите id для удаления записи:')
            self.editData(id)
    
    def readData(self):
        lines = self.db.read()
        for line in lines:
            print(line)

    def editData(self, id):
        self.db.update(id, self.getDataFromUser())

