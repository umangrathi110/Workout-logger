# Workout Logger 

Workout Logger is a web application that allows users to manage their workouts(pushups). Users can perform the CRUD operations(create, read, update and delete their workouts) by signing up and logging in.

### Project Video 
[Watch the video here](https://www.loom.com/share/5101b29af3c845288ddabf2e92f6a938?sid=c3354ac7-c842-47f6-9b0c-662f5ee2d90d)


## Features

- User Authentication: Sign up and log in.
- Workout Management: Add, update, delete, and view workouts.
- Data Persistence: Workouts are stored in an SQLite database.

## Technologies Used

- Backend: Flask
- Database: SQLite
- Frontend: HTML, CSS

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/workout-logger.git
   cd workout-logger
   ```

2. **Create and activate the virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the dependencies**
   ```bash
   pip install -r requirents.txt
   ```
4. **Run the application**
   ```bash
   flask --app app run
   ```
