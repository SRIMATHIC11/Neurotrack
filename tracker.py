from datetime import datetime

class MoodEntry:
    def __init__(self, mood_type, timestamp):
        self.__mood_type = mood_type
        self.__timestamp = timestamp

    def display_entry(self):
        return f"Mood: {self.__mood_type}, Time: {self.__timestamp}"

class Tracker:
    def __init__(self):
        self.__mood_entries = []

    def add_mood_entry(self, mood_type):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = MoodEntry(mood_type, timestamp)
        self.__mood_entries.append(entry)

    def display_mood_entries(self):
        if not self.__mood_entries:
            print("No mood entries yet.")
        else:
            for idx, entry in enumerate(self.__mood_entries, 1):
                print(f"{idx}. {entry.display_entry()}")