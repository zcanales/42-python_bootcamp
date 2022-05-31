from FileLoader import FileLoader
import pandas as pd

def youngestFellah(df, year):
    """
    Write a function youngestFellah that takes two arguments:
    • a pandas.DataFrame which contains the dataset
    • an Olympic year.
    The function returns a dictionary
    containing the age of the youngest woman and man who took part in the
    Olympics on that year. The name of the dictionary’s keys is up to you,
    but it must be self-explanatory.
    """
    data = df[["Year", "Sex", "Age"]]
    df_year = df[df["Year"] == year]
    df_mas = df_year[df_year["Sex"] == 'M']
    df_fem = df_year[df_year["Sex"] == 'F']
    df_fem = df_fem.Age.min()
    df_mas = df_mas.Age.min()
    mydic = {"f" : df_fem, "m" : df_mas}
    return mydic


if __name__ == "__main__":
    fl = FileLoader()
    df = fl.load("athete_events.csv")
    print(youngestFellah(df, 1994))