__version__ = "0.0.1"

"""
%snip magic for snippets management, supported by a sqlite db, powered by nbdev

# Author: Jun Xiong. 04/08/2022, 12:46
# Distributed under the terms of the Modified BSD License.


%d        -- for object inspection
%tidy     -- tidy-up notebook
%g        -- git commands
%saveimg  -- save cell outputs to disk
%lint     -- save cell outputs to disk

%%toc     -- create toc divider
%%runingb -- running in the background

snippets naming: # @desc #t1 #t2

todo
- [x] yaml cfg
- [x] absolute path for db
- [x] reset
- [x] shortcut
- [x] setup
- [x] snip (db free; local json db)
- [x] Todo Tree: 
- [x] absolute path, snip.json
- [ ] unit test: nbdev_test_nbs
- [ ] config yaml
- [ ] savefig, uuid
- [ ] url to source file
- [ ] pre-commit, not ipynb, only select ipynb py and images, update images with uuid
https://gist.github.com/tylerneylon/697065ca5906c185ec6dd3093b237164


toanswer
- export to one script?
- 
- 


workflow
- 

"""

# from .core import MiscMagics
from .viz import AssetMagics
from .snip import SnippetsMagics
from .ver import VControlMagics
from .misc import MiscMagics

def load_ipython_extension(ipython):
    ipython.register_magics(MiscMagics)
    ipython.register_magics(SnippetsMagics)
    ipython.register_magics(AssetMagics)
    ipython.register_magics(VControlMagics)
    