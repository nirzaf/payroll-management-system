import os
from dotenv import load_dotenv

def load_environment():
    """
    Load environment variables from .env file
    """
    load_dotenv()

def get_database_url():
    """
    Get MongoDB connection URL from environment variables
    """
    # Use the direct connection string from .env file
    connection_string = os.getenv('mongodbconnectionstring')
    if not connection_string:
        # Fallback to localhost if connection string is not provided
        return "mongodb://localhost:27017/payroll_db"
    return connection_string

def get_database_name():
    """
    Get MongoDB database name from environment variables
    """
    return os.getenv('dbname', 'payrollms')

def get_jwt_secret():
    """
    Get JWT secret key from environment variables
    """
    return os.getenv('JWT_SECRET_KEY', 'your-secret-key-here')

def get_app_settings():
    """
    Get application settings from environment variables
    """
    return {
        'debug_mode': os.getenv('DEBUG_MODE', 'False').lower() == 'true',
        'log_level': os.getenv('LOG_LEVEL', 'INFO'),
        'session_timeout': int(os.getenv('SESSION_TIMEOUT', '3600'))
    }
