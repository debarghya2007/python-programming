def mask_phone_number(phone: str) -> str:
    """
    Validates a phone number (must be 10 digits) and returns a masked 
    string in the format 'XXXXXX-1234'.
    """
    # Remove any extra whitespace
    clean_phone = phone.strip()

    # Validate length and ensure all characters are digits
    if len(clean_phone) != 10 or not clean_phone.isdigit():
        return "Invalid phone number"

    # Extract the last 4 digits using slicing
    last_four = clean_phone[6:]

    # Construct the masked string
    return f"XXXXXX-{last_four}"


def main():
    print("=== Call Center Masked Phone Number Formatter ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter phone number: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting session. Goodbye!")
            break

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        result = mask_phone_number(user_input)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
