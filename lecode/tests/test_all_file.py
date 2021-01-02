import os
import argparse
from lecode import utils

parser = argparse.ArgumentParser(
    prog="test_the_file.py",
    usage="python ...",
    description="hello"
)
parser.add_argument("-p", "--path", type=str, default=None,
                    help="this is path")

if __name__ == '__main__':
    # args = parser.parse_args("-f D:\Prog\lecode\lecode\jzoffer\I0001_JZ05.py".split(' '))
    args = parser.parse_args()
    path = r"D:\Prog\lecode\lecode\jzoffer" if args.path is None else args.path

    path_list = os.listdir(path)

    for p in path_list:
        if p.startswith("__"): continue
        filename = os.path.join(os.path.abspath(path), p)
        if os.path.isfile(filename):
            print(utils.mytest_the_file(filename))
