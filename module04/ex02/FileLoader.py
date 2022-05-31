import pandas as pd

class FileLoader:
    @staticmethod
    def load(path):
        try:
            arr = pd.read_csv(path)
            print(f"dimension -> {arr.shape}")
            # print("({} x {})".format(arr.shape[0], arr.shape[1]))
        except :
           exit("Not a valid path")
        return arr
    @staticmethod
    def display(df, n):
        if n >= 0:
            print(df.head(n))
        else:
            n *= -1
            print(df.tail(n))


if __name__ == "__main__":
    fl = FileLoader()
    df = fl.load("solar_system_census.csv")
    fl.display(df, 2)