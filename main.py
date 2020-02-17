import os

from General.DataHandling import DataHandling
from General.FileDataProcessing import DirectoryHandling
from General.StringHandling import Fuzzy

class Main:
    def __init__(self):
        self.dataHandling = DataHandling()
        self.directoryHandling = DirectoryHandling()
        self.stringHandling = Fuzzy()
        self.stringMatchConfidence = 90
        self.nameCsvPath = '/root/Documents/mj/nameSearch/name_set.csv'
        self.nameSearchDir = '/root/Documents/mj/dataSet/name_county'

    def setupNameList(self):
        directoryHandlingObj = DirectoryHandling()
        df = self.dataHandling.makeUniqNameSet(directoryHandlingObj, self.nameSearchDir)
        self.dataHandling.saveDataFrameToJson(df, self.nameCsvPath)

    def searchName(self, name):
        try:
            getNameDF = self.dataHandling.readCsvToDF(self.nameCsvPath)
            getNameList = getNameDF[self.dataHandling.inputNameSetHeader[3]] # hader name tag for NAME
            values = self.stringHandling.getMatchFromSet(name, getNameList.tolist(), self.stringMatchConfidence)
            print(values)

            return values
        except Exception as e:
            print('error in serachName in main', e)
            return False

    def checkSpell(self, name):
        splitName = name.split(' ')
        pass

    def __del__(self):
        del self.dataHandling
        del self.directoryHandling

if __name__ == "__main__":
    mainObj = Main()
    # mainObj.setupNameList()
    mainObj.searchName('Theoden')
    mainObj.searchName('Thedn')
