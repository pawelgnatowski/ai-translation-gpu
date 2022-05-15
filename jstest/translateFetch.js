// import fetch from 'fetch';
import "isomorphic-fetch"
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