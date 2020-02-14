import os

from General.DataHandling import DataHandling
from General.FileDataProcessing import DirectoryHandling

class Main:
    def __init__(self):
        self.dataHandling = DataHandling()
        self.directoryHandling = DirectoryHandling()


    def setupNameList(self):
        dirPath = ""
        directoryHandlingObj = DirectoryHandling()
        df = self.dataHandling.makeUniqNameSet(directoryHandlingObj, '/root/Documents/mj/dataSet/name_county')
        self.dataHandling.saveDataFrameToJson(df, '/root/Documents/mj/nameSearch/name_set.csv')

    def searchName(self, name):
        getNameDF = self.dataHandling.readCsvToDF('/root/Documents/mj/nameSearch/name_set.csv')
        getNameList = getNameDF[self.dataHandling.inputNameSetHeader[3]] # hader name tag for NAME
        print(getNameList)

    def __del__(self):
        del self.dataHandling
        del self.directoryHandling

if __name__ == "__main__":
    mainObj = Main()
    # mainObj.setupNameList()
    mainObj.searchName('test')
