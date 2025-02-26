from mongoengine import connect
from utils.config import get_database_url

def establish_connection():
    """
    Establishes connection to MongoDB using environment variables.
    """
    try:
        # Get database connection URL from environment
        db_url = get_database_url()
        
        # Connect to MongoDB
        connect(host=db_url)
        print("Successfully connected to MongoDB")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise