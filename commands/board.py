import click


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
    new_board = client.add_board(board_name, organization_id=org_id, permission_level=permission_level)
    click.echo('board {} was created. url={}'.format(new_board.name, new_board.url))


@board.command('list')
@click.pass_context
def board_list(ctx):
    client = ctx.obj['client']
    for b in client.list_boards():
        print(b.name)
