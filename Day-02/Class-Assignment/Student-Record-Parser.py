def parse_student_record(csv_line: str) -> None:
    """
    Splits a CSV string into fields, validates the record structure,
    and prints formatted student details.
    """
    # Split by comma
    fields = [field.strip() for field in csv_line.split(",")]

    # Validate that exactly 3 fields exist (Name, RollNumber, Department)
    if len(fields) != 3 or any(field == "" for field in fields):
        print("Invalid Record\n")
        return

    name, roll_no, dept = fields
    print(f"Name: {name} | Roll No: {roll_no} | Dept: {dept}\n")


def main():
    print("=== T&P CSV Student Record Parser ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter CSV Record (Name,RollNumber,Dept): ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting parser session. Goodbye!")
            break

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        parse_student_record(user_input)


if __name__ == "__main__":
    main()
