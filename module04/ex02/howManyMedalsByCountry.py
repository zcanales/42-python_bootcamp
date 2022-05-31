from FileLoader import FileLoader

def howManyMedalsByCountry(df, team):
    df_country = df[df["Team"] == team]
    df_country = df_country.copy()
    df_country.dropna(subset=['Medal'], inplace=True)
    my_dict = {}
    for year in df_country["Year"].drop_duplicates():
        my_dict[year] = {'G': df_country[df_country['Medal'] == "Gold"]["Medal"].count(),
            'S': df_country[df_country['Medal'] == "Silver"]["Medal"].count(),
            'B': df_country[df_country['Medal'] == "Bronze"]["Medal"].count()
        }

    return(my_dict)

if __name__ == "__main__":
    fl = FileLoader()
    df = fl.load("athete_events.csv")
    print(howManyMedalsByCountry(df, "Finland"))
