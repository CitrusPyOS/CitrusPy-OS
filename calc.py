def main():
    print("Calculator")
    print("__________")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter a calculation: ")

        if user_input.lower() == "exit":
            print("Exiting...")
            break

        try:
            result = eval(user_input)
            print(f"Result:{result}")
        except Exception as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()