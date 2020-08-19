"""Usage:
  download.py <tickerlist> <investment> <filename>
  download.py -h | --help | --version
"""

__author__ = "Marc J Kirschner"
__copyright__ = "Copyright (C) 2020 Marc J Kirschner"
__license__ = "Public Domain"
__version__ = "0.1.1rc"

from docopt import docopt
from tda_options import get_put_info


# Command Line Utility
def main():
    args = docopt(__doc__, version=__version__)
    ticker_list = list(map(str.upper,args["<tickerlist>"].split(",")))
    investment = float(args["<investment>"])
    filename = args["<filename>"]
    if ".csv" not in filename:
        filename = f"{filename}.csv"

    put_info_text, put_info_df = get_put_info(ticker_list, investment)
    put_info_df.to_csv(filename)
    print(put_info_df.head())


if __name__ == "__main__":
    main()
