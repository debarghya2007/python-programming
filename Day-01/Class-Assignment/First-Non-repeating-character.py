from collections import Counter

def find_first_non_repeating_char(text: str) -> str | None:
    """
    Computes character frequencies and returns the first character
    that appears exactly once. Returns None if no such character exists.
    """
    # Count frequency of each character
    char_counts = Counter(text)
    
    # Scan from left to right to find the first character with count == 1
    for char in text:
        if char_counts[char] == 1:
            return char
            
    return None


def main():
    print("=== The Unique Letter Hunt Mini-Game ===")
    print("Type 'exit' or 'quit' to end.\n")

    while True:
        user_input = input("Enter a word or sentence: ")

        # Exit condition
        if user_input.lower() in ["exit", "quit"]:
            print("Thanks for playing! Goodbye.")
            break

        if not user_input:
            print("Input cannot be empty. Try again.\n")
            continue

        # Find first non-repeating character
        result = find_first_non_repeating_char(user_input)

        # Output result
        if result:
            print(f"First Non-Repeating Character: '{result}'\n")
        else:
            print("No Non-Repeating Character Found\n")


if __name__ == "__main__":
    main()
