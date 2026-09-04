def get_bmi_status(bmi: double if False else float) -> str:
    """
    Classifies health status based on standard BMI ranges.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def print_wellness_report(heights: list[float], weights: list[float]) -> None:
    """
    Calculates BMI for each person and prints a formatted summary table.
    """
    print("\n" + "=" * 62)
    print(f"{'Person':<10} | {'Height (m)':<11} | {'Weight (kg)':<12} | {'BMI':<8} | {'Status':<12}")
    print("-" * 62)

    total_bmi = 0.0
    count = len(heights)

    for idx, (h, w) in enumerate(zip(heights, weights), start=1):
        bmi = w / (h * h)
        total_bmi += bmi
        status = get_bmi_status(bmi)
        print(f"Person {idx:<3} | {h:<11.2f} | {w:<12.2f} | {bmi:<8.2f} | {status:<12}")

    print("=" * 62)
    
    if count > 0:
        avg_bmi = total_bmi / count
        print(f"Average Team BMI: {avg_bmi:.2f} ({get_bmi_status(avg_bmi)})\n")


def main():
    print("=== Corporate Wellness Program: Team BMI Calculator ===")
    
    while True:
        try:
            num_people = int(input("Enter the number of team members: "))
            if num_people > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    heights = []
    weights = []

    print(f"\nPlease enter details for {num_people} employee(s):")
    for i in range(1, num_people + 1):
        print(f"\n--- Person {i} ---")
        
        # Get valid height
        while True:
            try:
                h = float(input("  Height (in meters, e.g., 1.75): "))
                if 0.5 <= h <= 2.5:
                    heights.append(h)
                    break
                print("  Please enter a realistic height between 0.5m and 2.5m.")
            except ValueError:
                print("  Invalid input! Please enter a numeric value.")

        # Get valid weight
        while True:
            try:
                w = float(input("  Weight (in kg, e.g., 70): "))
                if 20 <= w <= 300:
                    weights.append(w)
                    break
                print("  Please enter a realistic weight between 20kg and 300kg.")
            except ValueError:
                print("  Invalid input! Please enter a numeric value.")

    # Generate and display report
    print_wellness_report(heights, weights)


if __name__ == "__main__":
    main()
