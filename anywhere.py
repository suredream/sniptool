#!/usr/bin/env python3
import os, sys
from glob import glob
from os.path import expanduser
home = expanduser("~")
search_dirs = open(f'{home}/.anywhere').read().splitlines()
include = [d for d in search_dirs if not d.startswith('!')]
exclude = [d[1:] for d in search_dirs if d.startswith('!')]

# search_dirs = ['/mnt','/mnt/artifacts']
max_depths = 3
dir_list = []
idx = 0
for folder in include:
#     break
    for root, dirs, files in os.walk(folder):
        if '.' in root: continue #.git hidden folder
        if root.startswith('_'): continue
        for d in dirs:
            is_exclude = [root in e for e in exclude]
            if any(is_exclude): continue
            if '.' in d: continue
            if d.startswith('_'): continue

            target = os.path.join(root, d)
            if target[len(folder):].count('/') > max_depths: continue # too deep
            if len(sys.argv) > 1:
                if idx == int(sys.argv[1]):
                    print(target)
                    exit()
            else:
                print(f'{idx:3}:\t{target}', d)    
            idx += 1