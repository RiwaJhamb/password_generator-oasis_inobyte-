import sys
import random
import string
import pyperclip
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Password Generator")
        self.setGeometry(100, 100, 400, 250)
        
        # Create central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Create main layout
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        
        # Create input frame
        self.input_frame = QHBoxLayout()
        self.main_layout.addLayout(self.input_frame)
        
        # Create option frame
        self.option_frame = QHBoxLayout()
        self.main_layout.addLayout(self.option_frame)
        
        # Create generate frame
        self.generate_frame = QHBoxLayout()
        self.main_layout.addLayout(self.generate_frame)
        
        # Create input fields
        self.length_label = QLabel("Password Length:")
        self.input_frame.addWidget(self.length_label)
        
        self.length_entry = QLineEdit()
        self.input_frame.addWidget(self.length_entry)
        
        # Create option checkboxes
        self.use_uppercase = QCheckBox("Uppercase Letters")
        self.use_uppercase.setChecked(True)
        self.option_frame.addWidget(self.use_uppercase)
        
        self.use_lowercase = QCheckBox("Lowercase Letters")
        self.use_lowercase.setChecked(True)
        self.option_frame.addWidget(self.use_lowercase)
        
        self.use_numbers = QCheckBox("Numbers")
        self.use_numbers.setChecked(True)
        self.option_frame.addWidget(self.use_numbers)
        
        self.use_symbols = QCheckBox("Symbols")
        self.use_symbols.setChecked(True)
        self.option_frame.addWidget(self.use_symbols)
        
        # Create generate button
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)
        self.generate_frame.addWidget(self.generate_button)
        
        # Create copy button
        self.copy_button = QPushButton("Copy to Clipboard")
        self.copy_button.clicked.connect(self.copy_password)
        self.generate_frame.addWidget(self.copy_button)
        
        # Create password label
        self.password_label = QLabel("")
        self.generate_frame.addWidget(self.password_label)
        
    def generate_password(self):
        try:
            length = int(self.length_entry.text())
            if length < 8:
                QMessageBox.critical(self, "Error", "Password length must be at least 8 characters")
                return

            characters = ""
            if self.use_uppercase.isChecked():
                characters += string.ascii_uppercase
            if self.use_lowercase.isChecked():
                characters += string.ascii_lowercase
            if self.use_numbers.isChecked():
                characters += string.digits
            if self.use_symbols.isChecked():
                characters += string.punctuation

            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.setText(password)
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid input")
            
    def copy_password(self):
        password = self.password_label.text()
        if password:
            pyperclip.copy(password)
            QMessageBox.information(self, "Success", "Password copied to clipboard")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())

