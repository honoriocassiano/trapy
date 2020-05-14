import yaml


def read_swagger(content : str):
    parsed = yaml.load(content, Loader=yaml.FullLoader)

    return parsed


def read_file(filename: str):
    file = open(filename, mode='r')

    content = file.read()

    file.close()

    return content


content = read_file("./example.yaml")
spec = read_swagger(content)

print(spec['paths'])
