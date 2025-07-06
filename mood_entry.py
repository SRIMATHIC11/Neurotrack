class MoodEntry:
    def __init__(self, mood_type: str, timestamp: str):
        self.__mood_type = mood_type  # private attribute
        self.__timestamp = timestamp  # private attribute

    def get_mood_type(self) -> str:
        return self.__mood_type

    def get_timestamp(self) -> str:
        return self.__timestamp

    def display_entry(self) -> str:
        return f"Mood: {self.__mood_type}, Timestamp: {self.__timestamp}"