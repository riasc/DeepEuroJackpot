import os
import pandas as pd
from pathlib import Path
import numpy as np

import draws as dr


def main():

    nrs = dr.Draws('./numbers')

    # '''
    # numbers_path = "./numbers"
    # numbers = os.listdir(numbers_path)

    # draws = {}

    # #pd.DataFrame()

    # for file in numbers:
        # year = Path(file).stem
        # year_numbers = open(os.path.join("./numbers",file), "r")
        # draws[year] = pd.DataFrame()

        # for draw in year:
            # d = draw.rstrip().split("\t") # create list of numbers
            # draws[year].add(d)

    # print(draws)
    # '''




main()
