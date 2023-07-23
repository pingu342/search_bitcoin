import sys
import re
import glob

def get_first_line(path):
    with open(path) as f:
        return f.readline().rstrip('\n')
    return None

def parse_line(line):
    return re.split(r'\s+', line)

def get_balance(addr, file):
    with open(file) as f:
        for line in f:
            array = parse_line(line)
            if array[0] == addr:
                return array[1]

    return 0

if __name__ == "__main__":

    num_arguments = len(sys.argv) - 1
    if num_arguments < 2:
        print('Usage: python %s addr file1 file2 ...' % (sys.argv[0]))
        sys.exit(1)

    ADDR = sys.argv[1]

    FILES = []
    args = sys.argv[2:]
    for arg in args:
        array = glob.glob(arg)
        FILES.extend(array)

    FILES.sort()
    NUM = len(FILES)

    flags = []
    for i in range(NUM):
        array = parse_line(get_first_line(FILES[i]))
        flags.append(array[0] <= ADDR)
        if i > 0 and flags[i]:
            flags[i-1] = False

    for i in range(NUM):
        if flags[i]:
            print(get_balance(ADDR, FILES[i]));

