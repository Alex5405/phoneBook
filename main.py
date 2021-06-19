#ФИО: Хаметзянов Александр Александрович
#Группа: БСБО-08-19
from IPython.external.qt_for_kernel import QtCore

import design_main_window  # Это наш конвертированный файл design
import sqlite3
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
    QAction, QFileDialog, QApplication)
from tkinter import *
from tkinter import messagebox
#from PyQt5.QtGui import QIcon

class ExampleApp(QMainWindow, design_main_window.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.actionAdd.triggered.connect(self.test)
        self.actionRemove.triggered.connect(self.test)
        self.actionSearch.triggered.connect(self.test)

    def test(self):
        design_main_window.contact_count = 23
        design_main_window.Ui_MainWindow.printValue()
        print("ФИО: Хаметзянов Александр Александрович")

def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()