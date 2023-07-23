import sys
import re
import glob

if __name__ == "__main__":

    num_arguments = len(sys.argv) - 1
    if num_arguments < 1:
        print('Usage: python %s addr file1 file2 ...' % (sys.argv[0]))
        sys.exit(1)

    FILES = []
    args = sys.argv[1:]
    for arg in args:
        array = glob.glob(arg)
        FILES.extend(array)

    FILES.sort()

    n = 0
    p2pkh = 0
    p2sh = 0
    p2w = 0
    other = 0
    for file in FILES:
        print(file)
        with open(file) as f:
            for line in f:
                if re.search(r'^1', line):
                    p2pkh += 1
                elif re.search(r'^3', line):
                    p2sh += 1
                elif re.search(r'^bc1', line):
                    p2w += 1
                else:
                    other += 1
                n += 1
    print('p2pkh: %d / %d (%.1f %%)' % (p2pkh, n, p2pkh/n*100.0))
    print('p2sh : %d / %d (%.1f %%)' % (p2sh , n, p2sh /n*100.0))
    print('p2w  : %d / %d (%.1f %%)' % (p2w  , n, p2w  /n*100.0))
    print('other: %d / %d (%.1f %%)' % (other, n, other/n*100.0))
