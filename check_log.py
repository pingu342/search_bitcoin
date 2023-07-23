import re
#import ast
import sys
import glob

keys = 0
satoshi = 0

files = []
args = sys.argv[1:]
for arg in args:
    array = glob.glob(arg)
    files.extend(array)

for file in (files):
    print(file)
    with open(file) as f:
        i = 0
        for line in f:
            if re.search('Balance : ', line):
                line = line.strip()
                array = line.split('Balance : ')
                try:
                    #json = ast.literal_eval(array[1])
                    #n = json['result']['confirmed']
                    #n += json['result']['unconfirmed']
                    if len(array) < 2:
                        raise Exception('parse error')
                    n = int(array[1])
                    if n > 0:
                        print('[%d] %s' % (i, line))
                    satoshi += n
                    keys += 1
                except Exception as e:
                    print('[%d] %s' % (i, line))
            i += 1

print('Total %d satoshi found in %d keys.' % (satoshi, keys))

