# Will Brisbane 
# CS500
# Week 7

# Separate dictionary creation for potential future reuse
def makedictionaries():
    # Dictionary for room number
    # Course Number - Room number
    room_numbers = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    # Dictionary for instructors
    # Course Number  - Instructor last name
    instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    # Dictionary for meeting time
    # Course Number  - Meeting time
    meeting_times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }
    return room_numbers, instructors, meeting_times

def main():
    # Build dictionaries
    room_numbers, instructors, meeting_times = makedictionaries()

    # Sentinal for loop. Keep providing info until user exits
    proceed = True
    while proceed :
        # Ask user for course number
        course = input("Enter a course number (X or x to exit): ").strip().upper()

        # If course is key in room numbers, should be expected in all.
        # Not checking for simplicity but could do more complex checks for each field
        if course in room_numbers:
            print(f"\nCourse: {course}")
            print(f"Room: {room_numbers[course]}")
            print(f"Instructor: {instructors[course]}")
            print(f"Time: {meeting_times[course]}")
        elif course == "X":
            print("Have a nice day")
            proceed = False
        else:
            print("Course not found.")

if __name__ == "__main__":
    main()