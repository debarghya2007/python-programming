def count_vowels_and_consonants(text: str) -> None:
    """
    Loops through each character using index-based traversal (simulating charAt),
    counts vowels and consonants case-insensitively, and ignores spaces.
    """
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    # Index-based loop simulating charAt()
    for i in range(len(text)):
        char = text[i]

        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print(f"Vowels: {vowel_count} | Consonants: {consonant_count}\n")


def main():
    print("=== Library Kiosk: Vowel & Consonant Counter ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter book title: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting session. Goodbye!")
            break

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        count_vowels_and_consonants(user_input)


if __name__ == "__main__":
    main()
