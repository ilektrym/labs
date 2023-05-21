import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                         QTableWidgetItem, QPushButton, QMessageBox)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("WEEK_1")
        self.setWindowTitle("WEEK_2")
        self.setWindowTitle("Subject")
        self.setWindowTitle("Teacher")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_shedule_tab()
        self._create_shedule2_tab()
        self._create_shedule3_tab()
        self._create_shedule4_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="BOT",
                                     user="postgres",
                                     password="12DImA567",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def _create_shedule_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "WEEK_1")

        self.monday_gbox = QGroupBox("Monday")
        self.tuesday_gbox = QGroupBox("Tuesday")
        self.wednesday_gbox = QGroupBox("Wednesday")
        self.thursday_gbox = QGroupBox("Thursday")
        self.friday_gbox = QGroupBox("Friday")
        self.saturday_gbox = QGroupBox("Saturday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)

        self.shbox1.addWidget(self.monday_gbox)
        self.shbox1.addWidget(self.tuesday_gbox)
        self.shbox1.addWidget(self.wednesday_gbox)
        self.shbox2.addWidget(self.thursday_gbox)
        self.shbox2.addWidget(self.friday_gbox)
        self.shbox2.addWidget(self.saturday_gbox)

        self._create_monday_table()
        self._create_tuesday_table()
        self._create_wednesday_table()
        self._create_thursday_table()
        self._create_friday_table()
        self._create_saturday_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox3.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule_tab.setLayout(self.svbox)

    def _create_shedule2_tab(self):
        self.shedule2_tab = QWidget()
        self.tabs.addTab(self.shedule2_tab, "WEEK_2")

        self.monday2_gbox = QGroupBox("Monday")
        self.tuesday2_gbox = QGroupBox("Tuesday")
        self.wednesday2_gbox = QGroupBox("Wednesday")
        self.thursday2_gbox = QGroupBox("Thursday")
        self.friday2_gbox = QGroupBox("Friday")
        self.saturday2_gbox = QGroupBox("Saturday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)

        self.shbox1.addWidget(self.monday2_gbox)
        self.shbox1.addWidget(self.tuesday2_gbox)
        self.shbox1.addWidget(self.wednesday2_gbox)
        self.shbox2.addWidget(self.thursday2_gbox)
        self.shbox2.addWidget(self.friday2_gbox)
        self.shbox2.addWidget(self.saturday2_gbox)

        self._create_monday2_table()
        self._create_tuesday2_table()
        self._create_wednesday2_table()
        self._create_thursday2_table()
        self._create_friday2_table()
        self._create_saturday2_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox3.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule2_tab.setLayout(self.svbox)

    def _create_shedule3_tab(self):
        self.shedule3_tab = QWidget()
        self.tabs.addTab(self.shedule3_tab, "Subject")

        self.Subject_gbox = QGroupBox("Subject")

        self.svbox = QVBoxLayout()

        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.Subject_gbox)

        self._create_Subject_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule3_tab.setLayout(self.svbox)

    def _create_shedule4_tab(self):
        self.shedule3_tab = QWidget()
        self.tabs.addTab(self.shedule3_tab, "Teacher")

        self.Teacher_gbox = QGroupBox("Teacher")
        self.Vers_gbox = QGroupBox("Vers")

        self.svbox = QVBoxLayout()

        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.Teacher_gbox)
        self.shbox1.addWidget(self.Vers_gbox)

        self._create_Teacher_table()
        self._create_Vers_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule3_tab.setLayout(self.svbox)

    def _create_Teacher_table(self):
        self.Teacher_table = QTableWidget()
        self.Teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.Teacher_table.setColumnCount(5)
        self.Teacher_table.setHorizontalHeaderLabels(['id',"Teacher",'Subject',"",''])

        self._update_Teacher_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.Teacher_table)
        self.Teacher_gbox.setLayout(self.mvbox)

    def _update_Teacher_table(self):
        self.cursor.execute("SELECT teacher.id,full_name, subject_id FROM teacher JOIN subject ON subject.id = teacher.subject_id")
        records = list(self.cursor.fetchall())

        self.Teacher_table.setRowCount(len(records) + 1)
        k = 0
        AddButton = QPushButton("Add")
        for i, r in enumerate(records):
            r = list(r)
            k += 1
            joinButton = QPushButton("Join")
            DelButton = QPushButton("Delete")

            self.Teacher_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.Teacher_table.setItem(i, 1,
                                       QTableWidgetItem(str(r[1])))
            self.Teacher_table.setItem(i, 2,
                                       QTableWidgetItem(str(r[2])))
            self.Teacher_table.setCellWidget(i, 3, joinButton)
            self.Teacher_table.setCellWidget(i, 4, DelButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_Teacher_from_table(num))
            DelButton.clicked.connect(lambda ch, num=i: self._Del_Teacher_from_table(num))
        self.Teacher_table.setCellWidget(k, 4, AddButton)
        AddButton.clicked.connect(lambda ch, num=k: self._add_Teacher_from_table(num))
        self.Teacher_table.resizeRowsToContents()

    def _create_Vers_table(self):
        self.Vers_table = QTableWidget()
        self.Vers_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.Vers_table.setColumnCount(3)
        self.Vers_table.setHorizontalHeaderLabels(["Teacher",'Vers',""])

        self._update_Vers_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.Vers_table)
        self.Vers_gbox.setLayout(self.mvbox)

    def _update_Vers_table(self):
        self.cursor.execute("SELECT * FROM teacher_vers")
        records = list(self.cursor.fetchall())

        self.Vers_table.setRowCount(len(records) + 1)
        k = 0
        AddButton = QPushButton("Add")
        for i, r in enumerate(records):
            r = list(r)
            k += 1
            DelButton = QPushButton("Delete")

            self.Vers_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.Vers_table.setItem(i, 1,
                                       QTableWidgetItem(str(r[1])))
            self.Vers_table.setCellWidget(i, 2, DelButton)

            DelButton.clicked.connect(lambda ch, num=i: self._Del_Vers_from_table(num))
        self.Vers_table.setCellWidget(k, 2, AddButton)
        AddButton.clicked.connect(lambda ch, num=k: self._add_Vers_from_table(num))
        self.Vers_table.resizeRowsToContents()

    def _create_Subject_table(self):
        self.Subject_table = QTableWidget()
        self.Subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.Subject_table.setColumnCount(4)
        self.Subject_table.setHorizontalHeaderLabels(['id',"Subject", "",''])

        self._update_Subject_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.Subject_table)
        self.Subject_gbox.setLayout(self.mvbox)

    def _update_Subject_table(self):
        self.cursor.execute("SELECT name_p, id  FROM SUBJECT ORDER BY id ")
        records = list(self.cursor.fetchall())

        self.Subject_table.setRowCount(len(records) + 1)
        global k
        k = 0
        AddButton = QPushButton("Add")
        for i, r in enumerate(records):
            r = list(r)
            k += 1
            joinButton = QPushButton("Join")
            DelButton = QPushButton("Delete")

            self.Subject_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[0])))
            self.Subject_table.setItem(i, 0,
                                       QTableWidgetItem(str(r[1])))
            self.Subject_table.setCellWidget(i, 2, joinButton)
            self.Subject_table.setCellWidget(i, 3, DelButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_Subject_from_table(num))
            DelButton.clicked.connect(lambda ch, num=i: self._Del_Subject_from_table(num))
        self.Subject_table.setCellWidget(k, 3, AddButton)
        AddButton.clicked.connect(lambda ch, num=k: self._add_Subject_from_table(num))
        self.Subject_table.resizeRowsToContents()

    def _change_Subject_from_table(self, rowNum):
        row = list()

        for i in range(self.Subject_table.columnCount()):
            try:
                row.append(self.Subject_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("SELECT id FROM SUBJECT WHERE name_p = %s ", (row[1],))
            rec = list(self.cursor.fetchall())
            self.cursor.execute("UPDATE subject SET name_p = %s WHERE id = %s", (str(row[1]), int(row[0])))
            self.conn.commit()
            print(row, rec)
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_Teacher_from_table(self, rowNum):
        row = list()

        for i in range(self.Teacher_table.columnCount()):
            try:
                row.append(self.Teacher_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("SELECT id FROM Teacher WHERE full_name = %s ", (row[1],))
            rec = list(self.cursor.fetchall())
            self.cursor.execute("UPDATE Teacher SET full_name = %s and subject_id = %s WHERE id = %s", (str(row[1]),int(row[2]), int(row[0])))
            self.conn.commit()
            print(row, rec)
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _add_Teacher_from_table(self, rowNum):
        row = list()

        for i in range(self.Teacher_table.columnCount()):
            try:
                row.append(self.Teacher_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:

            self.cursor.execute("INSERT INTO Teacher (id,full_name, subject_id) VALUES (%s,%s,%s)", (int(row[0]),str(row[1]),int(row[2])))
            self.conn.commit()
            self._update_Teacher_table()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")
        print(row)

    def _Del_Teacher_from_table(self, rowNum):
        row = list()
        for i in range(self.Teacher_table.columnCount()):
            try:
                row.append(self.Teacher_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("DELETE FROM Teacher WHERE id = %s", (int(row[0]),))
            self.conn.commit()
            self.Teacher_table.setItem(int(row[0]) - 1, 0, None)
            self.Teacher_table.setItem(int(row[0]) - 1, 1, None)
            self.Teacher_table.setItem(int(row[0]) - 1, 2, None)
            self.Teacher_table.removeCellWidget(int(row[0]) - 1, 3)
            self._update_Teacher_table()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _add_Subject_from_table(self, rowNum):
        row = list()

        for i in range(self.Subject_table.columnCount()):
            try:
                row.append(self.Subject_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:

            self.cursor.execute("INSERT INTO subject (id,name_p) VALUES (%s,%s)", (int(row[0]),str(row[1])))
            self.conn.commit()
            self._update_Subject_table()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _Del_Subject_from_table(self, rowNum):
        row = list()
        for i in range(self.Subject_table.columnCount()):
            try:
                row.append(self.Subject_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("DELETE FROM subject WHERE id = %s", (int(row[0]),))
            self.conn.commit()
            self.Subject_table.setItem(int(row[0]) - 1, 0, None)
            self.Subject_table.setItem(int(row[0]) - 1, 1, None)
            self.Subject_table.removeCellWidget(int(row[0]) - 1, 2)
            self._update_Subject_table()

        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _add_Vers_from_table(self, rowNum):
        row = list()

        for i in range(self.Vers_table.columnCount()):
            try:
                row.append(self.Vers_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:

            self.cursor.execute("INSERT INTO teacher_vers (teacher_id, vers_id) VALUES (%s,%s)", (int(row[0]),str(row[1])))
            self.conn.commit()
            self._update_Vers_table()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")
        print(row)

    def _Del_Vers_from_table(self, rowNum):
        row = list()
        for i in range(self.Vers_table.columnCount()):
            try:
                row.append(self.Vers_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("DELETE FROM teacher_vers WHERE teacher_id = %s and vers_id = %s", (int(row[0]),int(row[1])))
            self.conn.commit()
            self.Vers_table.setItem(int(k) - 1, 0, None)
            self.Vers_table.setItem(int(k) - 1, 1, None)
            self.Vers_table.removeCellWidget(int(row[0]) - 1, 2)
            self._update_Vers_table()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")
        print(row)

    def _create_monday_table(self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(5)
        self.monday_table.setHorizontalHeaderLabels(["Time", "Kab", "Vers", "Subject", ""])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()
        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(5)
        self.tuesday_table.setHorizontalHeaderLabels(["Time", "Kab", "Vers", "Subject", ""])

        self._update_tuesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table)
        self.tuesday_gbox.setLayout(self.mvbox)

    def _create_wednesday_table(self):
        self.wednesday_table = QTableWidget()
        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_table.setColumnCount(5)
        self.wednesday_table.setHorizontalHeaderLabels(["Time", "Kab", "Vers", "Subject", ""])

        self._update_wednesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.wednesday_table)
        self.wednesday_gbox.setLayout(self.mvbox)

    def _create_thursday_table(self):
        self.thursday_table = QTableWidget()
        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_table.setColumnCount(5)
        self.thursday_table.setHorizontalHeaderLabels(["Time", "Kab", "Vers", "Subject", ""])

        self._update_thursday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thursday_table)
        self.thursday_gbox.setLayout(self.mvbox)

    def _create_friday_table(self):
        self.friday_table = QTableWidget()
        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_table.setColumnCount(5)
        self.friday_table.setHorizontalHeaderLabels(["Time", "Kab", "Vers", "Subject", ""])

        self._update_friday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.friday_table)
        self.friday_gbox.setLayout(self.mvbox)

    def _create_saturday_table(self):
        self.saturday_table = QTableWidget()
        self.saturday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.saturday_table.setColumnCount(5)
        self.saturday_table.setHorizontalHeaderLabels(["Time", "Kab", "Vers", "Subject", ""])

        self._update_saturday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.saturday_table)
        self.saturday_gbox.setLayout(self.mvbox)

    def _update_monday_table(self):
        self.cursor.execute("SELECT start_time, subject_id, vers_id, room_numb FROM start \
                            WHERE day_id ='1' and week_id = '1'")

        records = list(self.cursor.fetchall())
        self.monday_table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            self.monday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.monday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[3])))
            self.monday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[1])))
            self.monday_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num,1,1))

        self.monday_table.resizeRowsToContents()

    def _update_tuesday_table(self):
        self.cursor.execute("SELECT start_time, subject_id, vers_id, room_numb FROM start \
                            WHERE day_id ='2' and week_id = '1'")

        records = list(self.cursor.fetchall())
        self.tuesday_table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.tuesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.tuesday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[3])))
            self.tuesday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[2])))
            self.tuesday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[1])))
            self.tuesday_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num,2,1))

            self.tuesday_table.resizeRowsToContents()

    def _update_wednesday_table(self):
        self.cursor.execute("SELECT start_time, subject_id, vers_id, room_numb FROM start \
                                WHERE day_id ='3' and week_id = '1'")

        records = list(self.cursor.fetchall())
        self.wednesday_table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.wednesday_table.setItem(i, 0,
                                           QTableWidgetItem(str(r[0])))
            self.wednesday_table.setItem(i, 1,
                                           QTableWidgetItem(str(r[3])))
            self.wednesday_table.setItem(i, 2,
                                           QTableWidgetItem(str(r[2])))
            self.wednesday_table.setItem(i, 3,
                                           QTableWidgetItem(str(r[1])))
            self.wednesday_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num,3,1))

            self.wednesday_table.resizeRowsToContents()

    def _update_thursday_table(self):
        self.cursor.execute("SELECT start_time, subject_id, vers_id, room_numb FROM start \
                                WHERE day_id ='4' and week_id = '1'")

        records = list(self.cursor.fetchall())
        self.thursday_table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.thursday_table.setItem(i, 0,
                                           QTableWidgetItem(str(r[0])))
            self.thursday_table.setItem(i, 1,
                                           QTableWidgetItem(str(r[3])))
            self.thursday_table.setItem(i, 2,
                                           QTableWidgetItem(str(r[2])))
            self.thursday_table.setItem(i, 3,
                                           QTableWidgetItem(str(r[1])))
            self.thursday_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num,4,1))

            self.thursday_table.resizeRowsToContents()

    def _update_friday_table(self):
        self.cursor.execute("SELECT start_time, subject_id, vers_id, room_numb FROM start \
                                WHERE day_id ='5' and week_id = '1'")

        records = list(self.cursor.fetchall())
        self.friday_table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.friday_table.setItem(i, 0,
                                           QTableWidgetItem(str(r[0])))
            self.friday_table.setItem(i, 1,
                                           QTableWidgetItem(str(r[3])))
            self.friday_table.setItem(i, 2,
                                           QTableWidgetItem(str(r[2])))
            self.friday_table.setItem(i, 3,
                                           QTableWidgetItem(str(r[1])))
            self.friday_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num,5,1))

            self.friday_table.resizeRowsToContents()

    def _update_saturday_table(self):
        self.cursor.execute("SELECT start_time, subject_id, vers_id, room_numb FROM start \
                                WHERE day_id ='6' and week_id = '1'")

        records = list(self.cursor.fetchall())
        self.saturday_table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.saturday_table.setItem(i, 0,
                                           QTableWidgetItem(str(r[0])))
            self.saturday_table.setItem(i, 1,
                                           QTableWidgetItem(str(r[3])))
            self.saturday_table.setItem(i, 2,
                                           QTableWidgetItem(str(r[2])))
            self.saturday_table.setItem(i, 3,
                                           QTableWidgetItem(str(r[1])))
            self.saturday_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num,6,1))

            self.saturday_table.resizeRowsToContents()

    def _create_monday2_table(self):
        self.monday2_table = QTableWidget()
        self.monday2_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday2_table.setColumnCount(5)
        self.monday2_table.setHorizontalHeaderLabels(["Time", "Kab", "Vers", "Subject", ""])

        self._update_monday2_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday2_table)
        self.monday2_gbox.setLayout(self.mvbox)

    def _create_tuesday2_table(self):
        self.tuesday2_table = QTableWidget()
        self.tuesday2_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday2_table.setColumnCount(5)
        self.tuesday2_table.setHorizontalHeaderLabels(["Time", "Kab", "Vers", "Subject", ""])

        self._update_tuesday2_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday2_table)
        self.tuesday2_gbox.setLayout(self.mvbox)

    def _create_wednesday2_table(self):
        self.wednesday2_table = QTableWidget()
        self.wednesday2_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday2_table.setColumnCount(5)
        self.wednesday2_table.setHorizontalHeaderLabels(["Time", "Kab", "Vers", "Subject", ""])

        self._update_wednesday2_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.wednesday2_table)
        self.wednesday2_gbox.setLayout(self.mvbox)

    def _create_thursday2_table(self):
        self.thursday2_table = QTableWidget()
        self.thursday2_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday2_table.setColumnCount(5)
        self.thursday2_table.setHorizontalHeaderLabels(["Time", "Kab", "Vers", "Subject", ""])

        self._update_thursday2_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thursday2_table)
        self.thursday2_gbox.setLayout(self.mvbox)

    def _create_friday2_table(self):
        self.friday2_table = QTableWidget()
        self.friday2_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday2_table.setColumnCount(5)
        self.friday2_table.setHorizontalHeaderLabels(["Time", "Kab", "Vers", "Subject", ""])

        self._update_friday2_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.friday2_table)
        self.friday2_gbox.setLayout(self.mvbox)

    def _create_saturday2_table(self):
        self.saturday2_table = QTableWidget()
        self.saturday2_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.saturday2_table.setColumnCount(5)
        self.saturday2_table.setHorizontalHeaderLabels(["Time", "Kab", "Vers", "Subject", ""])

        self._update_saturday2_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.saturday2_table)
        self.saturday2_gbox.setLayout(self.mvbox)

    def _update_monday2_table(self):
        self.cursor.execute("SELECT start_time, subject_id, vers_id, room_numb FROM start \
                            WHERE day_id ='1' and week_id = '2'")

        records = list(self.cursor.fetchall())
        self.monday2_table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.monday2_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.monday2_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[3])))
            self.monday2_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[2])))
            self.monday2_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[1])))
            self.monday2_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num,1,2))

        self.monday2_table.resizeRowsToContents()

    def _update_tuesday2_table(self):
        self.cursor.execute("SELECT start_time, subject_id, vers_id, room_numb FROM start \
                            WHERE day_id ='2' and week_id = '2'")

        records = list(self.cursor.fetchall())
        self.tuesday2_table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.tuesday2_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.tuesday2_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[3])))
            self.tuesday2_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[2])))
            self.tuesday2_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[1])))
            self.tuesday2_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num,2,2))

            self.tuesday2_table.resizeRowsToContents()

    def _update_wednesday2_table(self):
        self.cursor.execute("SELECT start_time, subject_id, vers_id, room_numb FROM start \
                                WHERE day_id ='3' and week_id = '2'")

        records = list(self.cursor.fetchall())
        self.wednesday2_table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.wednesday2_table.setItem(i, 0,
                                           QTableWidgetItem(str(r[0])))
            self.wednesday2_table.setItem(i, 1,
                                           QTableWidgetItem(str(r[3])))
            self.wednesday2_table.setItem(i, 2,
                                           QTableWidgetItem(str(r[2])))
            self.wednesday2_table.setItem(i, 3,
                                           QTableWidgetItem(str(r[1])))
            self.wednesday2_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num,3,2))

            self.wednesday2_table.resizeRowsToContents()

    def _update_thursday2_table(self):
        self.cursor.execute("SELECT start_time, subject_id, vers_id, room_numb FROM start \
                                WHERE day_id ='4' and week_id = '1'")

        records = list(self.cursor.fetchall())
        self.thursday2_table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.thursday2_table.setItem(i, 0,
                                           QTableWidgetItem(str(r[0])))
            self.thursday2_table.setItem(i, 1,
                                           QTableWidgetItem(str(r[3])))
            self.thursday2_table.setItem(i, 2,
                                           QTableWidgetItem(str(r[2])))
            self.thursday2_table.setItem(i, 3,
                                           QTableWidgetItem(str(r[1])))
            self.thursday2_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num,4,2))

            self.thursday2_table.resizeRowsToContents()

    def _update_friday2_table(self):
        self.cursor.execute("SELECT start_time, subject_id, vers_id, room_numb FROM start \
                                WHERE day_id ='5' and week_id = '2'")

        records = list(self.cursor.fetchall())
        self.friday2_table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.friday2_table.setItem(i, 0,
                                           QTableWidgetItem(str(r[0])))
            self.friday2_table.setItem(i, 1,
                                           QTableWidgetItem(str(r[3])))
            self.friday2_table.setItem(i, 2,
                                           QTableWidgetItem(str(r[2])))
            self.friday2_table.setItem(i, 3,
                                           QTableWidgetItem(str(r[1])))
            self.friday2_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num,5,2))

            self.friday2_table.resizeRowsToContents()

    def _update_saturday2_table(self):
        self.cursor.execute("SELECT start_time, subject_id, vers_id, room_numb FROM start \
                                WHERE day_id ='6' and week_id = '2'")

        records = list(self.cursor.fetchall())
        self.saturday2_table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.saturday2_table.setItem(i, 0,
                                           QTableWidgetItem(str(r[0])))
            self.saturday2_table.setItem(i, 1,
                                           QTableWidgetItem(str(r[3])))
            self.saturday2_table.setItem(i, 2,
                                           QTableWidgetItem(str(r[2])))
            self.saturday2_table.setItem(i, 3,
                                           QTableWidgetItem(str(r[1])))
            self.saturday2_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num,6,2))

            self.saturday2_table.resizeRowsToContents()

    def _change_day_from_table(self, rowNum, day, week):
        row = list()
        if day == 1 and week == 1:
            for i in range(self.monday_table.columnCount()):
                try:
                    row.append(self.monday_table.item(rowNum, i).text())
                except:
                    row.append(None)

        if day == 2 and week == 1:
            for i in range(self.tuesday_table.columnCount()):
                try:
                    row.append(self.tuesday_table.item(rowNum, i).text())
                except:
                    row.append(None)

        if day == 3 and week == 1:
            for i in range(self.wednesday_table.columnCount()):
                try:
                    row.append(self.wednesday_table.item(rowNum, i).text())
                except:
                    row.append(None)

        if day == 4 and week == 1:
            for i in range(self.thursday_table.columnCount()):
                try:
                    row.append(self.thursday_table.item(rowNum, i).text())
                except:
                    row.append(None)

        if day == 5 and week == 1:
            for i in range(self.friday_table.columnCount()):
                try:
                    row.append(self.friday_table.item(rowNum, i).text())
                except:
                    row.append(None)

        if day == 6 and week == 1:
            for i in range(self.saturday_table.columnCount()):
                try:
                    row.append(self.saturday_table.item(rowNum, i).text())
                except:
                    row.append(None)

        if day == 1 and week == 2:
            for i in range(self.monday2_table.columnCount()):
                try:
                    row.append(self.monday2_table.item(rowNum, i).text())
                except:
                    row.append(None)

        if day == 2 and week == 2:
            for i in range(self.tuesday2_table.columnCount()):
                try:
                    row.append(self.tuesday2_table.item(rowNum, i).text())
                except:
                    row.append(None)

        if day == 3 and week == 2:
            for i in range(self.wednesday2_table.columnCount()):
                try:
                    row.append(self.wednesday2_table.item(rowNum, i).text())
                except:
                    row.append(None)

        if day == 4 and week == 2:
            for i in range(self.thursday2_table.columnCount()):
                try:
                    row.append(self.thursday2_table.item(rowNum, i).text())
                except:
                    row.append(None)

        if day == 5 and week == 2:
            for i in range(self.friday2_table.columnCount()):
                try:
                    row.append(self.friday2_table.item(rowNum, i).text())
                except:
                    row.append(None)

        if day == 6 and week == 2:
            for i in range(self.saturday2_table.columnCount()):
                try:
                    row.append(self.saturday2_table.item(rowNum, i).text())
                except:
                    row.append(None)

        try:
            self.cursor.execute("UPDATE timetable SET subject_id = %s, vers_id = %s, room_numb = %s WHERE day_id = %s and week_id = %s and start_time = %s ", (int(row[3]),int(row[2]),str(row[1]),int(day),int(week), str(row[0])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _update_shedule(self):
        self._update_monday_table()
        self._update_tuesday_table()
        self._update_wednesday_table()
        self._update_thursday_table()
        self._update_friday_table()
        self._update_saturday_table()
        self._update_monday2_table()
        self._update_tuesday2_table()
        self._update_wednesday2_table()
        self._update_thursday2_table()
        self._update_friday2_table()
        self._update_saturday2_table()
        self._update_Subject_table()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
