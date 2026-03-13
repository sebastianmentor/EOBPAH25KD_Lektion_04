from rich.console import Console
import os

FILE_NAME = "my_file.txt"

console = Console()

def save_msg(msg:str) -> None:
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def print_messages() -> None:
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f.readlines():
                print(line, end="")
    except FileNotFoundError as e:
        print(console.print(e, style="bold red"))
    
def get_message_from_user() -> str:
    msg = input("Enter message to save: ")
    return msg


def main():
    # setup  
    if os.path.exists(FILE_NAME): 
        print("Filen existerar! Inget behövs göras.")
    else:
        print("Filen existerade inte! Vi ser till att skapa filen!")
        with open(FILE_NAME, "w", encoding="utf-8") as f:...

    # program start
    while True:
        print("1. Print messages")
        print("2. Add message")
        print("3. Quit")

        choice = input("Enter choice: ")

        match choice:
            case "1":
                print_messages()

            case "2":
                msg = get_message_from_user()
                if msg:
                    save_msg(msg)
                else:
                    console.print("No message recieved!!! What are you doing?", style="red bold")    
            case "3":
                print("Good bye!")
                break
            case _:
                print("Invalid choice!")
      
    
if __name__=="__main__":
    main()