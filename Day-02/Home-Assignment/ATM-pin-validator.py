def check_pin_length(pin: str) -> None:
    """
    Checks if the entered PIN string has a length of exactly 4 characters.
    """
    if len(pin) != 4:
        print("Invalid PIN — must be exactly 4 digits.\n")
    else:
        print("PIN length OK.\n")


def main():
    print("=== ATM PIN Length Validator ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter PIN: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting validator session. Goodbye!")
            break

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        check_pin_length(user_input)


if __name__ == "__main__":
    main()
