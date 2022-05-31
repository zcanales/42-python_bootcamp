from matplotlib import image
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from FileLoader import FileLoader

class Komparator:
    def __init__(self, df):
        self.df = df
    

    def compare_box_plots(self, categorical_var, numerical_var):
        nb = len(self.df[categorical_var].drop_duplicates())
        f, ax = plt.subplots(1, nb + 1, figsize=(9, 4))
        for i, elem in enumerate(self.df[categorical_var].drop_duplicates()):
            ax[i].set_title(f'Histogram for {categorical_var} with value {elem}')
            ax[i].plot(df[[categorical_var] == elem], df[[categorical_var] == elem])

if __name__ == "__main__":
    fl = FileLoader()
    df = fl.load("athete_events.csv")
    kom = Komparator(df)
    kom.compare_box_plots("Sex", "Height")

