# Task 1 start 
print("Task 1 Display Menu")
def display_menu():

    print("Menu:")
    print("a. Print help menu")
    print("b. Exit the program")

def main():
    
    display_menu()  
    while True:
        user_input = input("wildlife> ")
        if user_input == 'help':
            display_menu()  
        elif user_input == 'exit':
            print("Exiting the program.")
            return  
        else:
            print("Invalid command. Please enter 'help' or 'exit'.")
if __name__ == "__main__":
    main()
# Task 2 End # 