# Will Brisbane 
# CS500
# Week 5

# Part 1
# Method to validate int input
def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                # Rather than duplicating error messaging, raise an error so exception handling takes care of it
                raise ValueError
        except ValueError:
            print("Please enter a positive whole number.")

# Method to validate float input
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                # Rather than duplicating error messaging, raise an error so exception handling takes care of it
                raise ValueError
        except ValueError:
            print("Please enter a positive number.")

def main():
	# Initialize totals before adding in loops
    total_rainfall = 0
    total_months = 0

    years = get_int("Enter number of years: ")

    # Loop through years
    for year in range(1, years + 1):
        print(f"\nYear {year}")
        # Loop through months 
        for month in range(1, 13):
            rainfall = get_float(f"  Enter rainfall for month {month} (in inches): ")
            total_rainfall += rainfall
            total_months += 1

    # Calculate average
    average_rainfall = total_rainfall / total_months

    # Display results
    print("\n--- Rainfall Report ---")
    print(f"Number of months: {total_months}")
    print(f"Total rainfall: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")


if __name__ == "__main__":
    main()