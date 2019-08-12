'''
Created on 2019�?7�?21�?

@author: 55057
'''

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.Qt import QMainWindow
from ORM_model.decBaseClass import Book
import datetime
from core.book_querier_engine import ISBNSearchEngine
from core.rawdata_orm import InsertBook, BuildDatabaseRawDataORM, \
    InsertBatchBooks
from core.loggers import logger


class QtLibraryUI(QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 751, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.text_isbn = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.text_isbn.setObjectName("text_isbn")
        self.horizontalLayout.addWidget(self.text_isbn)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(20, 160, 751, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.btn_ISBNQuery = QtWidgets.QPushButton(self.tab)
        self.btn_ISBNQuery.setGeometry(QtCore.QRect(100, 440, 101, 41))
        self.btn_ISBNQuery.setObjectName("btn_ISBNQuery")
        self.btn_databaseQuery = QtWidgets.QPushButton(self.tab)
        self.btn_databaseQuery.setGeometry(QtCore.QRect(270, 440, 101, 41))
        self.btn_databaseQuery.setObjectName("btn_databaseQuery")
        self.btn_addBook = QtWidgets.QPushButton(self.tab)
        self.btn_addBook.setGeometry(QtCore.QRect(450, 440, 101, 41))
        self.btn_addBook.setObjectName("btn_addBook")
        self.btn_delBook = QtWidgets.QPushButton(self.tab)
        self.btn_delBook.setGeometry(QtCore.QRect(600, 440, 101, 41))
        self.btn_delBook.setObjectName("btn_delBook")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.text_path = QtWidgets.QTextEdit(self.tab_2)
        self.text_path.setGeometry(QtCore.QRect(40, 110, 531, 31))
        self.text_path.setObjectName("text_path")
        self.btn_browse = QtWidgets.QPushButton(self.tab_2)
        self.btn_browse.setGeometry(QtCore.QRect(580, 110, 75, 31))
        self.btn_browse.setObjectName("btn_browse")
        self.btn_import = QtWidgets.QPushButton(self.tab_2)
        self.btn_import.setGeometry(QtCore.QRect(660, 110, 75, 31))
        self.btn_import.setObjectName("btn_import")
        self.text_importMsg = QtWidgets.QTextBrowser(self.tab_2)
        self.text_importMsg.setGeometry(QtCore.QRect(40, 170, 701, 192))
        self.text_importMsg.setObjectName("text_importMsg")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.text_port = QtWidgets.QTextEdit(self.tab_3)
        self.text_port.setGeometry(QtCore.QRect(150, 150, 104, 31))
        self.text_port.setObjectName("text_port")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 71, 21))
        self.label_2.setObjectName("label_2")
        self.btn_start = QtWidgets.QPushButton(self.tab_3)
        self.btn_start.setGeometry(QtCore.QRect(80, 220, 121, 41))
        self.btn_start.setObjectName("btn_start")
        self.btn_restart = QtWidgets.QPushButton(self.tab_3)
        self.btn_restart.setGeometry(QtCore.QRect(520, 220, 121, 41))
        self.btn_restart.setObjectName("btn_restart")
        self.btn_stop = QtWidgets.QPushButton(self.tab_3)
        self.btn_stop.setGeometry(QtCore.QRect(310, 220, 121, 41))
        self.btn_stop.setObjectName("btn_stop")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ISBN�?"))
        self.btn_ISBNQuery.setText(_translate("MainWindow", "ISBN查询"))
        self.btn_databaseQuery.setText(_translate("MainWindow", "库内查询"))
        self.btn_addBook.setText(_translate("MainWindow", "图书录入"))
        self.btn_delBook.setText(_translate("MainWindow", "图书删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "图书信息"))
        self.btn_browse.setText(_translate("MainWindow", "浏览"))
        self.btn_import.setText(_translate("MainWindow", "导入"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "数据导入"))
        self.label_2.setText(_translate("MainWindow", "服务器端�?"))
        self.btn_start.setText(_translate("MainWindow", "启动"))
        self.btn_restart.setText(_translate("MainWindow", "重启"))
        self.btn_stop.setText(_translate("MainWindow", "停止"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "数据服务�?"))

    # 设置按钮事件
    def setupSignalsAndslots(self, MainWindow):
        # ISBN查询
        self.btn_ISBNQuery.clicked.connect(self.btnISBNQuertClicked)
        # 浏览按钮事件
        self.btn_browse.clicked.connect(self.btnBrowseClicked)
        # 添加书本
        self.btn_addBook.clicked.connect(self.btnAddBookClicked)
        # Execl批量导入
        self.btn_import.clicked.connect(self.btnBookBatchImportClicked)
    
    # ISBN查询图书信息
    def btnISBNQuertClicked(self):
        # QMessageBox.about(self,'test','information')
        str_isbn = self.text_isbn.toPlainText()
        isbnEngine = ISBNSearchEngine()
        book_information = isbnEngine.get_information_with_ISBN(str_isbn)
        if book_information == -1:
            self.textBrowser.setText('查询结果为空�?')
        else:       
            book_information_format = "标题：{0}\n作�??:{1}\n出版社：{2}\n中图分类号：{3}\n价格：{4} CNY\n".format(book_information[0], book_information[1], book_information[2], book_information[3], book_information[4])
            self.textBrowser.setText(book_information_format)

    # 获取导入文件路径   
    def btnBrowseClicked(self):
        path = QtWidgets.QFileDialog.getOpenFileNames(self, '', '', '', '')
        self.text_path.setText(path[0].__str__()[2:][:-2])

    def btnAddBookClicked(self):
        str_isbn = self.text_isbn.toPlainText()
        isbnEngine = ISBNSearchEngine()
        # 获取图书信息
        book_information = isbnEngine.get_information_with_ISBN(str_isbn)
        if book_information == -1:
            self.textBrowser.setText('查询结果为空�?')
        else:       
            book_information_format = "标题：{0}\n作�??:{1}\n出版社：{2}\n中图分类号：{3}\n价格：{4} CNY\n".format(book_information[0], book_information[1], book_information[2], book_information[3], book_information[4])
            self.textBrowser.setText(book_information_format)
            # 构建ORM模型
            book = Book(ISBN=str_isbn, book_name=book_information[0], book_author=book_information[1],
                    book_publisher=book_information[2], book_number=book_information[3],
                    book_price=book_information[4], book_notes=None,
                    book_storoge_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            # 插入图书
            InsertBook(book)
            # 日志记录
            logger.info('Write to database done.')

    # execl 内文件批量导�?
    def btnBookBatchImportClicked(self):
        # 导入文件路径
        file_path = self.text_path.toPlainText()
        # 调试信息
        logger.debug(file_path)
        # 构建原始数据
        books = BuildDatabaseRawDataORM(file_path)
        # 图书批量插入
        InsertBatchBooks(books)
        logger.info("Write to database succeed.")
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = QtLibraryUI()
    ui.setupUi(MainWindow)
    ui.setupSignalsAndslots(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
