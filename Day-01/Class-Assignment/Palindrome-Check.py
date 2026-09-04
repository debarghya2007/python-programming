def is_palindrome_iterative(text: str) -> bool:
    """
    Approach 1: Two-pointer iterative comparison.
    Moves pointers from opposite ends toward the middle.
    """
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_recursive(text: str) -> bool:
    """
    Approach 2: Recursive check.
    Compares boundary characters and shrinks the substring.
    """
    # Base case: empty string or single character is a palindrome
    if len(text) <= 1:
        return True

    # Check boundary characters
    if text[0] != text[-1]:
        return False

    # Recurse on the inner substring
    return is_palindrome_recursive(text[1:-1])


def is_palindrome_array_reversal(text: str) -> bool:
    """
    Approach 3: Array reversal check.
    Converts string to a character list, reverses it, and compares.
    """
    char_array = list(text)
    reversed_array = list(reversed(char_array))

    return char_array == reversed_array


def verify_palindrome(text: str) -> None:
    """
    Runs all 3 methods, prints results, and asserts that all approaches agree.
    """
    res_iter = is_palindrome_iterative(text)
    res_rec = is_palindrome_recursive(text)
    res_arr = is_palindrome_array_reversal(text)

    # Sanity check: Ensure all 3 approaches return the same boolean result
    assert res_iter == res_rec == res_arr, "Mismatch detected among palindrome algorithms!"

    def format_res(is_pal: bool) -> str:
        return "Palindrome" if is_pal else "Not Palindrome"

    print(f"\nResult for '{text}':")
    print(
        f"Iterative: {format_res(res_iter)} | "
        f"Recursive: {format_res(res_rec)} | "
        f"Array Reversal: {format_res(res_arr)}\n"
    )


def main():
    print("=== QA Text Verification Toolkit: Palindrome Checker ===")
    print("Type 'exit' or 'quit' to end the program.\n")

    while True:
        user_input = input("Enter text to check: ")

        # Check for exit command
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting Palindrome Checker. Goodbye!")
            break

        # Run verification on user input
        verify_palindrome(user_input)


if __name__ == "__main__":
    main()
