# main.py

from models.user import User
from models.tracker import Tracker

def main():
    print("Welcome to the NeuroTrack Mood & Mental Health Tracker!")
    
    user_name = input("Please enter your name: ")
    user_email = input("Please enter your email: ")
    
    user = User(user_name, user_email)
    
    tracker = Tracker()
    
    while True:
        print("\nMood Tracker Options:")
        print("1. Add Mood Entry")
        print("2. View Mood Entries")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            mood_type = input("Enter your mood (e.g., Happy, Sad, Anxious): ")
            tracker.add_mood_entry(mood_type)
            print("Mood entry added.")
        elif choice == '2':
            tracker.display_mood_entries()
        elif choice == '3':
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()