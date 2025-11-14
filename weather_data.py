import requests
import json


if __name__ == "__main__":
    data = requests.get("https://opendata-download-metfcst.smhi.se/api/category/snow1g/version/1/geotype/point/lon/16/lat/58/data.json")
    # data = requests.get("https://aftonbladet.se")

    # print(data.text)
    my_json_data = json.loads(data.text)
    for key in my_json_data.keys():
        print(key)

    # print(my_json_data['timeSeries'])

    # for sub_dict in my_json_data['timeSeries']:
    #     for key in sub_dict:
    #         print("\t", key)

    test = {12: "person 12", 13: "person 13", 14:14}

    print(json.dumps(test, indent=4))