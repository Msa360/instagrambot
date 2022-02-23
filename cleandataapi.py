# api config for cleandata.py file

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv("APIKEY")

def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def contain_text(file: str) -> bool:
    json_resp = ocr_space_file(filename=file, language='eng', api_key=apikey)
    x = json.loads(json_resp)
    y = x["ParsedResults"]   
    z = y[0]
    if z['ParsedText'] == "":
        return False
    else:
        return True

