class DataMaintainance:
    def __init__(self, fileName=""):
        self.fileName = fileName

    def getLastId(self):
        return 0

    def read(self):
        lines = []
        with open(self.fileName, 'r') as file:
            for line in file.readlines():
                lines.append(line.strip())
        return lines
    
    def add(self, note):
        with open(self.fileName, 'a') as file:
            file.write('\n' + f"{note.id};{note.title};{note.message};{note.data};") 

    def delete(self, id):
        lines = self.read()
        for line in lines:
            if line.split(';')[0] == id:
                lines.remove(line)
        
        
        with open(self.fileName, 'w') as file:
                for line in lines:
                    file.write('\n' + line) 



    def update(self, id, note):
        lines = self.read()
        for line in lines:
            if line.split(';')[0] == id:
                lines[lines.index(line)] =  f"{note.id};{note.title};{note.message};{note.data};"
        
        
        with open(self.fileName, 'w') as file:
                for line in lines:
                    file.write('\n' + line) 



    

