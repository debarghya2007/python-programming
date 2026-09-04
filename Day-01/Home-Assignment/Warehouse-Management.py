def analyze_inventory(sectionA: list[int], sectionB: list[int]) -> None:
    """
    Computes total quantities for two warehouse sections, determines if they are balanced,
    and identifies the highest quantity item across both sections.
    """
    total_A = sum(sectionA)
    total_B = sum(sectionB)
    
    status = "Balanced" if total_A == total_B else "Not Balanced"

    # Track maximum quantity, section name, and 1-based index
    max_qty = -1
    max_section = ""
    max_item_num = -1

    # Check Section A
    for idx, qty in enumerate(sectionA, start=1):
        if qty > max_qty:
            max_qty = qty
            max_section = "Section A"
            max_item_num = idx

    # Check Section B
    for idx, qty in enumerate(sectionB, start=1):
        if qty > max_qty:
            max_qty = qty
            max_section = "Section B"
            max_item_num = idx

    print(
        f"Section A Total: {total_A} | "
        f"Section B Total: {total_B} | "
        f"Status: {status} | "
        f"Highest Quantity: {max_qty} ({max_section}, Item {max_item_num})\n"
    )


def parse_input_array(prompt_text: str) -> list[int]:
    """
    Prompts the user for a space or comma-separated list of integers.
    """
    while True:
        raw_input = input(prompt_text).strip()
        if raw_input.lower() in ["exit", "quit"]:
            return []

        try:
            clean_input = raw_input.replace(",", " ").split()
            if not clean_input:
                print("Input cannot be empty. Please enter integer values.")
                continue
            return [int(val) for val in clean_input]
        except ValueError:
            print("Invalid input! Please enter numbers only (e.g., 20 15 30).")


def main():
    print("=== Warehouse Inventory Balancer ===")
    print("Type 'exit' or 'quit' at any prompt to stop.\n")

    while True:
        print("--- New Inventory Assessment ---")
        sectionA = parse_input_array("Enter quantities for Section A (e.g., 20 15 30): ")
        if not sectionA:
            print("Exiting inventory balancer.")
            break

        sectionB = parse_input_array("Enter quantities for Section B (e.g., 25 10 30): ")
        if not sectionB:
            print("Exiting inventory balancer.")
            break

        # Verify equal number of items across sections
        if len(sectionA) != len(sectionB):
            print(
                f"\nError: Section length mismatch! Section A has {len(sectionA)} items, "
                f"while Section B has {len(sectionB)} items. Please re-enter.\n"
            )
            continue

        # Run analysis
        print()
        analyze_inventory(sectionA, sectionB)


if __name__ == "__main__":
    main()
