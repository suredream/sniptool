__version__ = "0.0.1"

from .core import SnippetsMagics, MiscMagics

def load_ipython_extension(ipython):
    ipython.register_magics(SnippetsMagics)
    ipython.register_magics(MiscMagics)