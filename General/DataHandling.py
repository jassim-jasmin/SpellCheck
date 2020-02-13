import pandas as pd
import sys

class DataHandling:
    def __init__(self):
        """ from name list files data is in this default form """
        self.inputNameSetHeader = ['county', 'gender', 'year_of_birth', 'name', 'frequency']

    def csvToDF(self, directoryPath, sep, head):
        try:
            data = pd.read_csv(directoryPath, sep=sep, header=None, names=head)
            return data
        except Exception as e:
            return pd.DataFrame()

    def mergeDataFrame(self, df, directoryPath, csvSeperator, head, distFields=None):
        try:
            if not df.empty:
                if distFields:
                    dfConcat = pd.concat([df, self.csvToDF(directoryPath, csvSeperator, head)])
                    dfConcat.drop_duplicates(subset=distFields, keep="first", inplace=True)
                    return dfConcat
                else:
                    return pd.concat([df, self.csvToDF(directoryPath, csvSeperator, head)])

            else:
                return False
        except Exception as e:
            print('error in mergeDataFrame in DataHandling')
            return False

    def osDirPathConnector(self):
        try:
            if sys.platform == 'linux':
                seperator = '/'
            else:
                seperator = '\\'

            return seperator
        except Exception as e:
            print('error in osDirPathConnector', e)
            return False

    def makeUniqNameSet(self, directoryHandlingObj, dirPath):
        """
        Concat all records in every text files in the @dirpath and remove duplicate name only
        :param directoryHandlingObj: FileDataProcessing.DirectoryHandling object
        :param dirPath: path of folder conatin text file
        :return: dataframe with unique names
        """
        try:
            fileList = directoryHandlingObj.getDirectoryElements(dirPath)
            mainNmaeDf = pd.DataFrame(columns=self.inputNameSetHeader)
            for index in range(0,len(fileList)):
                if index == 0:
                    mainNmaeDf = self.csvToDF(dirPath + self.osDirPathConnector() + fileList[index], ',', self.inputNameSetHeader)
                else:
                    mainNmaeDf = self.mergeDataFrame(mainNmaeDf, dirPath + self.osDirPathConnector() + fileList[index], ',', self.inputNameSetHeader, 'name')

            return mainNmaeDf
        except Exception as e:
            print('error in makeUniqNameSet in DataHandling', e)
            return False

    def makeNameGroupDict(self, directoryHandlingObj, dirPath):
        try:
            nameDataFrame = self.makeUniqNameSet(directoryHandlingObj, dirPath)

