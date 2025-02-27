from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt, Signal

class SidebarWidget(QWidget):
    # Signals for navigation
    dashboard_clicked = Signal()
    employees_clicked = Signal()
    payroll_clicked = Signal()
    benefits_clicked = Signal()
    attendance_clicked = Signal()
    reports_clicked = Signal()
    settings_clicked = Signal()
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        # Set fixed width for sidebar
        self.setFixedWidth(200)
        self.setStyleSheet("background-color: #2c3e50; color: white;")
        
        # Create layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Add logo/title area
        title = QLabel("PMS")
        title.setStyleSheet("font-size: 24px; padding: 20px; background-color: #34495e;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Create navigation buttons
        self.add_nav_button("Dashboard", self.dashboard_clicked)
        self.add_nav_button("Employees", self.employees_clicked)
        self.add_nav_button("Payroll", self.payroll_clicked)
        self.add_nav_button("Benefits", self.benefits_clicked)
        self.add_nav_button("Attendance", self.attendance_clicked)
        self.add_nav_button("Reports", self.reports_clicked)
        self.add_nav_button("Settings", self.settings_clicked)
        
        # Add stretch to push buttons to top
        layout.addStretch()
    
    def add_nav_button(self, text, signal):
        button = QPushButton(text)
        button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                text-align: left;
                padding: 12px 20px;
                border: none;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
            QPushButton:pressed {
                background-color: #2980b9;
            }
        """)
        button.clicked.connect(signal)
        self.layout().addWidget(button)