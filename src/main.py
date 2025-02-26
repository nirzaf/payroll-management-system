import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from database.connection import establish_connection
from utils.config import load_environment

def main():
    # Load environment variables
    load_environment()
    
    # Establish database connection
    establish_connection()
    
    # Initialize Qt application
    app = QApplication(sys.argv)
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Start application event loop
    sys.exit(app.exec())

if __name__ == '__main__':
    main()