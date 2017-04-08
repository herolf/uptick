import click
from pprint import pprint
from bitshares.storage import configStorage as config
from .ui import (
    onlineChain,
    unlockWallet
)
from .main import main


@main.command()
@click.pass_context
@onlineChain
@click.argument(
    'members',
    nargs=-1)
@click.option(
    "--account",
    default=config["default_account"],
    help="Account that takes this action",
    type=str)
@unlockWallet
def approvecommittee(ctx, members, account):
    """ Approve committee member(s)
    """
    pprint(ctx.bitshares.approvecommittee(
        members,
        account=account
    ))


@main.command()
@click.pass_context
@onlineChain
@click.argument(
    'members',
    nargs=-1)
@click.option(
    "--account",
    help="Account that takes this action",
    default=config["default_account"],
    type=str)
@unlockWallet
def disapprovecommittee(ctx, members, account):
    """ Disapprove committee member(s)
    """
    pprint(ctx.bitshares.disapprovecommittee(
        members,
        account=account
    ))
