from trello import TrelloClient
from api.config import Config


def new_client(c: Config):
    client = TrelloClient(api_key=c.api_key,
                          api_secret=c.api_secret,
                          token=c.token,
                          token_secret=c.token_secret)
    return client

