from trello import TrelloClient


def new_client(c):
    client = TrelloClient(api_key=c.api_key,
                          api_secret=c.api_secret,
                          token=c.token,
                          token_secret=c.token_secret)
    return client

