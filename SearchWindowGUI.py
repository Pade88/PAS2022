from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QMainWindow, QTextEdit, QPushButton
from PyQt6 import QtCore
from Logger import LogFile


class SearchWindowBuilder(QMainWindow):
    def __init__(self, main_gui, suppliers_manager):
        super().__init__()
        self.main_gui = main_gui
        self.suppliers_manager = suppliers_manager
        self.search_widget = self.tax_identification_text_edit = self.search_button = self.output_text_view = None
        self.close_button = None
        LogFile.log_message("Fereastra de cautare a unui furnizor a fost initiata", "info")

    def init_search_window_graphics(self):
        self.search_widget = QWidget()
        layout = QGridLayout()

        layout.addWidget(QLabel("CUI:"))
        layout.addWidget(self.create_search_text_input())
        layout.addWidget(self.create_output_text_view())
        layout.addWidget(self.create_search_button())
        layout.addWidget(self.create_close_button())

        self.search_widget.setMinimumSize(QtCore.QSize(300, 250))
        self.search_widget.setLayout(layout)
        self.search_widget.setWindowTitle("Caută un furnizor")
        LogFile.log_message("Grafica ferestrei de cautare a unui furnizor a fost initializata!", "info")
        return self.search_widget

    def create_output_text_view(self):
        self.output_text_view = QTextEdit()
        self.output_text_view.setText("Introduceti codul de identificare a unui furnizor")
        self.output_text_view.setMinimumSize((QtCore.QSize(300, 100)))
        return self.output_text_view

    def create_search_text_input(self):
        self.tax_identification_text_edit = QTextEdit()
        self.tax_identification_text_edit.setMaximumSize(QtCore.QSize(300, 30))
        LogFile.log_message(f"Search text input created! {locals()}", "debug")
        return self.tax_identification_text_edit

    def create_search_button(self):
        self.search_button = QPushButton()
        self.search_button.setText("Caută")
        self.search_button.setMaximumSize(QtCore.QSize(300, 50))
        self.search_button.clicked.connect(lambda: self.search_button_pressed_handler())
        LogFile.log_message(f"Search button created! {locals()}", "debug")
        return self.search_button

    def create_close_button(self):
        self.close_button = QPushButton()
        self.close_button.setText("Înapoi")
        self.close_button.setMaximumSize(QtCore.QSize(300, 50))
        self.close_button.clicked.connect(lambda: self.close_button_pressed_handler())
        LogFile.log_message(f"Close button created! {locals()}", "debug")
        return self.close_button

    def search_button_pressed_handler(self):
        tax_identif = self.tax_identification_text_edit.toPlainText()
        LogFile.log_message(f"Se cauta furnizorul de CUI-ul {tax_identif}", "info")
        if len(tax_identif) != 9:
            self.output_text_view.setText("Dimensiunea CUI-ului trebuie sa fie de 9 cifre!")
            LogFile.log_message("Dimensiunea CUI-ului nu este de 9 cifre", "error")
        else:
            result = self.suppliers_manager.search_supplier_by_tax(tax_identif)
            if isinstance(result, str):
                self.output_text_view.setText(result)
                LogFile.log_message(f"Furnizorul a fost gasit, rezultatul: {result}", "info")
            else:
                self.output_text_view.setText(f'Furnizorul cu CUI-ul {tax_identif} nu a fost gasit!')
                LogFile.log_message(f"Nici un furnizor din baza de date nu are acest CUI!", "error")

    def close_button_pressed_handler(self):
        self.search_widget.close()
