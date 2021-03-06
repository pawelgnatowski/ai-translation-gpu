
// credit to:
// https://stackoverflow.com/questions/11849562/how-to-save-the-output-of-a-console-logobject-to-a-file

(function(console){

    console.save = function(data, filename){
    
        if(!data) {
            console.error('Console.save: No data')
            return;
        }
    
        if(!filename) filename = 'console.json'
    
        if(typeof data === "object"){
            data = JSON.stringify(data, undefined, 4)
        }
    
        var blob = new Blob([data], {type: 'text/json'}),
            e    = document.createEvent('MouseEvents'),
            a    = document.createElement('a')
    
        a.download = filename
        a.href = window.URL.createObjectURL(blob)
        a.dataset.downloadurl =  ['text/json', a.download, a.href].join(':')
        e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
        a.dispatchEvent(e)
     }
})(console)

// https://huggingface.co/Helsinki-NLP
// simple scraper to get all language models:
let allLangPairsElements=document.querySelectorAll(`article [title^="Helsinki-NLP/opus-mt"]`)
let langMap = [];
allLangPairsElements.forEach(it => {langMap.push(it.getAttribute('title')) })
let langPairs = langMap.map(title => title.replace('Helsinki-NLP/opus-mt-', '').split('-'));

console.save(langMap);