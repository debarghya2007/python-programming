class BookIssue:
    def __init__(self, title: str, borrower_name: str, days_overdue: int):
        self.title = title
        self.borrower_name = borrower_name
        self.days_overdue = days_overdue

    # Instance method: calculates fine for a specific book (Rs 5 per overdue day)[cite: 6]
    def fine_amount(self) -> float:
        return float(self.days_overdue * 5) if self.days_overdue > 0 else 0.0

    # Instance method: flags whether this specific book is overdue by > 14 days[cite: 6]
    def is_severely_overdue(self) -> bool:
        return self.days_overdue > 14

    # Static utility method: computes total fine across a list of book issues[cite: 6]
    @staticmethod
    def total_fine_collected(issues: list['BookIssue']) -> float:
        return sum(issue.fine_amount() for issue in issues)


if __name__ == "__main__":
    # Create an array/list of five BookIssue objects matching sample input[cite: 6]
    issues = [
        BookIssue("Clean Code", "Student A", 18),
        BookIssue("Effective Java", "Student B", 5),
        BookIssue("Refactoring", "Student C", 0),
        BookIssue("DSA Handbook", "Student D", 21),
        BookIssue("Design Patterns", "Student E", 9)
    ]

    # Print each book's title, overdue days, and status[cite: 6]
    for issue in issues:
        status = "Severely overdue" if issue.is_severely_overdue() else "OK"
        print(f"{issue.title} - {issue.days_overdue} days - {status}")

    # Compute and print total fine using the class name[cite: 6]
    total = BookIssue.total_fine_collected(issues)
    print(f"Total fine collected: Rs {total:.1f}")

'''
JUSTIFICATION FOR STATIC VS INSTANCE METHOD:

1. fine_amount() and is_severely_overdue() are instance methods because they 
   depend directly on the instance data of an individual book (self.days_overdue)[cite: 6]. 
   Each book issue has its own overdue period and calculated fine[cite: 6].

2. total_fine_collected() is static because calculating the total fine across multiple 
   books is a class-level utility operation[cite: 6]. It operates on a collection of 
   BookIssue objects as a whole rather than being bound to any single book instance[cite: 6].
'''
