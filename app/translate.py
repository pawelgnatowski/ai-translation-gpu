from transformers import MarianTokenizer, MarianMTModel
import os
from typing import List


class HuggingFaceTranslator():
    def __init__(self, models_dir:str,use_gpu: bool = True):
        self.models = {}
        self.models_dir = models_dir
        self.use_gpu = use_gpu

    def get_downloaded_language_models(self):
        routes = [x.split('-')[-2:] for x in os.listdir(self.models_dir)]
        return routes

    def load_model(self, route):
        model = f'opus-mt-{route}'
        path = os.path.join(self.models_dir, model)
        try:
            # model load to GPU if available - otherwise CPU is used - just remove the 'cuda' part
            # https://github.com/huggingface/transformers/issues/5602 => that was the hint!
            # TODO what to do when no GPU is available?
            # TODO unload model if out of memory?
            # .to('cuda')
            model = MarianMTModel.from_pretrained(path)
            if (self.use_gpu==True):
                model.to('cuda')
            tok = MarianTokenizer.from_pretrained(path)
        except:
            print(f'Model {route} not found')
            return 0, f"Make sure you have downloaded model for {route} translation"
        self.models[route] = (model, tok)
        print(f'Model {model} loaded')
        return 1, f"Successfully loaded model for {route} transation"

    def translate(self, text_language, target_language, text):
        route = f'{text_language}-{target_language}'
        if not self.models.get(route):
            success_code, message = self.load_model(route)
            if not success_code:
                return message
# tokenizer does not have to be loaded to cuda - batch though does. .to('cuda')
# prepare_seq2seq_batch is deprecated!!! need to look into code to see if it is still used
        batch = self.models[route][1].prepare_seq2seq_batch(
            src_texts=list([text]), return_tensors="pt")
        if (self.use_gpu == True):
            batch.to('cuda')
        gen = self.models[route][0].generate(**batch)
        translated: List[str] = self.models[route][1].batch_decode(
            gen, skip_special_tokens=True)
        return translated
