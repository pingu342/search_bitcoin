import re
import ast
import sys

key = 0
btc = 0

files = re.split(r'[\s\r\t]+', sys.argv[1])

for file in (files):
    print(file)
    with open(file) as f:
        for l in f:
            if re.search('Balance : ', l):
                l = l.strip()
                b = l.split('Balance : ')
                try:
                    b = ast.literal_eval(b[1])
                    n = b['result']['confirmed']
                    n += b['result']['unconfirmed']
                    btc += n
                    if n > 0:
                        print(l)
                    key += 1
                except Exception as e:
                    print(b[1])

key_space = 2**256
coverage = key / key_space * 100

print('%d BTC found from %d keys.' % (btc, key))
print('coverage %e [%%]' % (coverage))
