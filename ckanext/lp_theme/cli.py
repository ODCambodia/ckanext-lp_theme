import click


@click.group(short_help="lp_theme CLI.")
def lp_theme():
    """lp_theme CLI.
    """
    pass


@lp_theme.command()
@click.argument("name", default="lp_theme")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [lp_theme]
