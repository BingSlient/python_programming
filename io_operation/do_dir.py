"""Learn how to use os package to operate directories and files in python
"""

from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print(f'{fsize:10d} {mtime} {f}{flag}')
    # print('{:10d} {} {}{}' % (fsize, mtime, f, flag))
    print(f'{datetime(2019, 7, 18, 23, 38): %Y-%m-%d %H-%M}')

