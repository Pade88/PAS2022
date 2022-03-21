from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel,
    QMainWindow,
    QComboBox,
    QPushButton
)

from Logger import LogFile
from AlertWindow import AlertMessage

COMPANY_QCBX_PLACEHOLDER = "Selecteaza o companie!"
SUPPLIERS_QCBX_PLACEHOLDER = "Selecteaza un furnizor!"


class DeleteWindowBuilder(QMainWindow):
    def __init__(self, main_gui):
        super().__init__()
        self.main_gui = main_gui
        self.supl_manager = self.main_gui.suppliers_manager
        self.comp_manager = self.main_gui.company_manager

        self.companies_names = self.comp_manager.get_companies_names()
        self.supliers_names = self.supl_manager.get_suppliers_names()

        self.delete_widget = None
        self.remove_supplier = None
        self.remove_company = None
        LogFile.log_message("Fereastra de stergere a unui furnizor a fost initializata", "info")

    def init_delete_window_graphics(self):
        self.delete_widget = QWidget()
        layout = QGridLayout()

        # Labels
        layout.addWidget(QLabel("Sterge o companie"), 0, 0, 1, 2)
        layout.addWidget(QLabel("Sterge un furnizor"), 2, 0, 1, 2)
        # QCB
        layout.addWidget(self.remove_company_combo_view(self.companies_names), 1, 0, 1, 2)
        layout.addWidget(self.remove_supplier_combo_view(self.supliers_names), 3, 0, 1, 2)
        # QBTN
        layout.addWidget(self.back_button(), 4, 0)
        layout.addWidget(self.delete_button(), 4, 1)



        self.delete_widget.setLayout(layout)
        self.delete_widget.setWindowTitle('Șterge un furnizor')
        return self.delete_widget

    # QCB
    def remove_company_combo_view(self, companies_list):
        self.remove_company = QComboBox()
        self.remove_company.addItem(COMPANY_QCBX_PLACEHOLDER)
        [self.remove_company.addItem(item) for item in companies_list]
        self.remove_company.activated.connect(lambda: self.remove_company_combo_view_pressed_handler())
        return self.remove_company

    def remove_supplier_combo_view(self, suppliers_list):
        self.remove_supplier = QComboBox()
        self.remove_supplier.addItem(SUPPLIERS_QCBX_PLACEHOLDER)
        [self.remove_supplier.addItem(item) for item in suppliers_list]
        self.remove_supplier.activated.connect(lambda: self.remove_supplier_combo_view_pressed_handler())
        return self.remove_supplier

    # QCBHDL
    def remove_company_combo_view_pressed_handler(self):
        place_holder_id = self.remove_company.findText(COMPANY_QCBX_PLACEHOLDER)
        self.remove_company.removeItem(place_holder_id)
        # Cross selection, if a item is selected in other qcombo, reset this one
        # If reset is not possible (default placeholder item was removed)
        # Create a new placeholder and try to reset again
        cross_placeholder = self.remove_supplier.findText(SUPPLIERS_QCBX_PLACEHOLDER)
        if cross_placeholder > 0:
            self.remove_supplier.setCurrentIndex(cross_placeholder)
        else:
            self.remove_supplier.addItem(SUPPLIERS_QCBX_PLACEHOLDER)
            cross_placeholder = self.remove_supplier.findText(SUPPLIERS_QCBX_PLACEHOLDER)
            self.remove_supplier.setCurrentIndex(cross_placeholder)

    def remove_supplier_combo_view_pressed_handler(self):
        place_holder_id = self.remove_supplier.findText(SUPPLIERS_QCBX_PLACEHOLDER)
        self.remove_supplier.removeItem(place_holder_id)
        # Cross selection, same as above
        cross_placeholder = self.remove_company.findText(COMPANY_QCBX_PLACEHOLDER)
        if cross_placeholder > 0:
            self.remove_company.setCurrentIndex(cross_placeholder)
        else:
            self.remove_company.addItem(COMPANY_QCBX_PLACEHOLDER)
            cross_placeholder = self.remove_company.findText(COMPANY_QCBX_PLACEHOLDER)
            self.remove_company.setCurrentIndex(cross_placeholder)

    # QBTN

    def delete_button(self):
        btn = QPushButton()
        btn.setText("Sterge")
        btn.clicked.connect(lambda: self.delete_button_pressed_handler())
        return btn

    def back_button(self):
        btn = QPushButton()
        btn.setText("Inapoi")
        btn.clicked.connect(lambda: self.back_button_pressed_handler())
        return btn

    # QBTNHDL

    def delete_button_pressed_handler(self):
        selected_company = self.remove_company.currentText()
        selected_supplier = self.remove_supplier.currentText()

        if selected_company != COMPANY_QCBX_PLACEHOLDER:
            del_status = self.comp_manager.remove_company(selected_company)
        else:
            del_status = self.supl_manager.remove_supplier(selected_supplier)

        if del_status and selected_company != COMPANY_QCBX_PLACEHOLDER:
            AlertMessage.create_message_box("SUCCES", f"{selected_company} removed successfully!")
            self.delete_widget.close()
        elif del_status and selected_supplier != SUPPLIERS_QCBX_PLACEHOLDER:
            AlertMessage.create_message_box("SUCCES", f"{selected_supplier} removed successfully!")
            self.delete_widget.close()
        else:
            AlertMessage.create_message_box("FAIL", "Something went wrong!")

    def back_button_pressed_handler(self):
        self.delete_widget.close()