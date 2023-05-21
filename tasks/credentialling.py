import yaml


def get_credentials():
    with open('../credentials.yaml') as file:
        credentials = yaml.safe_load(file)
    return credentials
