import click
from api import Config


@click.group('config')
@click.pass_context
def config(ctx):
    pass


@config.command('new')
@click.pass_context
def config_new(ctx):
    api_key = click.prompt('API Key', hide_input=True, type=str)
    token = click.prompt('API Token', hide_input=True, type=str)

    cfg = Config(api_key=api_key, token=token)
    cfg.write_to_yaml()
