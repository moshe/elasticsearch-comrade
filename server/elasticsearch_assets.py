import json
from glob import glob
from os import path

assets_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), 'elasticsearch'))


def get_index_settings_docs():
    files = glob(path.join(assets_dir, 'index_settings', '*'))
    resp = []
    for f in files:
        resp.append(json.load(open(f)))
    return resp
