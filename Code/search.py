import sys
from utils import *

def main():
    filename = sys.argv[1]
    print(parse_grid(filename=filename))

if __name__ == "__main__":
    main()