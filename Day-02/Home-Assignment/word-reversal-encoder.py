def reverse_each_word(sentence: str) -> str:
    """
    Splits a sentence into individual words, reverses each word,
    and joins them back together preserving original word order.
    """
    words = sentence.split(" ")
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)


def main():
    print("=== Mirror Text: Word Reversal Encoder ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter sentence: ")

        if user_input.strip().lower() in ["exit", "quit"]:
            print("Exiting encoder session. Goodbye!")
            break

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        result = reverse_each_word(user_input)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
