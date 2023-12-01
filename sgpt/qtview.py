import viewmodel

from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QTextEdit,
    QLineEdit
)

def init(argv):
    global app
    app = QApplication(argv)

class View(QMainWindow):
    def __init__(self):
        super().__init__()

        self.enterhook = []
        self.reverthook = []
        self.retryhook = []
        self.textlog = ""

        self.setWindowTitle("SGPT")

        self.layout = QVBoxLayout()

        self.textbox = QTextEdit()
        self.textbox.setReadOnly(True)
        self.layout.addWidget(self.textbox)

        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText("질문을 입력하세요")
        self.lineedit.returnPressed.connect(self.enter)
        self.layout.addWidget(self.lineedit)

        self.buttonslayout = QHBoxLayout()

        self.revertbutton = QPushButton("지우기")
        self.revertbutton.clicked.connect(self.revert)
        self.buttonslayout.addWidget(self.revertbutton)

        self.retrybutton = QPushButton("재시도")
        self.retrybutton.clicked.connect(self.retry)
        self.buttonslayout.addWidget(self.retrybutton)

        self.buttons = QWidget()
        self.buttons.setLayout(self.buttonslayout)
        self.layout.addWidget(self.buttons)

        self.log_update_timer = QTimer()
        self.log_update_timer.setInterval(50)
        self.log_update_timer.timeout.connect(self.refresh_text)

    def exec(self):
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.show()
        self.log_update_timer.start()
        app.exec()

    def enter(self):
        text = self.lineedit.text()
        for f in self.enterhook:
            f(text)

    def revert(self):
        self.revertfunc()
        for f in self.reverthook:
            f()

    def retry(self):
        self.retryfunc()
        for f in self.retryhook:
            f()

    def get_entered(self):
        return self.lineedit.text()

    def set_text(self, txt):
        self.textlog = txt

    def refresh_text(self):
        self.textbox.setText(self.textlog)

