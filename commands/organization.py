import click
import json


def organization_repr(organizations):
    bs = []
    if type(organizations) == list:
        for b in organizations:
            bs.append({'id': b.id, 'name': b.name})
    else:
        bs.append({'id': organizations.id, 'name': organizations.name})

    return json.dumps({"organizations": bs})


@click.group('organization')
@click.pass_context
def organization(ctx):
    pass


@organization.command('list')
@click.pass_context
def organization_list(ctx):
    client = ctx.obj['client']
    os = []
    for o in client.list_organizations():
        os.append(o)
    click.echo(organization_repr(os))
