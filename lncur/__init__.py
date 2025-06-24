import argparse, importlib.metadata
from lncur.utils import lncur

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="Prints version",action="store_true")
    parser.add_argument("-l", "--link", help="Symlinks cursors files",action="store_true")

    args = parser.parse_args()

    if args.version:
        print(f"Lncur v{importlib.metadata.version("lncur")}")
    if args.link:
        lncur()