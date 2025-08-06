import argparse, importlib.metadata
from lncur.utils.link import link
from lncur.utils.make import make

def main() -> None:
    # Parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="Prints version",action="store_true")
    parser.add_argument("-l", "--link", help="Symlinks cursors files",action="store_true")
    parser.add_argument("-m", "--make", help="Make a cursor theme directory",type=str)

    args = parser.parse_args()

    if args.version:
        print(f"Lncur v{importlib.metadata.version("lncur")}")
    if args.link:
        link()
    if args.make:
        make(args.make)
