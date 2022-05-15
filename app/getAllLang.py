# Python program to read
# json file


import json

# Opening JSON file
from itertools import starmap



# Iterating through the json
# list

def myPrint(*args):
    source = args[0]
    target = args[1]
    print(source + target)


# data = [["es", "en"],
#         ["pl", "en"],
#         ["pl", "de"]
#         ]
# y=1
# langs = list(filter(lambda langPair:langPair[y] == 'en', data))

def filterLangs (langList=[], lang='en', boolTarget=False):
    if boolTarget:
        boolTarget=1
    else:
        boolTarget=0

    langs = list(filter(lambda langPair: langPair[boolTarget] == lang, langList))

    return langs

def getLangagueList (path=''):
    f = open(path+'allModels.json', )

    # returns JSON object as
    # a dictionary
    data = json.load(f)['models']
    f.close()
    return data



# create a list from a csv file, using first column as element list.
# the other column is not needed
def createListFromCSV(path=''):
    f = open(path+'allModels.csv', 'r')
    data = f.readlines()
    f.close()
    data = [line.split(',') for line in data]
    data = [line[0] for line in data]
    return data

# list A = [["es", "en"], ["de", "en"], ["pl", "de"]]
# list B = ["es","de"]
# Result: [["es", "en"], ["de", "em"]]

def filterListAbyListB(listA=[], listB=[]):
    listA = list(filter(lambda langPair: langPair[0] in listB, listA))
    return listA


