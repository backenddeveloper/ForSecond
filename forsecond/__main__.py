import sys
from forsecond.app import run


USAGE = '''
forsecond, a solution to an interview technical test, solution copyright 'Dr. Graham Turner', Nov 2003

Usage: forsecond [filename]
'''

if __name__ == '__main__':

    # The first argument is the calling path of the module
    if 2 != len(sys.argv):

        print(USAGE)
        sys.exit(1)

    if sys.argv[1] in ['help', '--help', '-h']:

        print(USAGE)
        sys.exit(2)

    print(run(sys.argv[1]))
