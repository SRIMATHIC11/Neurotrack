# NeuroTrack Mood & Mental Health Tracker

## Overview
NeuroTrack is a console-based application designed to help users track their mood and mental health over time. The application allows users to log their moods, view their mood history, and gain insights into their mental well-being.

## Features
- User registration and management
- Mood entry logging with timestamps
- Display of mood history
- Simple and intuitive console interface

## OOP Concepts Demonstrated
This project showcases several Object-Oriented Programming (OOP) concepts:

1. **Encapsulation**: User information and mood entries are encapsulated within their respective classes, ensuring that data is managed and accessed through defined methods.

2. **Abstraction**: Interfaces are used to define the essential methods for mood tracking operations, allowing for a clear separation between the implementation and the user of the classes.

3. **Inheritance**: The `Tracker` class inherits from the `MoodEntry` class, allowing it to extend functionality and manage multiple mood entries.

4. **Polymorphism**: Method overriding is demonstrated in the `Tracker` class, where it provides specific implementations for adding and displaying mood entries.

5. **Multiple Inheritance**: The project structure allows for potential multiple inheritance scenarios, particularly in the interfaces, where different tracking functionalities can be combined.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd neurotrack-mood-tracker
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python src/main.py
   ```

## Usage Examples
- Register a new user
- Log a mood entry
- View mood history

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.