from FileLoader import FileLoader
import pandas as pd

def proportionBySport(df, year, sport, gender):
    df = df.drop_duplicates(subset=["Name", "Sport", "Event"])
    sport = df[df["Sport"] == sport]
    sport_year = sport[sport["Year"] == year]
    sport_gender = sport[sport["Sex"] == gender]
    if (len(sport_year) == 0):
        return ("0")
    return (len(sport_gender) / sport_gender["Sport"].count())
    #return (len(sport_gender) / len(sport_year))
    





if __name__ == "__main__":
    fl = FileLoader()
    df = fl.load("athete_events.csv")
    print(proportionBySport(df, 1952, "Athletics", "M"))