# Built-In
import sys

# HomeBrew-ed
from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QPushButton,
    QLabel,
    QGridLayout,
    QComboBox,
    QTextEdit,
    QMainWindow)
from PyQt6 import QtCore

# PMSIC build
from AddWindowGui import AddWindowBuilder
from TableWindowGUI import TableWindowBuilder
from SearchWindowGUI import SearchWindowBuilder
from DeleteWindowGUI import DeleteWindowBuilder
from Logger import LogFile

COLUMN_SIZE = 3

SUPPLIERS_DB_FILE = "suppliers_db.json"
COMPANIES_DB_FILE = "companies_db.json"


class GUIBuilder(QMainWindow):
    def __init__(self, company_manager, supplier_manager, products_manager):
        self.company_manager = company_manager
        self.suppliers_manager = supplier_manager
        self.products_manager = products_manager
        self.suppliers = supplier_manager.get_suppliers()
        self.suppliers_names = supplier_manager.get_suppliers_names()
        self.companies = company_manager.get_company()
        self.companies_names = company_manager.get_companies_names()
        self.main_widget = None
        self.add_widget = None
        self.remove_widget = None
        self.table_view_widget = None
        self.companies_combo_items = None
        self.suppliers_combo_items = None
        self.list_item = None
        self.text_edit = None
        self.sort_selector = None
        self.app = QApplication(sys.argv)
        super().__init__()
        self.init_graphics()
        LogFile.log_message("Interfata grafica a fost initializata cu succes!", "info")
        self.app.exec()
        LogFile.log_message("Aplicatia ruleaza", "info")

    def init_graphics(self):
        self.main_widget = QWidget()
        layout = QGridLayout()
        layout.addWidget(QLabel("Lista de companii:"), 0, 0, 1, COLUMN_SIZE)
        layout.addWidget(self.create_company_combo_view(self.companies_names), 1, 0, 1, COLUMN_SIZE)

        layout.addWidget(QLabel("Lista de furnizori:"), 2, 0, 1, COLUMN_SIZE)
        layout.addWidget(self.create_suppliers_combo_view(self.suppliers_names), 3, 0, 1, COLUMN_SIZE)

        layout.addWidget(QLabel("Sortare:"), 4, 0)
        layout.addWidget(self.create_sort_combo_box(), 4, 1)

        layout.addWidget(self.create_text_edit(), 5, 0, 1, COLUMN_SIZE)
        layout.addWidget(self.create_table_view(), 6, 0, 1, COLUMN_SIZE)

        layout.addWidget(self.add_suppliers_button(), 7, 0)
        layout.addWidget(self.search_suppliers_button(), 7, 1)
        layout.addWidget(self.delete_suppliers_button(), 7, 2)
        layout.addWidget(self.create_exit_button(), 8, 0, 1, COLUMN_SIZE)
        self.main_widget.setLayout(layout)
        self.main_widget.setWindowTitle('PMSIC')
        self.main_widget.setMinimumSize(QtCore.QSize(500, 350))
        self.main_widget.show()

    def create_company_combo_view(self, items_list):
        self.companies_combo_items = QComboBox()
        [self.companies_combo_items.addItem(item) for item in items_list]
        self.companies_combo_items.activated.connect(lambda: self.update_suppliers_combo_box(
            self.company_manager.get_company_suppliers(self.companies_combo_items.currentText())))
        self.companies_combo_items.currentText()
        return self.companies_combo_items

    def create_suppliers_combo_view(self, items_list):
        self.suppliers_combo_items = QComboBox()
        [self.suppliers_combo_items.addItem(item) for item in items_list]
        self.suppliers_combo_items.activated.connect(lambda: self.set_text_edit(
            self.suppliers[self.suppliers_combo_items.currentIndex()]))
        return self.suppliers_combo_items

    def update_suppliers_combo_box(self, new_items):
        self.suppliers = self.suppliers_manager.get_suppliers_update(new_items)
        self.suppliers_combo_items.clear()
        [self.suppliers_combo_items.addItem(item) for item in new_items]
        self.suppliers_combo_items.update()

    def create_text_edit(self):
        self.text_edit = QTextEdit()
        return self.text_edit

    def set_text_edit(self, text):
        self.text_edit.setText(str(text))

    # Buttons
    def add_suppliers_button(self):
        btn = QPushButton()
        btn.setText("Adauga")
        btn.setMaximumSize(QtCore.QSize(100, 50))
        btn.clicked.connect(lambda: self.add_suppliers_pressed_handler())
        return btn

    def search_suppliers_button(self):
        btn = QPushButton()
        btn.setText("Caută")
        btn.setMaximumSize(QtCore.QSize(100, 50))
        btn.clicked.connect(lambda: self.search_suppliers_pressed_handler())
        return btn

    def delete_suppliers_button(self):
        btn = QPushButton()
        btn.setText("Șterge")
        btn.setMaximumSize(QtCore.QSize(100, 50))
        btn.clicked.connect(lambda: self.delete_suppliers_pressed_handler())
        return btn

    def create_table_view(self):
        btn = QPushButton()
        btn.setText("Vezi lista de produse")
        btn.clicked.connect(lambda: self.create_table_view_pressed_handler())
        return btn

    # ButtonHandler
    def add_suppliers_pressed_handler(self):
        LogFile.log_message("Butonul de adaugare a furnizorilor a fost apasat", "info")
        self.add_widget = AddWindowBuilder(self).init_add_window_graphics()
        self.add_widget.show()

    def search_suppliers_pressed_handler(self):
        LogFile.log_message("Butonul de cautare a furnizorilor a fost apasat", "info")
        self.add_widget = SearchWindowBuilder(self, self.suppliers_manager).init_search_window_graphics()
        self.add_widget.show()

    def delete_suppliers_pressed_handler(self):
        LogFile.log_message("Butonul de stergere a furnizorilor a fost apasat", "info")
        self.remove_widget = DeleteWindowBuilder(self).init_delete_window_graphics()
        self.remove_widget.show()

    def create_table_view_pressed_handler(self):
        LogFile.log_message("Butonul de vizualizare a produselor a fost apasat", "info")
        table_data = self.products_manager.get_products(self.get_current_supplier().strip())
        self.table_view_widget = TableWindowBuilder(self).init_table_view_graphics(table_data)
        self.table_view_widget.show()

    def get_current_company(self):
        return self.companies_combo_items.currentText()

    def get_current_supplier(self):
        return self.suppliers_combo_items.currentText()

    def create_sort_combo_box(self):
        sort_options = ["Nesortat", "A-Z", "Z-A"]
        self.sort_selector = QComboBox()
        [self.sort_selector.addItem(item) for item in sort_options]
        self.sort_selector.activated.connect(lambda: self.sort_selector_handler())

        return self.sort_selector

    def sort_selector_handler(self):
        if self.sort_selector.currentText() == "Nesortat":
            pass
        elif self.sort_selector.currentText() == "A-Z":
            self.suppliers_combo_items.model().sort(0, QtCore.Qt.SortOrder.AscendingOrder)
        else:
            self.suppliers_combo_items.model().sort(0, QtCore.Qt.SortOrder.DescendingOrder)

    def create_exit_button(self):
        btn = QPushButton()
        btn.setText("Ieșire")
        btn.clicked.connect(lambda: self.exit_button_pressed_handler())
        return btn

    def exit_button_pressed_handler(self):
        self.app.quit()
