import os
import pandas as pd

class Draws:

    draws = pd.DataFrame() 

    def __init__(self, path):
        years = []
        for year in sorted(os.listdir(path)):
            years.append(os.path.join(path, year))

        # create data frame from data
        self.draws = pd.DataFrame(self.parse_draws(years))
        self.draws.index = self.draws['date']
        del self.draws['date']

        print(self.draws)


    # parse the draws within each year
    def parse_draws(self, years):
        data = {
            "date": [], 
            "1": [], 
            "2": [], 
            "3": [],
            "4": [],
            "5": [], 
            "E1": [], 
            "E2": []
        }
        for year in years:
            with open(year,'r') as draws:
                next(draws)  # ignore header 
                for draw in draws:
                    no = draw.rstrip().split('\t')
                    for i,v in enumerate(data.keys()):
                        data[v].append(no[i])

        return data





