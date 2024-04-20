import json

def get_config():
    with open('config/qaland', 'r') as f:
        return json.load(f)
