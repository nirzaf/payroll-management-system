from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtCore import Qt
from .sidebar import SidebarWidget

class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        # Create main layout
        layout = QHBoxLayout(self)
        
        # Add sidebar
        self.sidebar = SidebarWidget()
        layout.addWidget(self.sidebar)
        
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
        
        # Set layout stretch factors
        layout.setStretch(0, 1)  # Sidebar takes 1 part
        layout.setStretch(1, 4)  # Content takes 4 parts
        
        # Set layout margins and spacing
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)