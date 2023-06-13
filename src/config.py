import yaml

def get():
    with open('../config.yml', 'r') as file:
        dados = yaml.safe_load(file)
    return dados