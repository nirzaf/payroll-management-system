from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
import os

class ThemeManager(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.is_dark_mode = True
        self.apply_theme()
    
    def setup_ui(self):
        # Create theme toggle button
        self.theme_button = QPushButton()
        self.theme_button.setFixedSize(32, 32)
        self.theme_button.setIconSize(self.theme_button.size())
        
        # Set the mode icon
        icon_path = os.path.join(os.path.dirname(__file__), '..', 'icons', 'mode.png')
        self.theme_button.setIcon(QIcon(icon_path))
        
        # Style the button
        self.theme_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                border-radius: 16px;
            }
            QPushButton:hover {
                background-color: rgba(52, 73, 94, 0.1);
            }
        """)
        
        self.theme_button.clicked.connect(self.toggle_theme)
    
    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()
    
    def apply_theme(self):
        if self.is_dark_mode:
            self.parent().setStyleSheet("""
                QMainWindow, QWidget {
                    background-color: #2c3e50;
                    color: white;
                }
                QPushButton {
                    background-color: #34495e;
                    color: white;
                    border: none;
                    padding: 8px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #3498db;
                }
                QLineEdit {
                    background-color: #34495e;
                    color: white;
                    border: 1px solid #3498db;
                    padding: 5px;
                    border-radius: 4px;
                }
            """)
        else:
            self.parent().setStyleSheet("""
                QMainWindow, QWidget {
                    background-color: #f5f6fa;
                    color: #2c3e50;
                }
                QPushButton {
                    background-color: #e8e8e8;
                    color: #2c3e50;
                    border: none;
                    padding: 8px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #3498db;
                    color: white;
                }
                QLineEdit {
                    background-color: white;
                    color: #2c3e50;
                    border: 1px solid #bdc3c7;
                    padding: 5px;
                    border-radius: 4px;
                }
            """)