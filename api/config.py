import os
import yaml


DEFAULT_CONFIG_PATH = os.path.join(os.getenv('HOME'), '.trello.yaml')


class Config:

    def __init__(self, api_key=None, api_secret=None, token=None, token_secret=None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.token = token
        self.token_secret = token_secret

    @staticmethod
    def read_from_yaml(file_path=DEFAULT_CONFIG_PATH):
        with open(file_path, 'r') as f:
            data = yaml.load(f)

        api_key = data.get('api_key')
        api_secret = data.get('api_secret')
        token = data.get('token')
        token_secret = data.get('token_secret')

        return Config(api_key, api_secret, token, token_secret)

    def write_to_yaml(self, file_path=DEFAULT_CONFIG_PATH):
        data = {'api_key': self.api_key,
                'api_secret': self.api_secret,
                'token': self.token,
                'token_secret': self.token_secret}

        with open(file_path, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
