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
    db_host = os.getenv('MONGODB_HOST', 'localhost')
    db_port = os.getenv('MONGODB_PORT', '27017')
    db_name = os.getenv('MONGODB_NAME', 'payroll_db')
    db_user = os.getenv('MONGODB_USER')
    db_pass = os.getenv('MONGODB_PASSWORD')
    
    if db_user and db_pass:
        return f"mongodb://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    return f"mongodb://{db_host}:{db_port}/{db_name}"

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