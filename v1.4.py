import sys
from sys import argv
# Импортируем наш интерфейс
from GEN import *
from SEC import *
from mainform import*
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from sympy import Matrix
import random
from functools import partial
# проверка на простое число
def is_prime(n):
    if n< 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True
rejim=''

class Generat(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=GEN()
        self.ui.setupUi(self)
        if rejim=='BL':
            self.ui.pushButton.clicked.connect(self.doliBL)
        elif rejim=='SHA':
            self.ui.pushButton.clicked.connect(self.doliSHA)
        else:
            self.ui.textEdit.setText('Введите K,N через пробел')
            self.ui.pushButton.clicked.connect(self.doliKTO)

    def doliBL(self):
        try:
            sistem=list(map(int,self.ui.textEdit.toPlainText().split()))
            secret=int(self.ui.textEdit_2.toPlainText())
        except :
            em = QtWidgets.QErrorMessage(self)
            em.showMessage("Не те данные")
            return
        x=[]
        x.append(secret)
        prv=is_prime(sistem[2])
        if sistem[0]>sistem[1] or prv!=True or sistem[2]<=secret:
            em = QtWidgets.QErrorMessage(self)
            em.showMessage("Не те данные")
            return
        for i in range(1,sistem[0]):
            x.append(random.randint(0,1000))
        mas=[]
        for i in range(sistem[1]):
            listA=[]
            for j in range(sistem[0]):
                listA.append(random.randint(0,1000))
            listA.append(sum(np.array(listA)*np.array(x))%sistem[2])
            mas.append(listA)

        self.ui.textEdit_3.setText("Ваши данные:")
        for i in range(len(mas)):
            vivod=''
            for j in range(len(mas[i])):
                if j!=len(mas[i])-1:
                    vivod+=(f"A{i,j} = {mas[i][j]} ")
                else:
                    vivod+=(f"B{i} = {mas[i][j]} ")
            self.ui.textEdit_3.append(vivod +'\n')

    def doliSHA(self):
        try:
            sistem=list(map(int,self.ui.textEdit.toPlainText().split()))
            secret=int(self.ui.textEdit_2.toPlainText())
        except :
            em = QtWidgets.QErrorMessage(self)
            em.showMessage("Не те данные")
            return
        prv=is_prime(sistem[2])
        if sistem[0]>sistem[1] or prv!=True or sistem[2]<=secret:
            em = QtWidgets.QErrorMessage(self)
            em.showMessage("Не те данные")
            return
        a =[]
        k=sistem[0]
        n=sistem[1]
        for i in range(k-1):
            a.append(random.randint(2,1000))
        x=[i for i in range(1,n+1)]
        ki = []
        for i in range(n):
                sm = secret
                for j in range(k-1):
                    sm += a[j]*(x[i]**(k-j-1))
                ki.append(sm%sistem[2])

        vivod=''
        self.ui.textEdit_3.setText("Ваши данные:")
        for i in range(len(ki)):
            vivod+=f'A{i}={x[i],ki[i]}\n'
        self.ui.textEdit_3.append(vivod)
    def doliKTO(self):
        try:
            sistem=list(map(int,self.ui.textEdit.toPlainText().split()))
            secret=int(self.ui.textEdit_2.toPlainText())
        except :
            em = QtWidgets.QErrorMessage(self)
            em.showMessage("Не те данные")
            return
        x=[]
        mas=[]
        k=sistem[0]
        n=sistem[1]

        primes = [i for i in range(int(secret**(1/k)),int(secret**(1/(k-1)))) if is_prime(i)]
        #print(primes)
        #print(primes,int(secret**-k),int(secret**-(k-1)))
        if sistem[0]>sistem[1] or primes==[] :
            em = QtWidgets.QErrorMessage(self)
            em.showMessage("Не те данные")
            return
        for i in range(0,n):
            p=random.choice(primes)
            x.append(p)
            mas.append(secret%p)
        self.ui.textEdit_3.setText("Ваши данные:")
        vivod=''
        for i in range(len(mas)):
            vivod+=(f"A{i} = {mas[i]} P{i} = {x[i]} \n")
        self.ui.textEdit_3.append(vivod +'\n')

#Вкладка о программе
class Secret(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=SEC()
        self.ui.setupUi(self)
        if rejim=='BL':
            self.ui.pushButton.clicked.connect(self.doliBL)
        elif rejim=='SHA':
            self.ui.pushButton.clicked.connect(self.doliSHA)
        else:
            self.ui.textEdit.setText('Введите K,N через пробел')
            self.ui.pushButton.clicked.connect(self.doliKTO)
    def doliKTO(self):
        try:
            sistem=list(map(int,self.ui.textEdit.toPlainText().split()))
            dannie=list(map(int,self.ui.textEdit_3.toPlainText().split()))
        except :
            em = QtWidgets.QErrorMessage(self)
            em.showMessage("Не те данные")
            return

        k=sistem[0]
        n=sistem[1]
        if k>n or len(dannie)/2!=k :
            em = QtWidgets.QErrorMessage(self)
            em.showMessage("Не те данные")
            return
        Mob=1
        masM=[]
        masY=[]
        masP=[]
        for i in range(1,k+1):
            Mob*=dannie[i]
            masP.append(dannie.pop(i))
        for i in range(k):
            m=Mob//masP[i]
            masM.append(m)
            masY.append(pow(m,-1,masP[i]))
        N=0
        for i in range(len(dannie)):
            N+=dannie[i]*masM[i]*masY[i]
        self.ui.textEdit_2.setText(f"Секрет = {N%Mob}")
    def doliBL(self):
        try:
            sistem=list(map(int,self.ui.textEdit.toPlainText().split()))
            dannie=list(map(int,self.ui.textEdit_3.toPlainText().split()))
        except :
            em = QtWidgets.QErrorMessage(self)
            em.showMessage("Не те данные")
            return

        k=sistem[0]
        n=sistem[1]
        p=sistem[2]
        if k>n or len(dannie)/k!=k+1 :
            em = QtWidgets.QErrorMessage(self)
            em.showMessage("Не те данные")
            return
        masA=[]
        masB=[]
        for i in range(k):
            masA.append(list(dannie[j+i*(k+1)] for j in range(k)))
            masB.append(dannie[k+i*(k+1)])
        A=Matrix(masA)
        D=np.array((A.inv_mod(p))).T
        masB = np.array(masB).T
        resh=masB.dot(D)
        resh=resh%p
        self.ui.textEdit_2.setText(f"Секрет = {resh[0]}")
    def doliSHA(self):
        try:
            sistem=list(map(int,self.ui.textEdit.toPlainText().split()))
            dannie=list(map(int,self.ui.textEdit_3.toPlainText().split()))
        except :
            em = QtWidgets.QErrorMessage(self)
            em.showMessage("Не те данные")
            return

        k=sistem[0]
        n=sistem[1]
        p=sistem[2]
        if k>n or len(dannie)/2!=k :
            em = QtWidgets.QErrorMessage(self)
            em.showMessage("Не те данные")
            return
        Y=[]
        X=[]
        for i in range(0,k*2,2):
            X.append(dannie[i])
            Y.append(dannie[i+1])

        sm = 0
        for j in range(len(Y)):
            p1=1
            p2=1
            for i in range(len(X)):
                if j != i:
                    p1=p1*(0 - X[i])
                    p2=p2*(X[j] - X[i])
                else:
                    p1=p1*1
                    p2=p2*1
            sm = sm+Y[j]*p1/p2
        sm=int(sm%p)
        self.ui.textEdit_2.setText(f"Секрет = {sm}")


#основный класс программы
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action.triggered.connect(partial(self.doli, "SHA"))
        self.ui.action_2.triggered.connect(partial(self.secr, "SHA"))
        self.ui.action_3.triggered.connect(partial(self.doli, "KTO"))
        self.ui.action_4.triggered.connect(partial(self.secr, "KTO"))
        self.ui.action_5.triggered.connect(partial(self.doli, "BL"))
        self.ui.action_6.triggered.connect(partial(self.secr, "BL"))
        self.widget_2=QtWidgets.QWidget(self)
        self.widget_2.setGeometry(QtCore.QRect(0, 20, 801, 531))

    def doli(self,a):
        global rejim
        rejim=a
        self.widget_2.hide()
        self.widget_2=Generat(self)
        self.widget_2.setGeometry(QtCore.QRect(0, 15, 801, 531))
        self.widget_2.show()
    def secr(self,a):
        global rejim
        rejim=a
        self.widget_2.hide()
        self.widget_2=Secret(self)
        self.widget_2.setGeometry(QtCore.QRect(0,15, 801, 531))
        self.widget_2.show()





#Инициализация программы
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
