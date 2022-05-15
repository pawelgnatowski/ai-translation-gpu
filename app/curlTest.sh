# !/bin/bash
python3 download_models.py --source pl --target en

curl --location --request POST 'http://localhost:5030/translate' --header 'Content-Type: application/json' --data-raw '{
 "text":"Elon leci na Marsa",            
 "from":"pl",
 "to":"en"
}'

curl --location --request POST 'http://localhost:5030/translate' --header 'Content-Type: application/json' --data-raw '{ "text":"Najlepsze Pierogi w miescie",  "from":"pl",
 "to":"en" }'