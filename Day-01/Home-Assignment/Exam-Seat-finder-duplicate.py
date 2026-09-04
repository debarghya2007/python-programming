def check_duplicate_seats(seat_numbers: list[int]) -> None:
    """
    Checks for duplicate seat numbers using nested loops without relying on 
    collections or built-in set operations.
    """
    duplicates = []
    n = len(seat_numbers)

    # Compare every element with all subsequent elements
    for i in range(n):
        for j in range(i + 1, n):
            if seat_numbers[i] == seat_numbers[j]:
                # Add to duplicates list if not already recorded
                if seat_numbers[i] not in duplicates:
                    duplicates.append(seat_numbers[i])

    # Output results
    if duplicates:
        for seat in duplicates:
            print(f"Duplicate Seat Number Found: {seat}")
    else:
        print("No Duplicate Seats Found")


def main():
    print("=== Exam Hall Seat Duplication Checker ===")
    print("Enter seat numbers separated by spaces or commas (or 'exit' to quit).\n")

    while True:
        user_input = input("Enter seat numbers: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting checker session.")
            break

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        # Parse user input into an array of integers
        try:
            # Replaces commas with spaces and splits into individual strings
            clean_input = user_input.replace(",", " ").split()
            seat_numbers = [int(seat) for seat in clean_input]
            
            # Check for duplicates
            check_duplicate_seats(seat_numbers)
            print()

        except ValueError:
            print("Invalid input! Please enter valid integer seat numbers only.\n")


if __name__ == "__main__":
    main()
