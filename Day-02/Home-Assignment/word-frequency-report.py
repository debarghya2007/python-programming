import string
from collections import Counter

def print_filtered_word_frequency(feedback: str) -> None:
    """
    Normalizes feedback text, strips punctuation, filters out stop words,
    and prints word frequencies sorted in descending order of count.
    """
    # 1. Define stop-words set for quick O(1) lookup
    stop_words = {"the", "was", "and", "a", "is", "of", "in"}

    # 2. Normalize: lowercasing
    cleaned_text = feedback.lower()

    # 3. Strip punctuation (periods, commas, etc.)
    # Equivalent to using replace() for common punctuation
    for char in string.punctuation:
        cleaned_text = cleaned_text.replace(char, "")

    # 4. Split into individual words by whitespace
    words = cleaned_text.split()

    # 5. Filter out stop words and empty strings
    filtered_words = [word for word in words if word and word not in stop_words]

    if not filtered_words:
        print("No meaningful words found after filtering.\n")
        return

    # 6. Count frequencies (using Counter, Python's equivalent of HashMap frequency mapping)
    frequency_map = Counter(filtered_words)

    # 7. Sort by count descending (most_common() orders by count highest to lowest)
    print("\n--- Word Frequency Report ---")
    for word, count in frequency_map.most_common():
        print(f"{word}: {count}")
    print()


def main():
    print("=== T&P Stop-Word-Filtered Word Frequency Reporter ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter feedback paragraph: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting report session. Goodbye!")
            break

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        print_filtered_word_frequency(user_input)


if __name__ == "__main__":
    main()
