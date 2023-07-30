from menu import Menu
from note import Note
from dataMaintainance import DataMaintainance
from observer import Observer

class Presenter:
    def __init__(self):
        self.menu = Menu()
        self.observer = Observer()

    def mainLoop(self):
        while True:
            self.menu.show()
            self.observer.chooseAction()
            print()
            if input('Продолжим?') == 'нет':
                break




