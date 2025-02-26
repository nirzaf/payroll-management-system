from mongoengine import connect
from utils.config import get_database_url, get_database_name

def establish_connection():
    """
    Establishes connection to MongoDB using environment variables.
    """
    try:
        # Get database connection URL and name from environment
        db_url = get_database_url()
        db_name = get_database_name()
        
        # Connect to MongoDB
        connect(db=db_name, host=db_url)
        print(f"Successfully connected to MongoDB database: {db_name}")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise
