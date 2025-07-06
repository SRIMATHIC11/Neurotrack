def validate_mood_input(mood):
    valid_moods = ['happy', 'sad', 'angry', 'anxious', 'neutral']
    if mood.lower() in valid_moods:
        return True
    return False

def format_mood_entry(mood_entry):
    return f"Mood: {mood_entry.mood_type}, Timestamp: {mood_entry.timestamp}"