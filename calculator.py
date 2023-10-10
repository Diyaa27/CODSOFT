import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator by Sadia Javed")
        self.setGeometry(100, 100, 300, 400)

        self.init_ui()

    def init_ui(self):
        self.result_display = QLineEdit(self)
        self.result_display.setReadOnly(True)
        self.result_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.result_display.setStyleSheet("font-size: 20px;")

        layout = QVBoxLayout()
        button_grid = QGridLayout()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+', 'C'  # Added 'C' for clear
        ]

        row, col = 0, 0

        for button_text in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.button_click)
            button.setFixedSize(60, 60)
            button.setStyleSheet("font-size: 18px;")

            if button_text == '=':
                button.setStyleSheet("font-size: 18px; background-color: #f0a040;")  # Style '=' button
            elif button_text == 'C':
                button.setStyleSheet("font-size: 18px; background-color: #ff3030; color: white;")  # Style 'C' button

            button_grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addWidget(self.result_display)
        layout.addLayout(button_grid)
        self.setLayout(layout)
        self.show()

    def button_click(self):
        sender = self.sender()
        if sender.text() == '=':
            try:
                result = eval(self.result_display.text())
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")
        elif sender.text() == 'C':
            self.result_display.clear()
        else:
            current_text = self.result_display.text()
            new_text = current_text + sender.text()
            self.result_display.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    sys.exit(app.exec_())
