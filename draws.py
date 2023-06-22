import os
import pandas as pd

class Draws:
    data = {
        "date": [], "1": [], "2": [], "3": [],
        "4": [],"5": [], "E1": [], "E2": []
    }

    def __init__(self, path):
        numbers = sorted(os.listdir(path))  # files containing the draws per year
        self.parse_draws(numbers)

        # for draws in numbers:
            # self.parse_draws(os.path.join(path,draws))
        # df = pd.DataFrame(self.data)
        # df.index = df['date']
        # del df['date']
        # print(df)

    # parse the draws within each year
    def parse_draws(self, draws):
        for year in draws:


            with open(os.path.join(, "r") as draws:
                next(draws)  # ignore header 
                for draw in draws:
                    no = draw.rstrip().split('\t')
                    for i,v in enumerate(self.data.keys()):
                        self.data[v].append(no[i])







#        print(data)



