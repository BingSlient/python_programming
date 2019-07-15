"""Learn how to operate file in python
"""

from io import StringIO  # used to operate string stream on fly
from io import BytesIO   # used to operate byte stream on fly

import os # use os command, operations on dir. and file name`

################################
# Reads a file and stores it in StringIO
################################


if __name__ == '__main__':
    print('creating StringIO sio...')
    sio = StringIO()

    fp = r'../README.md'
    # get file name using os.path.split
    fname = os.path.split(fp)[1]
    print('reading file:{}, in {}'.format(fname, os.path.abspath('..')))

    with open(fp, 'r') as f:
        s = f.read()
        sio.write(s)
    
    print('Writing content of file {} to StringIO'.format(fname))
    print('Print out StringIO using StringIO.getvalue() method...')
    print(40*'_')
    print(sio.getvalue())
    print(40*'_')
    
    # after writing, the file pointer is not at the start of a StringIO
    print('StringIO file pointer current position: {}'.format(sio.tell()))
    # move file pointer to beginning of StringIO
    sio.seek(0)
    print('move file pointer to beginning of StringIO')
    print('Current stream position of StringIO:{}\n'.format(sio.tell()))
    print('Print out StringIO using StringIO.readlines() method...')
    print(40*'_')

    for line in sio.readlines():
        print(line.strip())
    print(40*'_')
    
    

    
