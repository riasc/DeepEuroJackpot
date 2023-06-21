import os
import pandas as pd

class Draws:
    data = [] 

    def __init__(self, path):
        numbers = sorted(os.listdir(path))  # files containing the draws per year
        for draws in numbers:
            self.parse_draws(os.path.join(path,draws))

    # parse the draws within each year
    def parse_draws(self,path):
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
        with open(path, "r") as draws:
            for draw in draws:
                no = draw.rstrip().split('\t')


