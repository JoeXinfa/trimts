# -*- coding: utf-8 -*-

"""
Remove trailing white spaces in code.
Usage: python this-script work-path
"""

import os
import sys

#PATH = '/path/to/your/project'
PATH = sys.argv[1]
print('Working in', PATH)

for path, dirs, files in os.walk(PATH):
    for f in files:
        file_name, file_extension = os.path.splitext(f)
        if file_extension == '.py':
            path_name = os.path.join(path, f)
            print('Working on', path_name)
            with open(path_name, 'r', encoding='utf-8') as fh:
                new = [line.rstrip() for line in fh]
            with open(path_name, 'w', encoding='utf-8') as fh:
                #[fh.write('%s\n' % line) for line in new]
                fh.writelines((line+'\n' for line in new))
