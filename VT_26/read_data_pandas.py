import pandas as pd

def main():
    df = pd.read_csv("data.csv")
    print(df.head(5), end="\n\n")

    print(df.info(), end="\n\n")

    print(df.describe(), end="\n\n")

    for col in df.columns:
        print(col + '-', end='')

    print()

    print(df[(df["temperatur"] > 22) & (df["ljusstyrka"] < 300 )])

if __name__ == "__main__":
    main()