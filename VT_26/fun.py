from datetime import datetime

SWEDISH_MAP = {
    0: "Måndag",
    1: "Tisdag",
    2: "Onsdag",
    3: "Torsdag",
    4: "Fredag",
    5: "Lördag",
    6: "Söndag"
}

def main():
    now = datetime.now()
    print(SWEDISH_MAP[now.weekday()])    
    print(now.date())
    print(now.strftime("%H:%M:%S - %Y/%m/%d"))

if __name__ == "__main__":
    main()