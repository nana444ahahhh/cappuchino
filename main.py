import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

l = [["арабика", "средняя", "нет", "500руб", "200мл"], ["капучино", "средняя", "есть", "400руб", "150мл"],
     ["латте", "сильная", "нет", "350", "125мл"],
     ["старбакс", "секретная", "очень много", "1000", "25мл"]]
con = sqlite3.connect("coffee.sqlite3")
cur = con.cursor()
cur.execute(f"""DROP TABLE IF EXISTS coffee;""")
cur.execute(f"""CREATE TABLE coffee("сорт","обжарка","сахар","цена","объем")""")
for i in range(len(l)):
    cur.execute(f"""INSERT INTO coffee("сорт","обжарка","сахар","цена","объем") VALUES{tuple(l[i])}""")
a = cur.execute('''select * from coffee  where сорт == "арабика" ''').fetchall()


class booki(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.infa)

    def infa(self):
        b = self.lineEdit.text()
        print(b)
        try:
            a = cur.execute(f'''select * from coffee  where сорт == "{b}" ''').fetchall()
            self.label_3.setText(list(*a)[1])
            self.label_5.setText(list(*a)[2])
            self.label_7.setText(list(*a)[3])
            self.label_9.setText(list(*a)[4])
            self.label_10.setText("")
        except Exception:
            self.label_10.setText("такого у нас нет...")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = booki()
    ex.show()
    sys.exit(app.exec())
