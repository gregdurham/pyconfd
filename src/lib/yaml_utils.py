import yaml

def yaml_to_dict(file):
    with open(file) as _:
        return yaml.load(_)