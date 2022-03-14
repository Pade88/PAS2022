from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QMainWindow, QTextEdit, QPushButton, QMessageBox
from PyQt6 import QtCore
from Logger import LogFile
from AlertWindow import AlertMessage


class DeleteWindowBuilder(QMainWindow):
    def __init__(self, main_gui):
        super().__init__()
        self.main_gui = main_gui
        self.delete_widget = None
        LogFile.log_message("Fereastra de stergere a unui furnizor a fost initializata", "info")

    def init_delete_window_graphics(self):
        #AlertMessage.create_message_box("FAIL", "WIP")
        print("WIP, Not implemented!")
        # Work in progress
        """
        self.delete_widget = QWidget()
        layout = QGridLayout()
        layout.addWidget(QLabel("Delete NYI"))
        self.delete_widget.setLayout(layout)
        return self.delete_widget
        """