from workout_logger import db, create_app
from workout_logger.models import User  # Import all models here

if __name__ == '__main__':
    app = create_app()

    # Create the database tables (explicit creation of database)
    with app.app_context():
        db.create_all()

    app.run()
