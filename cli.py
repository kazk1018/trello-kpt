import click

from api import Config, new_client
from commands import board, config, organization


@click.group()
@click.pass_context
def cli(ctx):
    # context type definition
    ctx.ensure_object(dict)

    # add client to context
    client = new_client(Config.read_from_yaml())
    ctx.obj['client'] = client


# commands
cli.add_command(board)
cli.add_command(config)
cli.add_command(organization)


def main():
    cli()


if __name__ == '__main__':
    main()
