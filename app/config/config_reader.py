import yaml

with open('config/config.yaml', 'r') as f:
    global config
    config = yaml.safe_load(f)