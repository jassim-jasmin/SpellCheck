# from fuzzysearch import find_near_matches
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class Fuzzy:
    def getMatchFromSet(self,string, stringSet, confidence, notConfidencce = None) -> str:
        """It is a fuzzywuzzy process extractOne output only returns with confidence"""
        try:
            if stringSet:
                match = process.extractOne(string, stringSet)

        if (match[1] == notConfidencce) or (match[1] < confidence):
            return False
        elif match[1] > confidence:
            return match

                #else:
                 #   return False
            #else:
             #   return
        except Exception as e:
            print('error in getMatchFromSet in StringHandling')
