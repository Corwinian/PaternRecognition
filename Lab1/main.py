#! /usr/bin/python
# -*- coding: utf-8 -*-
#

import sys
import random
from collections import namedtuple
from PyQt4 import QtCore, QtGui, uic  # подключает основные модули PyQt

# прототип главной формы
class MainForm(QtGui.QMainWindow):

    # конструктор
    def __init__(self):
        super(MainForm, self).__init__()

        # динамически загружает визуальное представление формы
        uic.loadUi("mainwindow.ui", self)

        # связывает событие нажатия на кнопку с методом
        self.connect(self.btnStart, QtCore.SIGNAL("clicked()"), self.calc_classic_ver)

    def setLabelText(self):
        self.label.setText("New label text")

    def calc_classic_ver(self):
        temp = ();
        uniq_count = 0
        two_count = 0
        two_pair_count = 0
        three_count = 0

        count = int(self.lExpCount.text())            

        for i in range(count):
            print (i)
            ran_str = str(random.randint(0, 9999))

            while (len(ran_str) != 4):
                ran_str= "0"+ran_str

            res = {}

            for ch in ran_str:
                if ch not in res.keys():
                    res[ch] = 1 
                else:
                    res[ch] += 1

            isUniq = True
            isTwoPair = False
            
            for ch in res.values():
                if ch != 1:
                    isUniq = False
                if ch == 2:
                    if isTwoPair:
                        two_pair_count+= 1
                    else:
                        two_count+=1 
                    isTwoPair = True
                elif ch == 3:
                    three_count+=1
                elif ch == 4:
                    two_pair_count+=1

            if isUniq:
                uniq_count+=1
        
        self.leUniq.setText(str(uniq_count/count))
        self.lePair.setText(str(two_count/count))
        self.leTwoPair.setText(str(two_pair_count/count))
        self.leThree.setText(str(three_count/count))

        #Аналитическое решение
        #количество 4 значных номеров 10000

        #Событие A - количество уникальных цифр 
        #10*9*8*7=5040 номеров тогда P(A) = 5040/10000 =0.504
        #
        #Событие B - количество пар
        #есть 12 способов разместить тройку числел a,b,c (abac,aabc, acda, caab, caba, baca .....)
        #для каждого a существует 36 таких троек
        #
        #10 *12 *36 = 4320 номеров, тогда P(B)=4320/10000 = 0.432
        #
        #Событие C - количество троек
        #есть 4 способов располодить числа a,b (aaab, aaba, abbb)
        #при етом таких вариантов a ceotndetn 9 вариантов
        # 10*4*9 = 360
        #тогда P(С)=360/10000 = 0.036
        #
        #Событие D - количество 2 пар
        #есть 6 способов расположить пару цифр a,b (aabb, abba, abab....)
        #кличесво пар - 45 (+9+8+7+6+5+4+3+2+1) 
        #6*45 = 270, 
        #P(D)=270/10000 = 0.027
        #
        self.laUniq.setText(str(5040/10000))
        self.laPair.setText(str(4320/10000))
        self.laTwoPair.setText(str(270/10000))
        self.laThree.setText(str(360/10000))


def main():
    app = QtGui.QApplication(sys.argv)  # создаёт основной объект программы
    form = MainForm()  # создаёт объект формы
    form.show()  # даёт команду на отображение объекта формы и содержимого
#    w = QtGui.QWidget()
 
  #  w.resize(320, 240)  # изменить размеры виджета
   # w.setWindowTitle("Hello, World!")  # установить заголовок
    #w.show()  # отобразить окно на экране
    app.exec()  # запускает приложение

if __name__ == "__main__":
    sys.exit(main())

 