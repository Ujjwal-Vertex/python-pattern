import time

def countdown_timer(seconds):
    print(f"\nStarting countdown for {seconds} seconds...\n")
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Divides seconds into minutes and seconds
        time_format = f"{mins:02d}:{secs:02d}"
        print(time_format, end='\r')  # Print the time remaining, overwrite it every second
        time.sleep(1)  # Wait for one second
        seconds -= 1  # Decrease the time by one second

    print("\nTime's up! 🚨")
def main():
    print("Welcome to the Countdown Timer!")
    
    while True:
        try:
            countdown_seconds = int(input("Enter the time in seconds for the countdown: "))
            if countdown_seconds <= 0:
                print("Please enter a positive number greater than 0.")
            else:
                countdown_timer(countdown_seconds)
        except ValueError:
            print("Invalid input! Please enter a valid number.")

        # if the user wants to set another countdown
        repeat = input("\nDo you want to set another countdown? (y/n): ").lower()
        if repeat != 'y':
            print("\nGoodbye!")
            break

# Run the program
main()
