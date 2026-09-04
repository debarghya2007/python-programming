def find_longest_streak(signal_log: str) -> None:
    """
    Scans a string of signal readings ('R', 'Y', 'G') and determines 
    the longest consecutive streak of any single color.
    """
    if not signal_log:
        print("No signal readings provided.\n")
        return

    # Standardize casing to handle lower-case inputs gracefully
    signal_log = signal_log.upper()

    max_streak_color = signal_log[0]
    max_streak_length = 1

    current_color = signal_log[0]
    current_length = 1

    # Traversal starting from the second character
    for i in range(1, len(signal_log)):
        if signal_log[i] == current_color:
            current_length += 1
        else:
            # Check if previous streak broke the record
            if current_length > max_streak_length:
                max_streak_length = current_length
                max_streak_color = current_color
            
            # Reset counters for the new color streak
            current_color = signal_log[i]
            current_length = 1

    # Final check for a streak that extends to the very end of the string
    if current_length > max_streak_length:
        max_streak_length = current_length
        max_streak_color = current_color

    print(f"Longest Streak: '{max_streak_color}' repeated {max_streak_length} time(s)\n")


def main():
    print("=== Traffic Signal Streak Analyzer ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter signal log (e.g., RRGGGYRR): ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting analyzer session. Goodbye!")
            break

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        find_longest_streak(user_input)


if __name__ == "__main__":
    main()
