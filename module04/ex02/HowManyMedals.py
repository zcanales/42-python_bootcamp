from FileLoader import FileLoader

def howManyMedals(df, name):
   
    df = df.drop_duplicates(subset=["Name", "Sport", "Event", "Year", "City"])
    # Shorter way:
#    df_three = df[df["Name"] == name][["Year", "Medal"]]
    df_name = df[df["Name"] == name]
    # To avoid error -> A value is trying to be set on a copy of a slice from a DataFrame
    df_name = df_name.copy()
    df_name.dropna(subset=['Medal'], inplace=True)
    df_filter = df_name[["Year", "Medal"]]
    my_dic = {}
    for year in df_filter["Year"].drop_duplicates():
        G = df_filter[(df_filter["Year"] == year) & (df_filter["Medal"] == "Gold")].count()
        S = df_filter[(df_filter["Year"] == year) & (df_filter["Medal"] == "Silver")].count()
        B = df_filter[(df_filter["Year"] == year) & (df_filter["Medal"] == "Bronze")].count()
        my_dic[year] = {'G': G["Medal"], 'S' : S["Medal"], 'B' : B["Medal"]}
       # Other way to do more simplified:
       # my_dict[year] = {'G': df_bis['Medal'][(df_bis['Year'] == year) & (df_bis['Medal'] == 'Gold')].count(),
            #'S': df_bis['Medal'][(df_bis['Year'] == year) & (df_bis['Medal'] == 'Silver')].count(),
            #'B': df_bis['Medal'][(df_bis['Year'] == year) & (df_bis['Medal'] == 'Bronze')].count()}
    return (my_dic)

    #return df_name
    
if __name__ == "__main__":
    fl = FileLoader()
    df = fl.load("athete_events.csv")
    print(howManyMedals(df, "Kjetil Andr Aamodt"))
