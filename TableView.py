import datetime

from PyQt6.QtCore import QAbstractTableModel, Qt,QModelIndex,QTime
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout,QGridLayout, QWidget, QScrollArea, QLabel, QLineEdit,QTimeEdit, QSpacerItem,QSizePolicy


import  pandas as pd

import math

class IOFieldManager:
    def __init__(self, df: pd.DataFrame,liveList:list, scroll_view: QScrollArea):
        self.df = df
        self.scroll_view = scroll_view
        self.callbacks = []
        self.liveList = liveList
        self.setup_ui()
        self.SqlUpdateEvent = None

    def setup_ui(self):
        container = QWidget()


        layout = QGridLayout(container)
        titles = ["Description", "Recipe Value"," ", "Live Value"]
        for col, title in enumerate(titles):
            layout.addWidget(QLabel(title), 0, col)

        rowNo=1

        layout.setRowMinimumHeight(rowNo, 30)
        layout.setRowStretch(rowNo, 0)

        recipeValHLayout = QHBoxLayout()
        liveValueHLayout = QHBoxLayout()
        layout.addLayout(recipeValHLayout, rowNo, 1)
        layout.addLayout(liveValueHLayout, rowNo, 3)
        value = 0
        label = QLabel(f"{""} :")
        label.setFixedWidth(300)
        label.setFixedHeight(0)


        io_field = QLineEdit(str(value))
        # io_field.textChanged.connect(lambda val, idx=index, col=value: self.handle_val_change(idx, col, val))
        io_field.setFixedWidth(150)
        io_field.setFixedHeight(0)

        layout.addWidget(label, rowNo, 0)
        recipeValHLayout.addWidget(io_field)
        unitLabel = QLabel(f"")
        unitLabel.setFixedHeight(0)
        recipeValHLayout.addWidget(unitLabel)

        io_field_live = QLineEdit('-')
        io_field_live.setFixedWidth(150)
        io_field_live.setFixedHeight(0)

        liveValueHLayout.addWidget(io_field_live)
        liveValueHLayout.addWidget(unitLabel)




        i = 0
        for index, row in self.df.iterrows():
            layout.setRowMinimumHeight(rowNo, 30)
            layout.setRowStretch(rowNo, 0)

            recipeValHLayout = QHBoxLayout()
            liveValueHLayout = QHBoxLayout()
            layout.addLayout(recipeValHLayout,rowNo,1)
            layout.addLayout(liveValueHLayout, rowNo, 3)
            value = row.iloc[1]
            label = QLabel(f"{index} :")
            label.setFixedWidth(300)
            label.setFixedHeight(30)
            if row.iloc[0]=='INT':

                io_field = QLineEdit(str(value))
                io_field.textChanged.connect(lambda val, idx=row.iloc[3], col=value: self.handle_val_change(idx, col, val))
                io_field.setFixedWidth(150)
                io_field.setFixedHeight(30)
                layout.addWidget(label,rowNo,0)
                recipeValHLayout.addWidget(io_field)
                unitLabel = QLabel(f" {row.iloc[2]}")
                unitLabel.setFixedHeight(30)
                recipeValHLayout.addWidget(unitLabel)
                if type(self.liveList) ==str:
                    io_field_live = QLineEdit(self.liveList)
                else:
                    io_field_live = QLineEdit(str(round(self.liveList[i],1)))
                i+=1
                io_field_live.setFixedWidth(150)
                io_field_live.setFixedHeight(30)
                io_field_live.setReadOnly(True)


                liveValueHLayout.addWidget(io_field_live)
                liveValueHLayout.addWidget(unitLabel)

            if row.iloc[0]=='Time':
                if value==None : value=0
                if  value!=None and math.isnan(value):
                    value=0
                m = int(value / 60)
                s = int(value % 60)
                h=int(m / 60)
                m=int(m % 60)
                io_field = QTimeEdit(QTime(h,m,s))
                io_field.setDisplayFormat('HH : mm : ss')
                # print(row.iloc[3])
                io_field.timeChanged.connect(lambda val, idx=row.iloc[3]: self.handle_time_change(idx, val))
                io_field.setFixedWidth(150)
                io_field.setFixedHeight(30)
                layout.addWidget(label,rowNo, 0)
                recipeValHLayout.addWidget(io_field)
                unitLabel = QLabel(f" {row.iloc[2]}")
                unitLabel.setFixedHeight(30)
                recipeValHLayout.addWidget(unitLabel)
                val =0
                if type(self.liveList) ==str:
                    val= 0
                else:
                    val  = self.liveList[i]
                m = int(val/ 60)
                s = int(val % 60)
                h = int(m / 60)
                m = int(m % 60)
                i+=1
                io_field_live = QTimeEdit(QTime(h,m,s))
                io_field_live.setDisplayFormat('HH : mm : ss')
                io_field_live.setFixedWidth(150)
                io_field_live.setFixedHeight(30)
                io_field_live.setReadOnly(True)

                liveValueHLayout.addWidget(io_field_live)
                liveValueHLayout.addWidget(unitLabel)

            rowNo+=1


        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(spacer,rowNo,0)

        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        layout.addItem(spacer, rowNo, 2)

        self.scroll_view.setWidget(container)
        self.scroll_view.setWidgetResizable(True)


    def handle_val_change(self, index, column, value):
        self.SqlUpdateEvent(index,value)

    def handle_time_change(self, index,val ):
        val:QTime = val
        value = val.hour()*3600 +val.minute()*60 + val.second()
        # print(index)
        self.SqlUpdateEvent(index,value )


    def clear_ui(self):
        for i in reversed(range(self.scroll_view.widget().layout().count())):
            widget = self.scroll_view.widget().layout().itemAt(i).widget()
            widget.setParent(None)