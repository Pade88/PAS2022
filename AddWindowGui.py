# Built-In
from Logger import LogFile
from AlertWindow import AlertMessage

# HomeBrew-ed
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QMainWindow, QTextEdit, QPushButton, QMessageBox
from PyQt6 import QtCore


class AddWindowBuilder(QMainWindow):
    def __init__(self, main_gui):
        super().__init__()
        self.main_gui = main_gui
        self.supl_manager = self.main_gui.suppliers_manager
        self.comp_manager = self.main_gui.company_manager
        self.nume = self.TI = self.prod = self.addr = self.in_charge = self.phone = None
        self.te_edit_variables = [self.nume, self.TI, self.prod, self.addr, self.in_charge, self.phone]
        self.add_widget = self.delete_widget = None
        LogFile.log_message("Fereastra de adaugare a unui furnizor a fost initiata", "info")

    # Init buttons graphhic
    def init_add_window_graphics(self):
        self.add_widget = QWidget()
        layout = QGridLayout()

        labels_text = ["Nume", "CUI", "Lista de produse", "Adresa", "Administrator", "Telefon"]

        for pos_cnt, (label_text, te_var) in enumerate(zip(labels_text, self.te_edit_variables)):
            layout.addWidget(QLabel(label_text), pos_cnt, 0)
            te_var = QTextEdit()
            te_var.setMaximumSize(QtCore.QSize(200, 30))
            self.te_edit_variables[pos_cnt] = te_var
            layout.addWidget(te_var, pos_cnt, 1)

        layout.addWidget(self.create_done_button())
        layout.addWidget(self.create_close_button())
        self.add_widget.setLayout(layout)
        self.add_widget.setWindowTitle('Adaugă un furnizor')
        LogFile.log_message("Grafica ferestrei de adaugare a unui furnizor a fost initializata", "info")
        return self.add_widget

    def create_done_button(self):
        add_btn = QPushButton()
        add_btn.setText("Gata")
        add_btn.setMaximumSize(QtCore.QSize(100, 50))
        add_btn.clicked.connect(lambda: self.done_button_handler())
        LogFile.log_message(f"Butonul <<Done>> a fost creat cu succes! {locals()}", "info")
        return add_btn

    def create_close_button(self):
        close_btn = QPushButton()
        close_btn.setText("Înapoi")
        close_btn.setMaximumSize(QtCore.QSize(100, 50))
        close_btn.clicked.connect(lambda: self.close_button_handler())
        LogFile.log_message(f"Butonul <<Close>> a fost creat cu succes! {locals()}", "info")
        return close_btn

    def done_button_handler(self):
        arg_list = [qte_item.toPlainText() for qte_item in self.te_edit_variables if len(qte_item.toPlainText()) > 0]
        if len(arg_list) == len(self.te_edit_variables):
            self.comp_manager.add_new_supplier(self.main_gui.get_current_company(), arg_list[0])
            self.supl_manager.add_new_supplier(*arg_list)

            [qte_item.clear() for qte_item in self.te_edit_variables]
            AlertMessage.create_message_box("SUCCES", "Datele au fost inregistrate!")
            LogFile.log_message(f"Furnizorul {arg_list} a fost adaugat cu succes!", "info")
            self.add_widget.close()
        else:
            AlertMessage.create_message_box("FAIL", "Completeaza toate campurile!")
            LogFile.log_message("Butonul a fost apasat dar nu toate campurile au fost completate", "error")

    def close_button_handler(self):
        self.add_widget.close()
