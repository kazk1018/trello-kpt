import click
import json
import os


def board_repr(boards):
    bs = []
    if type(boards) == list:
        for b in boards:
            bs.append({'id': b.id, 'name': b.name, 'url': b.url})
    else:
        bs.append({'id': boards.id, 'name': boards.name, 'url': boards.url})

    return json.dumps({"boards": bs})


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
    bs = []
    for b in client.list_boards():
        bs.append(b)

    click.echo(board_repr(bs))


@board.command('search')
@click.argument('name')
@click.pass_context
def board_search(ctx, name):
    client = ctx.obj['client']
    bs = []
    for b in client.list_boards():
        if name in b.name:
            bs.append(b)

    click.echo(board_repr(bs))


@board.command('report')
@click.argument('board_id')
@click.argument('output')
@click.pass_context
def board_report(ctx, board_id, output):
    _, ext = os.path.splitext(output)
    if ext != '.md':
        click.echo('output must be markdown (.md) file.')

    else:
        client = ctx.obj['client']
        b = client.get_board(board_id)

        f = open(output, 'w')

        # Title
        f.write('# {}\n'.format(b.name))

        for l in b.get_lists('open'):
            # Lists
            f.write('## {}\n'.format(l.name))

            # Cards
            for card in l.list_cards():
                f.write('### {}\n'.format(card.name))

                # Comments
                for comment in card.get_comments():
                    f.write('- {}\n'.format(comment['data']['text']))

                f.write('\n')

            f.write('\n')

        f.close()


