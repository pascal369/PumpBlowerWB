# -*- coding: utf-8 -*-
from mimetypes import common_types
import os
import sys
import subprocess
import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtGui
from PySide import QtUiTools
from PySide import QtCore
import importlib
Eqp=['Pump','Blower',]
Pump_type=['SpiralVortexPump','SludgePump','MixedFlowPump','CentrifugalPump','SubmersiblePump','UniaxialScrewPump']
SpiralVortexPump_series=['300','350','400','500','600','700','800']
SludgePump_series=['75x75','100x75','100x100','125x100','150x125','250x200']
MixedFlowPump_series=['600','700','800','900','1000']
CentrifugalPump_series=['40Ax32A','50Ax40A','65Ax50A','80Ax65A','100Ax80A','125Ax100A','150Ax125A']
SubmersiblePump_series=['50A','65A','80A','100A']
UniaxialScrewPump_series=['80A','100A']
Blower_type=['HelicalBlower']
HelicalBlower_series=['32A','40A','50A','65A','80A','100A','125A','150A']

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName('Dialog')
        Dialog.resize(300, 410)
        Dialog.move(1000, 0)
        
        #Eqp
        self.label_Eqp = QtGui.QLabel('Equipment',Dialog)
        self.label_Eqp.setGeometry(QtCore.QRect(10, 13, 100, 12))
        self.comboBox_Eqp = QtGui.QComboBox(Dialog)
        self.comboBox_Eqp.setGeometry(QtCore.QRect(80, 10, 200, 22))
        #Type
        self.label_Type = QtGui.QLabel('Type',Dialog)
        self.label_Type.setGeometry(QtCore.QRect(10, 38, 100, 12))
        self.comboBox_Type = QtGui.QComboBox(Dialog)
        self.comboBox_Type.setGeometry(QtCore.QRect(80, 35, 200, 22))
        #Series
        self.label_Series = QtGui.QLabel('Series',Dialog)
        self.label_Series.setGeometry(QtCore.QRect(10, 63, 100, 12))
        self.comboBox_Series = QtGui.QComboBox(Dialog)
        self.comboBox_Series.setGeometry(QtCore.QRect(80, 60, 200, 22))

        #実行
        self.pushButton = QtGui.QPushButton('Educution',Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 85, 100, 22))
        #tool
        self.pushButton2 = QtGui.QPushButton('Tool',Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(170, 85, 100, 22))

        #img
        self.img = QtGui.QLabel(Dialog)
        self.img.setGeometry(QtCore.QRect(30, 140, 250, 250))
        self.img.setAlignment(QtCore.Qt.AlignCenter)

        self.comboBox_Eqp.addItems(Eqp)
        self.comboBox_Eqp.setCurrentIndex(1)
        self.comboBox_Eqp.currentIndexChanged[int].connect(self.onEqp)
        self.comboBox_Eqp.setCurrentIndex(0)

        self.comboBox_Type.setCurrentIndex(1)
        self.comboBox_Type.currentIndexChanged[int].connect(self.onType)
        self.comboBox_Type.setCurrentIndex(0)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("pressed()"), self.create)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", 'PumpBlowerWB', None))
        pass

    def onEqp(self):
         
         global mypath
         global pic
         self.comboBox_Type.clear()
         self.comboBox_Series.clear()
         key=self.comboBox_Eqp.currentText()
         key2=self.comboBox_Type.currentText()
         
         if key=='Pump':
             self.comboBox_Type.show()
             self.comboBox_Series.show()
             self.comboBox_Type.addItems(Pump_type)  
             key2=self.comboBox_Type.currentText()
             mypath=key2
             pic=key2+'.png'    
         elif key=='Blower':
             self.comboBox_Type.show()
             self.comboBox_Series.show()
             self.comboBox_Type.addItems(Blower_type)  
             key2=self.comboBox_Type.currentText()
             mypath=key2
             pic=key2+'.png'     

         try:
              base=os.path.dirname(os.path.abspath(__file__))
              joined_path = os.path.join(base, "Sewage_eqp_data",mypath,pic)
              self.img.setPixmap(QtGui.QPixmap(joined_path)) 
              #print(joined_path)
         except:
              pass    
    
    def onType(self):
         global mypath
         #global key
         self.comboBox_Series.clear()
         key=self.comboBox_Eqp.currentText()
         key2=self.comboBox_Type.currentText()
         self.comboBox_Series.show()
              
         if key=='Pump':
              key2=self.comboBox_Type.currentText()
              if key2=='SpiralVortexPump':#渦巻斜流ポンプ
                self.comboBox_Series.addItems(SpiralVortexPump_series)  
                mypath=key2
                pic=key2+'.png'        
              elif key2=='SludgePump':#汚泥ポンプ
                self.comboBox_Series.addItems(SludgePump_series)  
                mypath=key2
                pic=key2+'.png'      
              elif key2=='MixedFlowPump':
                self.comboBox_Series.addItems(MixedFlowPump_series)  
                mypath=key2
                pic=key2+'.png'     
              elif key2=='CentrifugalPump':
                self.comboBox_Series.addItems(CentrifugalPump_series)  
                mypath=key2
                pic=key2+'.png'    
              elif key2=='SubmersiblePump':
                self.comboBox_Series.addItems(SubmersiblePump_series)  
                mypath=key2
                pic=key2+'.png'   
              elif key2=='UniaxialScrewPump':
                self.comboBox_Series.addItems(UniaxialScrewPump_series)  
                mypath=key2
                pic=key2+'.png'  
         elif key=='Blower':
              key2=self.comboBox_Type.currentText()
              if key2=='HelicalBlower':
                self.comboBox_Series.addItems(HelicalBlower_series)  
                mypath=key2
                pic=key2+'.png'  

         try:
             base=os.path.dirname(os.path.abspath(__file__))
             joined_path = os.path.join(base, "Sewage_eqp_data",mypath,pic)
             self.img.setPixmap(QtGui.QPixmap(joined_path))   
             #print(joined_path)
         except:
             pass             
    
    def create(self): 
            #global mypath
            #key=self.comboBox_Eqp.currentText()
            key3=self.comboBox_Series.currentText()
            key2=self.comboBox_Type.currentText()
            if key2=='SpiralVortexPump':
                fname=key2+'_'+key3+'.FCStd'  
            elif key2=='SludgePump':
                fname=key2+'_'+key3+'.FCStd'   
            elif key2=='MixedFlowPump':
                fname=key2+'_'+key3+'.FCStd'   
            elif key2=='CentrifugalPump':
                fname=key2+'_'+key3+'.FCStd'   
            elif key2=='SubmersiblePump':
                fname=key2+'_'+key3+'.FCStd'     
            elif key2=='UniaxialScrewPump':
                fname=key2+'_'+key3+'.FCStd'     
            elif key2=='HelicalBlower':
                fname=key2+'_'+key3+'.FCStd'   
            print(mypath,fname)        
            base=os.path.dirname(os.path.abspath(__file__)) 
            joined_path = os.path.join(base, 'Sewage_eqp_data',mypath,fname) 
            
            try:
                doc=App.activeDocument()
                Gui.ActiveDocument.mergeProject(joined_path)
            except:
                print(joined_path)
                Gui.ActiveDocument.mergeProject(joined_path)  

            App.ActiveDocument.recompute()  
            Gui.ActiveDocument.ActiveView.fitAll()  
         
class main():
        d = QtGui.QWidget()
        d.ui = Ui_Dialog()
        d.ui.setupUi(d)
        d.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        d.show() 
        
           