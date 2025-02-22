from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import (QMainWindow, QApplication,QInputDialog,QMessageBox,QStyle)
from PyQt6.uic import loadUi
from SQLite import sqLiteConnection
from PLC import plcComm
from const import  variableList
import sys

from TableView import IOFieldManager


class MainUI(QMainWindow):
    def __init__(self):

        # Variables
        self.CurrentID=0
        self.CurrentRecipeID = 0
        self.currentRecipeList=[[],[]]


        #Initialise screen
        super(MainUI, self).__init__()
        loadUi("CIPRecepie.ui", self)
        self.SqLite = sqLiteConnection()

        self.cktSelection = "A"

        # Add logo
        labelGoose = self.Logo1View
        pixmap1 = QPixmap('assets/goose.png')
        pixmap1 = pixmap1.scaled(200, 50)
        labelGoose.setPixmap(pixmap1)

        labelLactalis = self.Logo2View
        pixmap2 = QPixmap('assets/lactalis-logo.png')
        pixmap2 = pixmap2.scaled(200, 50)
        labelLactalis.setPixmap(pixmap2)


        #On screen update event call backs
        self.pgmSelectComboBox.currentIndexChanged.connect(self.programChangeEvent)
        self.recepieSelectComboBox.currentIndexChanged.connect(self.tableUpdateEvent)

        self.NewRecipeBtn.clicked.connect(self.createRecipeEvent)
        self.DeleteRecipeBtn.clicked.connect(self.deleteRecipeEvent)
        self.loadToDeviceBtn.clicked.connect(self.loadRecipeEvent)

        self.cktASel_btn.clicked.connect(lambda : self.cktChangeEvent("A"))
        self.cktBSel_btn.clicked.connect(lambda: self.cktChangeEvent("B"))


    def programChangeEvent(self, programIndex):
        self.CurrentID=programIndex
        self.currentRecipeList = self.SqLite.getRecipeList(programIndex, self.cktSelection)
        self.recepieSelectComboBox.clear()
        self.currentRecipeList[0].insert(0, 'Select Recipe')
        self.currentRecipeList[1].insert(0, -1)
        self.recepieSelectComboBox.addItems(self.currentRecipeList[0])

    def cktChangeEvent(self, btn):
        if btn=="A" and self.cktASel_btn.isChecked() :
            self.cktSelection = "A"

        if btn=="B" and self.cktBSel_btn.isChecked():
            self.cktSelection = "B"
        self.programChangeEvent(self.pgmSelectComboBox.currentIndex())


    def tableUpdateEvent(self, recipeID):
        if recipeID !=-1 and self.currentRecipeList[1][recipeID]!=-1 :

            self.CurrentRecipeID=self.currentRecipeList[1][recipeID]
            data1,data2,addr_1,addr_2= self.SqLite.getParameterList(self.CurrentID, self.currentRecipeList[1][recipeID], self.cktSelection)
            self.PLC = plcComm()
            live1 = self.PLC.readList(addr_1)
            live2 = self.PLC.readList(addr_2)

            self.TableModel_1=IOFieldManager(data1,live1,self.scrollArea_1)
            self.TableModel_2 = IOFieldManager(data2,live2, self.scrollArea_2)
            self.TableModel_1.SqlUpdateEvent = self.valueUpdate
            self.TableModel_2.SqlUpdateEvent = self.valueUpdate
            # self.tableView.setModel(self.TableModel)
        else:
            print("table clear")

    def valueUpdate(self,colName,value, ):
        self.SqLite.upateValue(colName, value, self.CurrentRecipeID)

    def createRecipeEvent(self):
        if self.CurrentID>0:
            text, ok = QInputDialog.getText(self.groupBox_3, 'Create Recipe', 'Enter recipe name', text="New Recipe")
            if ok:
                self.SqLite.NewRecipe(text, self.CurrentID, self.cktSelection)
                self.programChangeEvent(self.CurrentID)
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("Please select mode to create recipe")
            msgBox.setWindowTitle("Mode not selected")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Close )

            returnValue = msgBox.exec()
            if returnValue == QMessageBox.StandardButton.Close:
                print('OK clicked')
    def deleteRecipeEvent(self):

        self.SqLite.removeRecipe(self.CurrentRecipeID)
        self.programChangeEvent(self.CurrentID)

    def loadRecipeEvent(self):

        self.PLC = plcComm()

        spKeys = []
        tKeys = []

        if self.pgmSelectComboBox.currentIndex() == 1:
            spKeys = [key for key in variableList.keys() if key.startswith(f"HWS{self.cktSelection}")]
            tKeys = [key for key in variableList.keys() if key.startswith(f"HWT{self.cktSelection}")]
        elif self.pgmSelectComboBox.currentIndex() == 2:
            spKeys = [key for key in variableList.keys() if key.startswith(f"LYS{self.cktSelection}")]
            tKeys = [key for key in variableList.keys() if key.startswith(f"LYT{self.cktSelection}")]
        elif self.pgmSelectComboBox.currentIndex() == 3:
            spKeys = [key for key in variableList.keys() if key.startswith(f"ACS{self.cktSelection}")]
            tKeys = [key for key in variableList.keys() if key.startswith(f"ACT{self.cktSelection}")]

        spArray = []
        tArray = []

        for spKey in spKeys:
            value = self.SqLite.readRecipeValue(variableList[spKey].dbAddr, self.CurrentRecipeID)
            spArray.append((variableList[spKey].PLCAddr, value[0][0]))

        for tKey in tKeys:
            value = self.SqLite.readRecipeValue(variableList[tKey].dbAddr, self.CurrentRecipeID)
            tArray.append((variableList[tKey].PLCAddr, value[0][0]))
        if self.cktSelection == 'A' :
            self.PLC.writeTag("Recepie_Name_A", self.recepieSelectCombox.currentText())
        elif self.cktSelection == 'B' :
            self.PLC.writeTag("Recepie_Name_B", self.recepieSelectCombox.currentText())

        self.PLC.writeList(spArray)
        self.PLC.writeList(tArray)
        self.tableUpdateEvent(self.recepieSelectComboBox.currentIndex())










# Main start event
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('macos')
    app.setWindowIcon(QIcon('assets/icon.ico'))

    ui = MainUI()
    ui.show()
    app.exec()
