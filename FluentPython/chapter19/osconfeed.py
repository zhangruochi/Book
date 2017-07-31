#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


import json
import requests
import os



URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'

def load():
    if not os.path.exists(JSON):
        if not os.path.exists("data"):
            os.mkdir("data")

        with open(JSON,"wb") as fp:
            fp.write(requests.get(URL).content)    
        
    with open(JSON,encoding = "utf-8") as fp:
        return json.load(fp)


if __name__ == '__main__':
    json_obj = load()     
    print(json_obj)



