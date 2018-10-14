import click


def board_repr(b):
    return '{}: {} ({})'.format(b.id, b.name, b.url)


@click.group('board')
@click.pass_context
def board(ctx):
    pass


@board.command('new')
@click.argument('board_name')
@click.option('-o', '--organization-id', 'org_id')
@click.pass_context
def board_new(ctx, board_name, org_id):
    client = ctx.obj['client']
    permission_level = 'private'
    if org_id is not None:
        permission_level = 'org'
    new_board = client.add_board(board_name,
                                 organization_id=org_id,
                                 permission_level=permission_level,
                                 default_lists=False)

    click.echo(new_board.id)


@board.command('get')
@click.argument('board_id')
@click.pass_context
def board_get(ctx, board_id):
    client = ctx.obj['client']
    b = client.get_board(board_id)
    click.echo(board_repr(b))


@board.command('list')
@click.pass_context
def board_list(ctx):
    client = ctx.obj['client']
    for b in client.list_boards():
        click.echo(board_repr(b))
