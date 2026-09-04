def reverse_customer_name(customer_name: str) -> str:
    """
    Reverses the given customer name and returns the reversed string.
    The original string remains unchanged.
    """
    # String slicing [start:stop:step] with a step of -1 reverses the sequence
    return customer_name[::-1]


def main():
    print("=== Customer Identity Verification System ===")
    print("Type 'exit' or 'quit' to exit.\n")

    while True:
        customer_name = input("Enter customer name: ").strip()

        # Check for exit condition
        if customer_name.lower() in ["exit", "quit"]:
            print("System session ended.")
            break

        if not customer_name:
            print("Name cannot be empty. Please try again.\n")
            continue

        # Process and reverse the name
        reversed_name = reverse_customer_name(customer_name)

        # Output results
        print(f"Original Name: {customer_name}")
        print(f"Reversed Name: {reversed_name}\n")


if __name__ == "__main__":
    main()
