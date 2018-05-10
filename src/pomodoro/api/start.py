""" Implement the cmd1 command.

"""
from ..core import logger
from .. import main as m


def main():
    """ Execute the command.

    """
    logger.debug("executing cmd1 command")
    m()
    return
