from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QStackedWidget, QHBoxLayout
from PySide6.QtCore import Qt
from .components.login import LoginWidget
from .components.dashboard import DashboardWidget
from .components.sidebar import SidebarWidget
from .components.theme_manager import ThemeManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Payroll Management System")
        self.resize(1200, 800)
        
        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        # Create sidebar and theme manager
        sidebar_container = QWidget()
        sidebar_layout = QVBoxLayout(sidebar_container)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)
        
        self.sidebar = SidebarWidget()
        self.theme_manager = ThemeManager(self)
        
        sidebar_layout.addWidget(self.sidebar)
        sidebar_layout.addStretch(1)
        sidebar_layout.addWidget(self.theme_manager, 0, Qt.AlignCenter)
        
        # Add sidebar container to main layout
        self.layout.addWidget(sidebar_container)
        
        # Create content area
        content_container = QWidget()
        content_layout = QVBoxLayout(content_container)
        content_layout.setContentsMargins(0, 0, 0, 0)
        
        # Initialize stacked widget for different pages
        self.stacked_widget = QStackedWidget()
        
        # Create and add dashboard widget
        self.dashboard_widget = DashboardWidget()
        self.stacked_widget.addWidget(self.dashboard_widget)
        
        # Set dashboard as the main widget
        self.stacked_widget.setCurrentWidget(self.dashboard_widget)
        
        # Add stacked widget to layout
        self.layout.addWidget(self.stacked_widget)
    
    def show_dashboard(self):
        """Switch to dashboard view after successful login"""
        self.stacked_widget.setCurrentWidget(self.dashboard_widget)