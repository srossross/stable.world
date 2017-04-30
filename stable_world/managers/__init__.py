import click

from .pypi import PyPIManager
from .npm import NPMManager


def use(ty, project, cache_list, token, dryrun):

    if ty == PyPIManager.NAME:
        Manager = PyPIManager
    elif ty == NPMManager.NAME:
        Manager = NPMManager
    else:
        click.echo("Don't know what to do for type %s" % ty)
        return None

    manager = Manager(project, cache_list, token, dryrun)
    return manager.use()


def unuse(ty, info):
    if ty == PyPIManager.NAME:
        Manager = PyPIManager
    elif ty == NPMManager.NAME:
        Manager = NPMManager
    else:
        click.echo("Don't know what to do for type %s" % ty)
        return None

    Manager.unuse(info)
