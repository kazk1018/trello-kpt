import click
import json


def list_repr(lists):
    bs = []
    if type(lists) == list:
        for b in lists:
            bs.append({'id': b.id, 'name': b.name})
    else:
        bs.append({'id': lists.id, 'name': lists.name})

    return json.dumps({"lists": bs})


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
    ls = []
    for l in ls.split(',')[::-1]:
        rtn = b.add_list(l)
        ls.append(rtn)
    click.echo(list_repr(ls))


@lists.command('get')
@click.argument('board_id')
@click.pass_context
def board_get(ctx, board_id):
    client = ctx.obj['client']
    b = client.get_board(board_id)
    ls = []
    for l in b.all_lists():
        ls.append(l)
    click.echo(list_repr(ls))
