import sys
import os
import traceback
from Scalc import solve
from Calculus import integrate, differ
from Graph import show_graph
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5 import uic
Ui_MainWindow, QtBaseClass = uic.loadUiType('calcUI.ui')

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        menuBar = self.menuBar()
        modeMenu = menuBar.addMenu('&Modes')
        
        # Calculator Action
        self.calcAction = QAction('&Calculator', self)
        self.calcAction.triggered.connect(self.CalcCall)
        modeMenu.addAction(self.calcAction)
        # Calculus Begins
        calculusMenu = modeMenu.addMenu('&Calculus')
        # Differenciation
        self.integrateAction = QAction('&Differenciate', self)
        self.integrateAction.triggered.connect(self.DifferCall)
        calculusMenu.addAction(self.integrateAction)
        # Integrate Action
        self.integrateAction = QAction('&Integrate', self)
        self.integrateAction.triggered.connect(self.IntegrateCall)
        calculusMenu.addAction(self.integrateAction)
        # Graph Action
        self.graphAction = QAction('&Graph', self)
        self.graphAction.triggered.connect(self.GraphCall)
        modeMenu.addAction(self.graphAction)
        #
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lwrLim.hide()
        self.ui.uprLim.hide()
        self.ui.lower_lim.hide()
        self.ui.upper_lim.hide()
        self.ui.integSym.hide()
        self.ui.diffSym.hide()
        self.ui.sumSym.show()
        self.ui.expr1.textChanged.connect(self.Solve)

    def IntegrateCall(self):
        self.ui.integSym.show()
        self.ui.diffSym.hide()
        self.ui.sumSym.hide()
        self.ui.lwrLim.hide()
        self.ui.uprLim.hide()
        self.ui.floatResp.hide()
        self.ui.lower_lim.hide()
        self.ui.upper_lim.hide()
        self.ui.resp.show()
        self.ui.expr1.textChanged.connect(self.Integrate)

    def DifferCall(self):
        self.ui.integSym.hide()
        self.ui.diffSym.show()
        self.ui.sumSym.hide()
        self.ui.lwrLim.hide()
        self.ui.uprLim.hide()
        self.ui.floatResp.hide()
        self.ui.lower_lim.hide()
        self.ui.upper_lim.hide()
        self.ui.resp.show()
        self.ui.expr1.textChanged.connect(self.Differ)
        
    def CalcCall(self):
        self.ui.integSym.hide()
        self.ui.diffSym.hide()
        self.ui.lwrLim.hide()
        self.ui.uprLim.hide()
        self.ui.lower_lim.hide()
        self.ui.upper_lim.hide()
        self.ui.sumSym.show()
        self.ui.resp.show()
        self.ui.floatResp.show()
        self.ui.expr1.textChanged.connect(self.Solve)

    def GraphCall(self):
        self.ui.integSym.hide()
        self.ui.diffSym.hide()
        self.ui.sumSym.hide()
        self.ui.resp.hide()
        self.ui.floatResp.hide()
        self.ui.lower_lim.show()
        self.ui.upper_lim.show()
        self.ui.lwrLim.show()
        self.ui.uprLim.show()
        self.ui.expr1.returnPressed.connect(self.Plot)

    def Plot(self):
        try:
            q = str(self.ui.expr1.displayText())
            l_lim = str(self.ui.lwrLim.displayText())
            u_lim = str(self.ui.uprLim.displayText())
            
            if l_lim == '':
                l_lim = '0'
            
            if u_lim == '':
                u_lim = '0'
            
            if q == '':
                self.ui.resp.setText(q)
                return
            
            show_graph(q,[l_lim,u_lim])        
        except:
            print(traceback.format_exc())
            return
        

    def Solve(self):
        try:
            q = str(self.ui.expr1.displayText())
            if q == '':
                self.ui.resp.setText('')
                self.ui.floatResp.setText('')
                return
            ev = str(solve(q))
            try:
                fl_ev = str(solve('float('+q+')'))
                self.ui.floatResp.setText(fl_ev)
            except:
                self.ui.floatResp.setText('')
        except:
            self.ui.resp.setText('')
            self.ui.floatResp.setText('')
            return
        self.ui.resp.setText(ev)

    def Integrate(self):
        try:
            q = str(self.ui.expr1.displayText())
            if q == '':
                self.ui.resp.setText(q)
                return
            ev = str(integrate(q))
        except:
            self.ui.resp.setText('')
            return
        self.ui.resp.setText(ev)

    def Differ(self):
        try:
            q = str(self.ui.expr1.displayText())
            if q == '':
                self.ui.resp.setText(q)
                return
            ev = str(differ(q))
            
        except:
            self.ui.resp.setText('')
            return
        self.ui.resp.setText(ev)
        
if __name__ == '__main__':
    pyqtRemoveInputHook()
    app = QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle('OmniCalc')
    window.show()
    sys.exit(app.exec())
