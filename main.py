import os

from General.DataHandling import DataHandling
from General.FileDataProcessing import DirectoryHandling

class Main:
    def __init__(self):
        self.dataHandling = DataHandling()
        self.directoryHandling = DirectoryHandling()

    def __del__(self):
        del self.dataHandling
        del self.directoryHandling

