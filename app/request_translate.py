import requests

import urllib.parse
import urllib.request
import urllib.error


# make a request to transaltion web service with the given parameters
# and return the response
# example parameters:
# method = 'POST'
# url ='http://30.20.30.10:5000/translate'
# --header 'Content-Type: application/json'
# --data '{"text":"Hello world!"
#  "text":"Prezes Jarosław Kaczyński w świetnej formie mówi z troską o Polskę i wytycza zadania do pracy  dla Polski",
#  "source":"pl",
#  "target":"en"
# }'

def translateText(text, url, source, target):
    try:
        data = {'text': text, 'source': source, 'target': target}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        return response.json()["output"][0]
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
        return None
    except urllib.error.URLError as e:
        print(e.reason)
        return None
    except Exception as e:
        print(e)
        return None

# print (translateText ('jebac swiat!', 'http://30.20.30.10:5000/translate', 'pl', 'en'));

translatedJson = translateText ('jebac swiat!', 'http://30.20.30.10:5000/translate', 'pl', 'en');
print (translatedJson);