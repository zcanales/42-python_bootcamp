from FileLoader import FileLoader
import pandas as pd

class SpatioTemporalData:
    def __init__(self, df):
        self.df = df
    def when(self, location):
        df_when =  self.df[self.df["City"] == location]["Year"]
      #  Other step -> df_when["Year"]
        df_when = df_when.drop_duplicates()
      #  Other way o convert to list -> print(df_when.values.tolist())
       # print(df_when.reset_index())
        return (list(df_when))
    def where(self, data):
        df_where = self.df[self.df["Year"] == data]["City"].unique()
        return (df_where)

if __name__ == "__main__":
    fl = FileLoader()
    df = fl.load("athete_events.csv")
    std = SpatioTemporalData(df)
    print(std.when("Paris"))
    print(std.where(1900))