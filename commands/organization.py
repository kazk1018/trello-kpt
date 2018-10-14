import click


@click.group('organization')
@click.pass_context
def organization(ctx):
    pass


@organization.command('list')
@click.pass_context
def organization_list(ctx):
    client = ctx.obj['client']
    for b in client.list_organizations():
        click.echo('{}: {}'.format(b.name, b.id))
