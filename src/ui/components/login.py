from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import Qt, Signal

class LoginWidget(QWidget):
    login_successful = Signal()

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Title
        title = QLabel("Login")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; margin-bottom: 20px;")

        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setMinimumWidth(200)

        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumWidth(200)

        # Login button
        login_button = QPushButton("Login")
        login_button.setMinimumWidth(200)
        login_button.clicked.connect(self.handle_login)

        # Add widgets to layout
        layout.addWidget(title)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def handle_login(self):
        # TODO: Implement actual authentication logic
        username = self.username_input.text()
        password = self.password_input.text()
        
        # For now, just emit success signal
        if username and password:
            self.login_successful.emit()