# Will Brisbane CS500
# Assignment 3
# Part 1

# Ask the user to enter the charge for the food
food_charge = float(input("Enter the charge for the food: $"))

# Calculate tip (18%) and tax (7%)
tip = food_charge * 0.18
tax = food_charge * 0.07

# Calculate total
total = food_charge + tip + tax

# Display the results
print("\n--- Meal Cost Breakdown ---")
print(f"Food charge: ${food_charge:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")

# Part 2
# Ask the user for the current time in hours (0–23)
current_time = int(input("\nEnter the current time (0-23): "))

# Ask the user how many hours to wait for the alarm
wait_time = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the alarm time
alarm_time = (current_time + wait_time) % 24

# Display the result
print(f"\nThe alarm will go off at {alarm_time}:00 on a 24-hour clock.")