def parse_inventory_record(csv_line: str) -> None:
    """
    Splits a CSV string into fields, validates the record structure,
    and prints formatted product inventory details.
    """
    # Split by comma and strip extra whitespace around fields
    fields = [field.strip() for field in csv_line.split(",")]

    # Validate that exactly 3 fields exist (ProductName, SKU, Quantity)
    if len(fields) != 3 or any(field == "" for field in fields):
        print("Invalid Record\n")
        return

    product_name, sku, qty = fields
    print(f"Product: {product_name} | SKU: {sku} | Qty: {qty}\n")


def main():
    print("=== Warehouse Product Inventory CSV Parser ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter Inventory CSV Record (ProductName,SKU,Quantity): ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting parser session. Goodbye!")
            break

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        parse_inventory_record(user_input)


if __name__ == "__main__":
    main()
