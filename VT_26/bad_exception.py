# prevents CTRL + C 
# prevents CTRL + Z 
# and more... VERY BAD

while True:
    try:
        user_input = input("Enter somthing or q to quit: ")

        if user_input == "q": break

        print(user_input)
    except:
        print("Exception happend!")
    
    finally:
        print("Allways runs!")