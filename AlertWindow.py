from PyQt6.QtWidgets import QMainWindow,QMessageBox
from Logger import LogFile


class AlertMessage(QMainWindow):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_message_box(status, text):
        msg = QMessageBox()

        msg.setText(text)
        if status == "FAIL":
            msg.setWindowTitle("Eroare")
            msg.setIcon(QMessageBox.Icon["Critical"])
            msg.setStandardButtons(QMessageBox.StandardButton["Retry"])
        elif status == "SUCCES":
            msg.setIcon(QMessageBox.Icon["Information"])
            msg.setWindowTitle("Succes")
            msg.setStandardButtons(QMessageBox.StandardButton["Ok"])
        msg.exec()
        LogFile.log_message(f"Alert toast created with status {status} and {text}", "info")