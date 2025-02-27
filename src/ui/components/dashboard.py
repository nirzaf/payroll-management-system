from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtCore import Qt

class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        # Create main layout
        layout = QVBoxLayout(self)
        
        # Create content area
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        
        # Add welcome message
        welcome_label = QLabel("Welcome to Payroll Management System")
        welcome_label.setStyleSheet("font-size: 24px; margin: 20px;")
        welcome_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(welcome_label)
        
        # Add content widget to main layout
        layout.addWidget(content_widget)
        
        # Set layout margins and spacing
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)