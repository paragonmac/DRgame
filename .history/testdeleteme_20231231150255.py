from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QLabel
from PyQt5.QtCore import pyqtSignal

class SenderWidget(QWidget):
    # Define a signal that will carry a string
    textEntered = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.lineEdit = QLineEdit()
        self.lineEdit.returnPressed.connect(self.onReturnPressed)
        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)

    def onReturnPressed(self):
        # Emit the signal when enter is pressed
        self.textEntered.emit(self.lineEdit.text())

class ReceiverWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Waiting for input...")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def updateLabel(self, text):
        # Update the label when the slot receives the signal
        self.label.setText(text)

if __name__ == "__main__":
    app = QApplication([])
    sender = SenderWidget()
    receiver = ReceiverWidget()

    # Connect the sender's signal to the receiver's slot
    sender.textEntered.connect(receiver.updateLabel)

    sender.show()
    receiver.show()
    app.exec_()
