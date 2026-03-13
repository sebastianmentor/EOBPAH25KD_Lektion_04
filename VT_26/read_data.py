import csv
from pathlib import Path

def main():
    with open("data.csv", "r", newline="", encoding='utf-8') as f:
        data = csv.reader(f)

        for row in data:
            print(row)

if __name__ == "__main__":
    main()