import os
import argparse
import urllib
from urllib.request import urlretrieve
from config import *
import json
parser = argparse.ArgumentParser()
parser.add_argument("--source", type=str, help="source language code")
parser.add_argument(
    "--target", type=str, help="target language code"
)

# https://huggingface.co/Helsinki-NLP
def download_language_model(source, target):
    model = f"opus-mt-{source}-{target}"
    print(">>>Downloading data for %s to %s model..." % (source, target))
    directory = os.path.join("data", model)
    if not os.path.exists(directory):
        os.makedirs(directory)
    # os.makedirs(os.path.join("data", model))
    # download only non existing ones
    # TODO add a logic path to update models / need to add scraper functionality to check against some db.
        for file in FILENAMES:
            try:
                print(os.path.join(HUGGINGFACE_S3_BASE_URL, model, file))
                urlretrieve(
                    "/".join([HUGGINGFACE_S3_BASE_URL, model, file]),
                    os.path.join(MODEL_PATH, model, file)
                )
                print("Download complete!")
            except urllib.error.HTTPError:
                print("Model not found - check allModels.json - or get it manually from huggingface, you can scrape it using jstest file directly in browser console")
                os.rmdir(os.path.join("data", model))
                break


def filterLangs(langList=[], lang='en', boolTarget=False) -> list:
    """
    Parameters
    ----------
    langList : str[][]
            Language pairs list in a list [["en", "fr"],["de,"pl"]]
    lang : str
            Langauge you want to be returned

    boolTarget : bool
            False => filter for first item in pair, therefore you filter for source language
            True => filter for second item in pair, therefore you filter for target language

    Returns
    -------
    list
        List of Lists (language pairs) filtered by eihter 1st or second position

        ... first position is source language
        
        ... second position is target language
    
    Examples
    --------
    >>> filterLangs([["en", "fr"],["en", "de"],["de,"pl"]],"en",False)
    [["en", "fr"],["en", "de"]]

    ... Filtering for second position language

    >>> filterLangs([["en", "fr"],["de,"pl"]],"en",True)
    [[]]


    Raises
    ------
    LinAlgException
        No error handling here
    """
    if boolTarget:
        boolTarget = 1
    else:
        boolTarget = 0

    langs = list(filter(lambda langPair: langPair[boolTarget] == lang, langList))

    return langs


def getLangagueList(path=''):
    """gets language pairs from json file

    Args:
        path (str, optional): path to allModels.json. Defaults to ''.

    Returns:
        array: language pairs in a list [["en", "fr"],["de,"pl"]] => these are all the language pairs supported by the models at HuggingFace, you can filter those futhter down to limit amount of models you download and use.
    """    
    # TODO: create a bot to get all langs automagically
    f = open(path + 'allModels.json', )


    data = json.load(f)['models']
    f.close()
    return data
    
    

# create a list from a csv file, using first column as element list.
# the other column is not needed
def createListFromCSV(path=''):
    f = open(path+'used_langs.csv', 'r')
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


if __name__ == "__main__":
    args = parser.parse_args()
    # you can specify all in either source or target
      
    if args.source != 'all' and args.target != 'all':
        # download only one language pair
        download_language_model(args.source, args.target)
        exit(0)
    languageList = getLangagueList()
    if args.source != 'all':
        languageList = filterLangs(languageList, args.source)
    if args.target != 'all':
        languageList = filterLangs(languageList, args.target, True)
    print(languageList)
    for langPair in languageList:
        download_language_model(*langPair)