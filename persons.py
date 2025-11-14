from rich import print
import json


persons = {1234:
           {"name":"Sebastian",
            "age":44,
            "color": "Blue"},

            3333:
            {"name":"KalleAnka",
             "age":22,
             "color":"Red"}
}

def validate_age(age:int):
    if 0<=age<=130: return
    raise ValueError("Invalid age, must be between 0 and 130!")

def main():
    while True:
        print("1. Create person")
        print("2. Print all persons")
        print("0. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                new_id = int(input("Enter new id: "))
                new_name = input("Enter name: ")
                new_age = int(input("Enter age: "))
                validate_age(new_age)

            except ValueError as e:
                print(e)
                print("An exception happen but we handle it")
            
            except TypeError as e:
                print("We catch a TypeError! LOOK:")
                print(e)

            except:
                print(f"We catch something, look")

        if choice == "2":
            print(persons)

        if choice == "0": break
                






if __name__ == "__main__":
    main()
    # with open("my_json_data.json","w") as f:
    #     json.dump(persons, f, indent=4)

    # with open("my_json_data.json","r") as f:
    #     my_data = json.load(f)
        
    # print(my_data)
    # print(my_data[1234])

    # with open("my_json_data.json","r") as f:
    #     rich.print_json(f.read())
            
    # print(type(my_data))
    # rich.print_json(my_data)