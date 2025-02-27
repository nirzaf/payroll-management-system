import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from database.connection import establish_connection
from utils.config import load_environment
from database.sample_data import load_sample_data

def main():
    # Load environment variables
    load_environment()
    
    # Establish database connection
    establish_connection()
    
    # Load sample data if enabled in .env
    load_sample_data()
    
    # Initialize Qt application
    app = QApplication(sys.argv)
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Start application event loop
    sys.exit(app.exec())

if __name__ == '__main__':
    main()