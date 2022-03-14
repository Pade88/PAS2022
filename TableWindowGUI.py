# Home-Brew
from PyQt6.QtWidgets import QTableView, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QTextEdit, QHeaderView
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
# PMSIC
from Logger import LogFile
from AlertWindow import AlertMessage
from IOManager import IOManager
from Product import Product


class TableWindowBuilder(QMainWindow):
    def __init__(self, main_gui):
        self.main_gui = main_gui
        self.table_widget = None
        self.add_product_window = None
        self.data_model = None
        super().__init__()

    def init_table_view_graphics(self, data):
        self.table_widget = QWidget()
        layout = QGridLayout()

        table = QTableView()
        self.data_model = TableModel(data, self.main_gui)
        table.setModel(self.data_model)
        table.setMinimumSize(QtCore.QSize(350, 250))
        table.setAlternatingRowColors(True)
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

        table.clicked.connect(lambda: self.on_item_click(table))

        layout.addWidget(table)
        layout.addWidget(self.create_add_button())
        layout.addWidget(self.create_delete_button())
        layout.addWidget(self.create_close_button())

        self.table_widget.setLayout(layout)
        self.table_widget.setWindowTitle("Tabel cu produse")
        LogFile.log_message("Table view graphics initialized successfully!", "info")
        return self.table_widget

    def create_close_button(self):
        LogFile.log_message(f"Butonul de inapoi fost apasat {locals()}", "debug")
        close_btn = QPushButton()
        close_btn.setText("Înapoi")
        close_btn.setMaximumSize(QtCore.QSize(350, 50))
        close_btn.clicked.connect(lambda: self.close_button_handler())
        return close_btn

    def create_add_button(self):
        LogFile.log_message(f"Butonul de adaugare a unui produs a fost apasat {locals()}", "debug")
        add_btn = QPushButton()
        add_btn.setText("Adaugă produs")
        add_btn.setMaximumSize(QtCore.QSize(350, 50))
        add_btn.clicked.connect(lambda: self.add_button_handler())
        return add_btn

    def create_delete_button(self):
        LogFile.log_message(f"Butonul de stergere a unui produs a fost apasat {locals()}", "debug")
        del_btn = QPushButton()
        del_btn.setText("Șterge produs")
        del_btn.setMaximumSize(QtCore.QSize(350, 50))
        del_btn.clicked.connect(lambda: self.delete_button_handler())
        return del_btn

    def close_button_handler(self):
        self.table_widget.close()

    def add_button_handler(self):
        self.add_product_window = ProductAddWindowBuilder(self.main_gui, self).init_APW_add_product_graphic()
        self.add_product_window.show()

    def delete_button_handler(self):
        print("WIP, Not implemented!")

    def on_item_click(self, table):
        for index in table.selectedIndexes():
            print(index.column() + 1, index.row() + 1)

    def update_data_model(self):
        self.data_model.insertRows(0, 0, 0)


class ProductAddWindowBuilder(QMainWindow):
    def __init__(self, main_gui, second_gui):
        self.main_gui = main_gui
        self.second_gui = second_gui
        self.add_product_widget = None
        self.nume = self.pret = self.quantity = None
        self.input_data = [self.nume, self.pret, self.quantity]
        super().__init__()

    def init_APW_add_product_graphic(self):
        self.add_product_widget = QWidget()
        layout = QGridLayout()

        labels = ["Nume produs", "Pret produs", "Cantitate Produs"]
        for layout_row_cnt, (te_label, te_point) in enumerate(zip(labels, self.input_data)):
            layout.addWidget(QLabel(te_label), layout_row_cnt, 0)

            te_var = QTextEdit()
            te_var.setMaximumSize(QtCore.QSize(200, 30))
            self.input_data[layout_row_cnt] = te_var
            layout.addWidget(te_var, layout_row_cnt, 1)

        layout.addWidget(self.create_APW_add_button(), layout_row_cnt + 1, 0, 1, 2)
        layout.addWidget(self.create_APW_close_button(), layout_row_cnt + 2, 0, 1, 2)

        self.add_product_widget.setWindowTitle("Adaugă un produs")
        self.add_product_widget.setLayout(layout)
        return self.add_product_widget

    def create_APW_add_button(self):
        add_btn = QPushButton()
        add_btn.setText("Adaugă")
        add_btn.setMaximumSize(QtCore.QSize(350, 50))
        add_btn.clicked.connect(lambda: self.add_APW_button_handler())
        return add_btn

    def create_APW_close_button(self):
        close_btn = QPushButton()
        close_btn.setText("Înapoi")
        close_btn.setMaximumSize(QtCore.QSize(350, 50))
        close_btn.clicked.connect(lambda: self.close_APW_button_handler())
        return close_btn

    def add_APW_button_handler(self):
        product_owner = self.main_gui.get_current_supplier()
        product_name, product_price, product_quantity = [decode.toPlainText() for decode in self.input_data]
        try:
            if isinstance(int(product_price), int) and isinstance(int(product_quantity), int):
                self.main_gui.products_manager.add_product(Product(product_owner, product_name,
                                                                   product_price, product_quantity))
                AlertMessage.create_message_box("SUCCES", "Produsul a fost adaugat!")
                self.add_product_widget.close()
                self.second_gui.update_data_model()
        except ValueError:
            AlertMessage.create_message_box("FAIL", "Datele produsului nu corespund!")


    def close_APW_button_handler(self):
        self.add_product_widget.close()


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, main_gui):
        super(TableModel, self).__init__()
        self._data = data
        self.main_gui = main_gui

    def data(self, index, role):
        output_list = [[product.name.strip(), product.price.strip(), product.quantity.strip()]
                       for product in self.main_gui.products_manager.get_products(self.main_gui.get_current_supplier())]

        if role == Qt.ItemDataRole.DisplayRole:
            return output_list[index.row()][index.column()]
        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return 3

    def insertRows(self, position, rows, item, parent=QtCore.QModelIndex()):
        self.beginInsertRows(QtCore.QModelIndex(), len(self._data), len(self._data) + 1)
        self._data.append(item)
        self.endInsertRows()
        return True

    def headerData(self, section, orientation, role):
        headers = ["Nume produs", "Pret produs", "Cantitate disponibila"]
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QtCore.QVariant()
        return headers[section]

