def check_typing_accuracy(original: str, typed: str) -> None:
    """
    Compares original and typed strings character by character.
    Calculates accuracy percentage and finds the position of the first mismatch.
    """
    total_length = len(original)
    
    # Handle length mismatch gracefully
    if len(typed) != total_length:
        print(f"Warning: Length mismatch! Original length is {total_length}, but typed length is {len(typed)}.")
        total_length = min(len(original), len(typed))

    matched_count = 0
    first_mismatch_pos = -1
    orig_char = ""
    typed_char = ""

    # Compare characters index by index
    for i in range(total_length):
        if original[i] == typed[i]:
            matched_count += 1
        else:
            # Record the very first mismatch position (1-based index)
            if first_mismatch_pos == -1:
                first_mismatch_pos = i + 1
                orig_char = original[i]
                typed_char = typed[i]

    # Calculate accuracy percentage
    accuracy = (matched_count / len(original)) * 100

    # Format output
    output_str = f"Matched: {matched_count}/{len(original)} | Accuracy: {accuracy:.2f}% | "
    
    if first_mismatch_pos != -1:
        output_str += f"First Mismatch at position {first_mismatch_pos} ('{orig_char}' vs '{typed_char}')"
    elif len(typed) != len(original):
        output_str += f"First Mismatch at position {total_length + 1} (Length Difference)"
    else:
        output_str += "No Mismatches"

    print(f"\n{output_str}\n")


def main():
    print("=== Typing Speed Test Accuracy Checker ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        original = input("Enter original passage: ")
        if original.lower() in ["exit", "quit"]:
            print("Exiting Typing Speed Checker.")
            break

        typed = input("Enter user's typed text: ")
        if typed.lower() in ["exit", "quit"]:
            print("Exiting Typing Speed Checker.")
            break

        check_typing_accuracy(original, typed)


if __name__ == "__main__":
    main()
