import os
import argparse
from lecode import utils
parser = argparse.ArgumentParser(
    prog="test_the_file.py",
    usage="python ...",
    description="hello"
)
parser.add_argument("-f", "--file", type=str, default=None,
                    help="this is path of the file")

if __name__ == '__main__':
    # args = parser.parse_args("-f D:\Prog\lecode\lecode\jzoffer\I0001_JZ05.py".split(' '))
    args = parser.parse_args()
    filename = r"D:\Prog\lecode\lecode\jzoffer\I0001_JZ05.py" if args.file is None else args.file
    print(utils.mytest_the_file(filename))
