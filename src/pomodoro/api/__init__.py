""" Application commands common to all interfaces.

"""
from .cmd1 import main as cmd1
from .start import main as start
from .cmd2 import main as cmd2


__all__ = "cmd1", "cmd2", "start"
