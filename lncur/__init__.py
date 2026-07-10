import argparse
import importlib.metadata
from lncur.utils.link import link
from lncur.utils.make import make

def main() -> None:
  # Parser
  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--version", help="Prints version", action="store_true")
  parser.add_argument("-l", "--link", help="Symlinks cursors files", action="store_true")
  parser.add_argument("-m", "--make", help="Generate a cursor theme template", type=str)

  args = parser.parse_args()

  if args.version:
    print(f"Lncur v{importlib.metadata.version("lncur")}")
  elif args.link:
    link()
  elif args.make:
    # make(args.make)
    print(args.make)
  else:
    parser.print_help()
