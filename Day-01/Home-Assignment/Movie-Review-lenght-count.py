import string

def classify_word_lengths(review: str) -> None:
    """
    Splits a movie review into individual words, strip punctuation, 
    and classifies each by length:
    - Short: 1-4 letters
    - Medium: 5-8 letters
    - Long: 9+ letters
    """
    if not review.strip():
        print("Review is empty.\n")
        return

    # Split review into words
    words = review.split()

    short_count = 0
    medium_count = 0
    long_count = 0

    for word in words:
        # Strip surrounding punctuation (e.g., "fantastic!" -> "fantastic")
        clean_word = word.strip(string.punctuation)
        length = len(clean_word)

        if length == 0:
            continue

        if 1 <= length <= 4:
            short_count += 1
        elif 5 <= length <= 8:
            medium_count += 1
        else:  # 9+ letters
            long_count += 1

    print(f"Short: {short_count} | Medium: {medium_count} | Long: {long_count}\n")


def main():
    print("=== Movie Review Word Length Profiler ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter movie review: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting profiler session. Goodbye!")
            break

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        classify_word_lengths(user_input)


if __name__ == "__main__":
    main()
