from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QStackedWidget
from PySide6.QtCore import Qt
from .components.login import LoginWidget
from .components.dashboard import DashboardWidget
from .components.sidebar import SidebarWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Payroll Management System")
        self.resize(1200, 800)
        
        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        # Initialize stacked widget for different pages
        self.stacked_widget = QStackedWidget()
        
        # Create and add widgets
        self.login_widget = LoginWidget()
        self.dashboard_widget = DashboardWidget()
        
        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.dashboard_widget)
        
        # Set initial widget to login
        self.stacked_widget.setCurrentWidget(self.login_widget)
        
        # Add stacked widget to layout
        self.layout.addWidget(self.stacked_widget)
        
        # Connect signals
        self.login_widget.login_successful.connect(self.show_dashboard)
    
    def show_dashboard(self):
        """Switch to dashboard view after successful login"""
        self.stacked_widget.setCurrentWidget(self.dashboard_widget)