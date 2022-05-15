This is your personal Google translate service ;)


for faster inference it was designed to use Nvidia Cuda iference
for even faster inference consider exporting the model to ONNX.

Requirements:
nvidia CUDA capable GPU that can be passed through to docker container (or set huggingface translator use_gpu to False)

Tested on:
Windows 11 WSL2 + WSLg on Ubuntu 20.04

Note:
If you have a single GPU you can only use single container with GPU passthrough. (though inside container you can handle multiple instances of programs accessing GPU - tried and tested)

Build the image:
docker build -t ai-translation-gpu-app .

Run the image:
docker run -idt --rm --gpus all -v pathToVolumeWithLanguages/app/data:/app/data -p 5030:5000 --name ai-translate-app ai-translation-gpu-app

visit:
http://localhost:5030/get_routes

if you see nothing then you need to download language models
you can download them manually or use downloader from within container or host

app/allModels.json contains list of available language pairs
you can recreate the file by visiting https://huggingface.co/Helsinki-NLP

script for scraper:
app/getAllModels.js

Language model downloader usage:

download all supported models for Polish
python3 download_models.py --source all --target pl

download all supported models from Polish to any other language
python3 download_models.py --source pl --target all

download all models:
python3 download_models.py --source all --target all

of course you can write a function them download automatically.

Test your service edit curlTest.sh and run it.

EXAMPLE USAGE:

JavaScript:
    let translateText =
    {
        "text": "Make code not war",
        "from": "en",
        "to": "ru",
    };

    let translated = await fetch('http://localhost:5030/translate', {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(translateText)
    }) //.then (response=>response.json())
    console.log (await translated.json());

cURL:
    curl --location --request POST 'http://localhost:5030/translate' --header 'Content-Type: application/json' --data-raw '{
    "text":"Elon leci na Marsa",            
    "from":"pl",
    "to":"en"
    }'

from within python code:
    
    translate('I like candy','en','de')



if you like it please share and subscribe
drop a star to this repo too!

Cheers!
Pablo autoEscobar Gnatowski
pawel.gnatowski@gmail.com
Article:
https://www.pablo-labs.com/post/dyi-build-your-own-google-translate-service-give-this-solution-a-hug

