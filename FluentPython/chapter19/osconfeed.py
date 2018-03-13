#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com


import json
import requests
import os
from collections import abc

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        if not os.path.exists("data"):
            os.mkdir("data")

        with open(JSON, "wb") as fp:
            fp.write(requests.get(URL).content)

    with open(JSON, encoding="utf-8") as fp:
        return json.load(fp)


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        # 如果是列表，则对列表里每个元素构建对象
        elif isinstance(obj, abc.MutableMapping):
            return [cls.build(item) for item in obj]
        # 既不是列表也不是映射    
        else:
            return obj


if __name__ == '__main__':
    json_obj = load()
    # print(json_obj)
    print(sorted(json_obj["Schedule"].keys()))
