"""
Name: Lingzhi Hu
File name: dean_honor_roll.py
Description: This program repeatedly accepts student last name, first name,
             and GPAs. It stops when the last name entered is 'ZZZ'.
             It checks if the student qualifies for the Dean's List (GPA >= 3.5)
             or the Honor Roll (GPA >= 3.25) and prints an appropriate message.
"""

# Main loop
while True:
    # Get student's last name
    last_name = input("Enter student's last name (enter 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        print("Exiting the program.")
        break

    # Get student's first name
    first_name = input("Enter student's first name: ")

    # Get student's GPA as a float and verify valid input
    while True:
        try:
            gpa = float(input("Enter student's GPA (0.0 - 4.0): "))
            if 0.0 <= gpa <= 4.0:
                break
            else:
                print("GPA must be between 0.0 and 4.0. Please re-enter.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    # Check and print the result
    if gpa >= 3.5:
        print(f"{first_name} {last_name} qualifies for the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} qualifies for the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify for either honor.")

    # Print a blank line between records
    print()