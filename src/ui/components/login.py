from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import Signal
from database.models.user import User

class LoginWidget(QWidget):
    # Signal to emit when login is successful
    login_successful = Signal()
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("Payroll Management System")
        title.setStyleSheet("font-size: 24px; margin: 20px;")
        layout.addWidget(title)
        
        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setMinimumWidth(300)
        layout.addWidget(self.username_input)
        
        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)
        
        # Login button
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)
        login_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px;")
        layout.addWidget(login_button)
        
        # Error message label
        self.error_label = QLabel()
        self.error_label.setStyleSheet("color: red;")
        layout.addWidget(self.error_label)
        
        # Center all widgets
        layout.setAlignment(Qt.AlignCenter)
        
    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        try:
            # Authenticate user (implement actual authentication logic)
            user = User.authenticate(username, password)
            if user:
                self.error_label.clear()
                self.login_successful.emit()
            else:
                self.error_label.setText("Invalid username or password")
        except Exception as e:
            self.error_label.setText(str(e))