"""
This script processes a personnel csv file into a format that is easier to work with.

"""

from __future__ import division, print_function

import pandas as pd
import numpy as np
import sys
from dateutil.parser import parse

DATA_DIR = 'data/test.csv'


def _main():
    personnel = pd.read_csv(DATA_DIR)
    personnel.bio = clean_bio(personnel.bio)
    personnel.state = swap_codes(personnel.state)
    personnel = parse_date(personnel)
    personnel.to_csv('data/solution.csv', index=False)


def clean_bio(col):
    """
    Cleans messy features of the csv. Specifically, line breaks, tabs, and excess spaces.

    :param col: pd.Series with rows of type string
    :return: col: pd.Series with rows of type string
    """
    # Remove excess spaces, new lines, and tabs
    col = col.str.replace('\n|\t', ' ')
    col = col.str.replace('\s{2,}', ' ')

    # Remove leading and trailing spaces
    col = col.str.strip()

    return col


def swap_codes(col):
    """
    Swaps state abbreviations with their full names.

    :param col: pd.Series containing a column of state abbreviations
    :return: col: pd.Series with full state names
    """
    state_codes = pd.read_csv('data/state_abbreviations.csv')
    col = col.replace(state_codes.state_abbr.values,
                      state_codes.state_name.values)
    return col


def parse_date(df):
    """
    Parses date when given a dirty date string.

    Caveats
    ----
    If given only two, two-digit numbers (e.g., 05/13), the function assumes that
    it is the month and the day due to the ambiguous nature of the format.

    :param df: pd.DataFrame
    :return: datetime64 object
    """
    df['start_description'] = np.NaN #init start_description for entries that aren't dates
    for i, v in df.start_date.iteritems():
        try:
            df.start_date.iloc[i] = parse(v)
        except ValueError:
            print("{} failed to parse. Make sure that it is a date. Adding to \n"
                  "start_description".format(df.start_date[i]))
            df.start_description.iloc[i] = df.start_date.iloc[i]
            df.start_date.iloc[i] = pd.NaT
    return df


if __name__ == '__main__':
    sys.exit(_main())
