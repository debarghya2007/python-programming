def validate_file_extension(filename: str) -> str:
    """
    Extracts the file extension using rfind (equivalent to lastIndexOf) 
    and slicing (equivalent to substring), then validates against allowed types.
    """
    allowed_extensions = {"pdf", "docx", "zip"}

    # Find the last occurrence of '.' (returns -1 if not found)
    dot_index = filename.rfind(".")

    # Reject if no dot is present or if filename ends with a dot
    if dot_index == -1 or dot_index == len(filename) - 1:
        return "Rejected — invalid file type"

    # Extract extension and convert to lowercase for case-insensitive check
    extension = filename[dot_index + 1:].lower()

    if extension in allowed_extensions:
        return "Accepted"
    else:
        return "Rejected — invalid file type"


def main():
    print("=== Assignment Upload Portal: File Extension Validator ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter filename (e.g., Assignment1.PDF): ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting validator session. Goodbye!")
            break

        if not user_input:
            print("Filename cannot be empty. Please try again.\n")
            continue

        result = validate_file_extension(user_input)
        print(f"Result: {result}\n")


if __name__ == "__main__":
    main()
