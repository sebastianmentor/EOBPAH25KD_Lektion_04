import json 
import requests
from datetime import datetime
from rich import print_json

URL = "https://opendata-download-metfcst.smhi.se/api/category/snow1g/version/1/geotype/point/lon/16/lat/58/data.json"

DATA = [
    {"Sebastian":
     {"age": 88,
      "food": "Hamburgare",
      "color": "red"   
     }
    },
    {"Nina":
    {"age": 22,
    "food": "Pizza",
    "color": "blue"   
    }
    }
]

# jobbigt!
with open("Example.txt", "w", encoding='utf-8') as f:
    for dic in DATA:
        for name, d in dic.items():
            f.write(name + "\n")
            for key, val in d.items():
                f.write("\t" + str(key) + ":" + str(val) + "\n")


with open("Example2.json", "w", encoding='utf-8') as f:
    json.dump(DATA, f, indent=2)


wether_data = requests.get(URL)

# print(wether_data.text)

# print_json(wether_data.text, indent=2)
wether_data_dict = json.loads(wether_data.text)

# print(f"{type(wether_data_dict)=}")

print(wether_data_dict.keys())

for ts in wether_data_dict["timeSeries"]:
    time = datetime.strptime(ts["time"], "%Y-%m-%dT%H:%M:%SZ")
    temp = ts["data"]["air_temperature"]
    print(f"Time/temp:{time.hour} - {temp}")