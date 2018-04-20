import sys, os, course_work_ui
import xml.etree.ElementTree as et
from PyQt5 import QtWidgets, QtGui


class Control(QtWidgets.QDialog):
    def __init__(self):
        super(Control, self).__init__()
        self.db_directory = ""
        self.ui = course_work_ui.Ui_Dialog()
        self.form = QtWidgets.QWidget()
        self.init_ui()

    def init_ui(self):
        self.ui.setupUi(self.form)
        self.form.show()
        self.main_screen()
        self.ui.open_xml.clicked.connect(self.open_xml)
        self.ui.create_database.clicked.connect(self.create_database)

    def main_screen(self):
        self.ui.add_row.hide()
        self.ui.open_xml.setEnabled(True)
        self.ui.create_database.setEnabled(True)
        self.ui.save_as.setEnabled(False)
        self.ui.close_database.setEnabled(False)
        self.ui.add_cols.hide()
        self.ui.new_table.hide()
        self.ui.add_table.hide()
        self.ui.edit_table.hide()
        self.ui.delete_row.hide()
        self.ui.change_row.hide()
        self.ui.exit_table.hide()
        self.ui.table_widget.hide()
        self.ui.delete_table.hide()
        self.ui.num_of_columns.hide()
        self.ui.delete_col_names.hide()

    def run(self):
        self.ui.save_as.clicked.connect(self.save_as)
        self.ui.add_row.clicked.connect(self.add_row)
        self.ui.add_cols.clicked.connect(self.add_cols)
        self.ui.add_table.clicked.connect(self.add_table)
        self.ui.new_table.clicked.connect(self.new_table)
        self.ui.change_row.clicked.connect(self.save_table)
        self.ui.delete_row.clicked.connect(self.delete_row)
        self.ui.edit_table.clicked.connect(self.edit_table)
        self.ui.exit_table.clicked.connect(self.tables_name)
        self.ui.delete_table.clicked.connect(self.delete_table)
        self.ui.table_widget.cellClicked.connect(self.cell_clicked)
        self.ui.close_database.clicked.connect(self.main_screen)
        self.ui.num_of_columns.clicked.connect(self.num_of_cols_inp)
        self.ui.delete_col_names.clicked.connect(self.delete_columns)

    def cell_clicked(self, row, column):
        item = self.ui.table_widget.item(row, column)
        if item is not None:
            self.choosed = item.text()
        self.choosed_row = row

    def read_xml(self):                                 #заново читает XML файл и обновляет переменные
        self.tree = et.parse(self.db_directory)
        self.tree_root = self.tree.getroot()
        self.tables = [x.tag for x in self.tree_root]

    def check_file(self):
        if os.stat(self.db_directory).st_size == 0:
            data = et.Element("data")
            """addresses = et.SubElement(data, "addresses")
            ambulances = et.SubElement(data, "ambulances")
            brigades = et.SubElement(data, "brigades")
            carriages = et.SubElement(data, "carriages")
            calls = et.SubElement(data, "calls")
            employees = et.SubElement(data, "employees")
            patients = et.SubElement(data, "patients")"""
            with open(self.db_directory, "wb") as wr:       #открытие файла для записи двоичных данных
                wr.write(et.tostring(data))
        self.read_xml()

    def open_xml(self):
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                             "Open...", "", "XML Files (*.xml)", options=options)
        if file_name:
            self.db_directory = file_name
            self.ui.open_xml.setEnabled(False)
            self.ui.create_database.setEnabled(False)
            self.check_file()
            self.tables_name()
            self.run()

    def save_as(self):
        self.read_xml()
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                             "Save as...", "", "XML Files (*.xml)", options=options)
        if file_name:
            with (open(file_name, "wb")) as wrb:
                wrb.write(et.tostring(self.tree_root))

    def create_database(self):
        self.db_directory = "dbmanager.xml"
        self.ui.open_xml.setEnabled(False)
        self.ui.create_database.setEnabled(False)
        rew = open(self.db_directory, "w")
        rew.close()
        self.check_file()
        self.tables_name()
        self.run()


#-------------------------------------TABLES---MANAGEMENT---START----------------------------------

    def tables_name(self):
        if len(self.tree_root) != 0:
            self.choosed = self.tree_root[0].tag       #меняет указатель на первое название таблицы
            self.ui.delete_table.show()
            self.ui.edit_table.show()
        else:
            self.ui.delete_table.hide()
            self.ui.edit_table.hide()
        self.ui.add_row.hide()
        self.ui.add_cols.hide()
        self.ui.new_table.show()
        self.ui.add_table.hide()
        self.ui.delete_row.hide()
        self.ui.change_row.hide()
        self.ui.exit_table.hide()
        self.ui.num_of_columns.hide()
        self.ui.delete_col_names.hide()
        self.ui.save_as.setEnabled(True)
        self.ui.close_database.setEnabled(True)
        self.ui.table_widget.show()
        self.ui.table_widget.setColumnCount(0)
        self.ui.table_widget.setColumnCount(1)
        self.ui.table_widget.setRowCount(0)
        self.ui.table_widget.setRowCount(len(self.tree_root))
        self.ui.table_widget.setHorizontalHeaderLabels(["Tables"])
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        (lambda t: [self.ui.table_widget.setItem(i, 0, QtWidgets.QTableWidgetItem(each))
                    for i, each in enumerate(t)])(self.tables)

    def edit_table(self):
        self.choosed_fixed = self.choosed
        self.show_table()

    def new_table(self):
        self.ui.add_table.show()
        self.ui.new_table.hide()
        self.ui.edit_table.hide()
        self.ui.delete_table.hide()
        self.ui.table_widget.setRowCount(0)
        self.ui.table_widget.setRowCount(1)
        self.ui.table_widget.setHorizontalHeaderLabels(["Enter the name of the new table."])

    def add_table(self):
        self.read_xml()
        if self.ui.table_widget.item(0, 0) is not None:
            item_txt = self.ui.table_widget.item(0, 0).text().lower()
            if item_txt.isdigit() is False and 2 <= len(item_txt) <= 35 and item_txt not in self.tables:
                n_t = et.SubElement(self.tree_root, item_txt)
                self.tree.write(self.db_directory)
                self.choosed_fixed = item_txt
                self.show_table()
            else:
                self.ui.table_widget.setRowCount(0)
                self.ui.table_widget.setRowCount(1)

    def save_table(self):
        main_inst = self.tree_root.find(self.choosed_fixed)
        table_items = list()
        for i in range(self.ui.table_widget.rowCount()-1):
            table_items.append(list())
            for j in range(self.ui.table_widget.columnCount()):
                cell_item = self.ui.table_widget.item(i,j)
                if cell_item is not None:
                    cell_item_text = cell_item.text()
                else:
                    cell_item_text = "-"
                table_items[i].append(cell_item_text)
        for i, each in enumerate(main_inst[1:]):
            for j, e in enumerate(each):
                e.text = table_items[i][j]
        self.tree.write(self.db_directory)
        self.show_table()

    def show_table(self):
        self.read_xml()                                             #читает XML файл заново
        self.choosed_row = 0                                        #указатель на первую строку в таблице
        if self.choosed_fixed in self.tables:
            main_inst = self.tree_root.find(self.choosed_fixed)       #получает элемент XML с названием таблицы
            self.ui.add_row.show()
            self.ui.new_table.hide()
            self.ui.add_table.hide()
            self.ui.exit_table.show()
            self.ui.edit_table.hide()
            self.ui.change_row.hide()
            self.ui.delete_row.hide()
            self.ui.delete_table.hide()
            self.ui.delete_col_names.hide()
            self.ui.table_widget.setRowCount(0)  #убирает все строки в таблице
            self.ui.table_widget.setColumnCount(0)  #убирает все колонки в таблице
            if len(main_inst) != 0:                      #если таблица пустая, то очищает таблицу на экране
                self.ui.change_row.show()
                self.ui.delete_row.show()
                self.ui.delete_col_names.show()
                self.ui.table_widget.setColumnCount(len(main_inst[0]))
                self.ui.table_widget.setRowCount(len(main_inst))
                self.ui.table_widget.setHorizontalHeaderLabels([x.text for x in main_inst[0]])
                (lambda t: [self.ui.table_widget.setItem(i, j, QtWidgets.QTableWidgetItem(e.text))
                 for i, each in enumerate(t) for j, e in enumerate(each)])(main_inst[1:])
                self.ui.table_widget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            else:
                
                self.ui.table_widget.setColumnCount(1)
                self.ui.table_widget.setHorizontalHeaderLabels([self.choosed_fixed])
                self.ui.table_widget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def delete_table(self):
        if len(self.tree_root) != 0:
            main_inst = self.tree_root.find(self.choosed)
            self.tree_root.remove(main_inst)
            self.tree.write(self.db_directory)
            self.tables_name()

#-------------------------------------TABLES---MANAGEMENT---END----------------------------------

    def add_row(self):
        main_inst = self.tree_root.find(self.choosed_fixed)
        if len(main_inst) == 0:
            self.number_of_columns()
            self.ui.add_row.hide()
            self.ui.change_row.hide()
            self.ui.delete_row.hide()
            self.ui.exit_table.hide()
            self.ui.num_of_columns.show()
            self.ui.delete_col_names.hide()
        else:
            row = et.SubElement(main_inst, "row{}".format(len(main_inst)))
            row_list = list()
            for each in range(self.ui.table_widget.columnCount()):
                item = self.ui.table_widget.item(self.ui.table_widget.rowCount()-1, each)
                row_list.append("-") if item is None or len(item.text()) == 0 else row_list.append(item.text())
            for i, each in enumerate(main_inst[0]):
                field = et.SubElement(row, "field")
                field.text = row_list[i]
            self.tree.write(self.db_directory)
            self.show_table()

    def number_of_columns(self):
        self.ui.table_widget.setColumnCount(0)          #очищается таблица на экране
        self.ui.table_widget.setColumnCount(1)          #создаётся одна колонка
        self.ui.table_widget.setRowCount(0)
        self.ui.table_widget.setRowCount(1)                 #создаётся одна строка для ввода количества полей
        self.ui.table_widget.setHorizontalHeaderLabels(
            ["Enter the number of columns(max.50). Press 'Enter' to complete the input."])
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)  #колонка
                                                                            # растягивается по всей ширине таблицы

    def num_of_cols_inp(self):
        item = self.ui.table_widget.item(0, 0)
        if item is not None:
            item = item.text()
            if item.isdigit() and 1 <= int(item) <= 50:
                self.ui.num_of_columns.hide()
                self.ui.add_cols.show()
                self.ui.table_widget.setColumnCount(0)
                self.ui.table_widget.setColumnCount(int(item))
                self.ui.table_widget.setRowCount(0)
                self.ui.table_widget.setRowCount(1)
                self.ui.table_widget.setHorizontalHeaderLabels(["field{}".format(str(x+1)) for x in range(int(item))])
            else:
                cl_item = QtWidgets.QTableWidgetItem()
                cl_item.setText("")
                self.ui.table_widget.setItem(0, 0, cl_item)

    def add_cols(self):
        main_inst = self.tree_root.find(self.choosed_fixed)
        cols_list = list()
        for each in range(self.ui.table_widget.columnCount()):
            item = self.ui.table_widget.item(0, each)
            if item is None or item.text().isdigit() or (len(item.text()) == 0 or len(item.text()) > 30):
                self.ui.table_widget.setRowCount(0)
                self.ui.table_widget.setRowCount(1)
                return False
            else:
                cols_list.append(item.text())
        columns = et.SubElement(main_inst, "columns")
        for i in range(len(cols_list)):
            column = et.SubElement(columns, "column")
            column.text = cols_list[i]
        self.tree.write(self.db_directory)
        self.ui.add_cols.hide()
        self.choosed = self.choosed_fixed       #меняется содержимое переменной на содержимое переменной
                                                #с названием выбранной таблицы
        self.show_table()

    def delete_row(self):
        if self.choosed_row+1 != self.ui.table_widget.rowCount():
            main_inst = self.tree_root.find(self.choosed_fixed)
            main_inst.remove(main_inst.find(main_inst[self.choosed_row+1].tag))
            if self.choosed_row != 0:                   #перемещает указатель на предпоследнюю строку в таблице
                self.choosed_row -= 1
            self.tree.write(self.db_directory)
            self.show_table()

    def delete_columns(self):
        main_inst = self.tree_root.find(self.choosed_fixed)
        main_inst.clear()
        self.tree.write(self.db_directory)
        self.show_table()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ctrl = Control()
    sys.exit(app.exec_())
