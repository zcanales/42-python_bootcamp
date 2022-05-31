from matplotlib import image
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from FileLoader import FileLoader

class MyPlotLib:
    @staticmethod
    def histogram(data, features):
        df[features].hist()
        #features = [f for f in features if np.issubdtype(data[f].dtype, np.number)]
        #data[features].hist()
        plt.show()
    @staticmethod
    def density(data, features):
        data[features].plot.kde(alpha=0.5)
        plt.show()
        pass
    @staticmethod
    def pair_plot(data, features):
        pd.plotting.scatter_matrix(df[features], alpha=0.2)
       # sns.pairplot(df[features], markers=".", height=2, plot_kws=dict(linewidth=0))
        plt.show()
    @staticmethod
    def box_plot(data, features):
        boxplot = df[features].boxplot()
        plt.show()

if __name__ == "__main__":
    fl = FileLoader()
    mpl = MyPlotLib()
    df = fl.load("athete_events.csv")
    mpl.histogram(df, ["Height" ,   "Weight"])
   # mpl.density(df, ["Height" ,   "Weight"])
   # mpl.pair_plot(df, ["Height" ,   "Weight"])
   # mpl.box_plot(df, ["Height" ,   "Weight"])
    