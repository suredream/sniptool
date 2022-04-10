__version__ = "0.0.1"

from .core import MiscMagics
from .viz import AssetMagics
from .snip import SnippetsMagics
from .ver import VControlMagics

def load_ipython_extension(ipython):
    ipython.register_magics(SnippetsMagics)
    ipython.register_magics(AssetMagics)
    ipython.register_magics(VControlMagics)
    