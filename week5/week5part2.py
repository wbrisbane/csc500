# Will Brisbane 
# CS500
# Week 5

# Part 2
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

def main():
    # Ask user for number of books
    books = get_int("Enter the number of books purchased this month: ")

    # Determine points
    if books <= 1:
        points = 0
    elif books <= 3:
        points = 5
    elif books <= 5:
        points = 15
    elif books <= 7:
        points = 30
    else:
        points = 60

    # Display result
    print(f"Points awarded: {points}")

if __name__ == "__main__":
    main()