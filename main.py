from datetime import datetime

issues = []
completed_issues = []


def submit_issue(city1, problem1):
    issue = {
        'id': len(issues) + 1,
        'city': city1,
        'problem': problem1,
        'completed': False,
        'timestamp': datetime.utcnow()
    }
    issues.append(issue)
    return issue


def get_issues(completed=False):
    return completed_issues if completed else issues


def mark_issue_completed(issue_id1):
    for issue in issues:
        if issue['id'] == issue_id1:
            issue['completed'] = True
            completed_issues.append(issue)
            issues.remove(issue)
            return issue
    return None


if __name__ == "__main__":
    while True:
        print("\n1. Submit Issue")
        print("2. View Incomplete Issues")
        print("3. View Completed Issues")
        print("4. Mark Issue as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            city = input("Enter the city: ")
            problem = input("Enter the problem: ")
            submitted_issue = submit_issue(city, problem)
            print("Issue submitted successfully!")

        elif choice == '2':
            incomplete_issues = get_issues(completed=False)
            print("\nIncomplete Issues:")
            for idx, incomplete_issue in enumerate(incomplete_issues):
                print(f"{idx + 1}. {incomplete_issue['city']} - {incomplete_issue['problem']}")

        elif choice == '3':
            completed_issues = get_issues(completed=True)
            print("\nCompleted Issues:")
            for idx, completed_issue in enumerate(completed_issues):
                print(f"{idx + 1}. {completed_issue['city']} - {completed_issue['problem']} (Completed)")

        elif choice == '4':
            issue_id = int(input("Enter the issue ID to mark as completed: "))
            marked_issue = mark_issue_completed(issue_id)
            if marked_issue:
                print(f"Issue {issue_id} marked as completed!")
            else:
                print("Invalid issue ID.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
