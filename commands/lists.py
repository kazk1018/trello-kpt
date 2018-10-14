import click


@click.group('lists')
@click.pass_context
def lists(ctx):
    pass


@lists.command('add')
@click.argument('board_id')
@click.argument('lists')
@click.pass_context
def list_add(ctx, board_id, ls):
    client = ctx.obj['client']
    b = client.get_board(board_id)
    for l in ls.split(',')[::-1]:
        rtn = b.add_list(l)
        click.echo('{}: {}'.format(rtn.name, rtn.id))


@lists.command('get')
@click.argument('board_id')
@click.pass_context
def board_get(ctx, board_id):
    client = ctx.obj['client']
    b = client.get_board(board_id)
    ls = b.all_lists()
    for l in ls:
        click.echo('{}: {}'.format(l.name, l.id))
