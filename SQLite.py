import sqlite3
from os.path import commonpath

import pandas as pd
from const import  variableList


class sqLiteConnection():
    def __init__(self):
        self.con = sqlite3.connect("Recipe.db")

    def getRecipeList(self, Index, ckt):
        command = f"SELECT Name, Id from RecipeList WHERE Master ={Index} AND CKT = '{ckt}' ORDER BY Id"
        cursor = self.con.cursor()
        cursor.execute(command)
        records = cursor.fetchall()
        ret = [[], []]
        ret[0] = [item[0] for item in records]
        ret[1] = [item[1] for item in records]
        return ret
    def getParameterList(self,selection, Index, ckt):
        spKeys = []
        tKeys = []
        title_1=[]
        title_2=[]
        if selection == 1:
            spKeys = [key for key in variableList.keys() if key.startswith(f"HWS{ckt}")]
            tKeys = [key for key in variableList.keys() if key.startswith(f"HWT{ckt}")]
        elif selection == 2:
            spKeys = [key for key in variableList.keys() if key.startswith(f"LYS{ckt}")]
            tKeys = [key for key in variableList.keys() if key.startswith(f"LYT{ckt}")]
        elif selection == 3:
            spKeys = [key for key in variableList.keys() if key.startswith(f"ACS{ckt}")]
            tKeys = [key for key in variableList.keys() if key.startswith(f"ACT{ckt}")]

        command = "SELECT "
        for spKey in spKeys:
            command = f"{command} {variableList[spKey].dbAddr},"
            title_1.append(variableList[spKey].description)
        command = command[:-1]
        for tKey in tKeys:
            command = f"{command} {variableList[tKey].dbAddr},"
            title_2.append(variableList[tKey].description)
        command = f"{command[:-1]} from ValueList WHERE id = {Index}"


        cursor = self.con.cursor()
        cursor.execute(command)
        records = cursor.fetchall()
        val_1 = []
        val_2 = []
        addr_1=[]
        addr_2=[]
        if len(records)>0:
            for i in range(len(spKeys)):
                val_1.append([variableList[spKeys[i]].datatype, records[0][i],variableList[spKeys[i]].unit, variableList[spKeys[i]].dbAddr ])
                addr_1.append(variableList[spKeys[i]].PLCAddr)

            for j in range(len(tKeys)):
                i = j+len(spKeys)-1
                val_2.append([variableList[tKeys[j]].datatype, records[0][i], variableList[tKeys[j]].unit, variableList[tKeys[j]].dbAddr])
                addr_2.append(variableList[tKeys[j]].PLCAddr)


            data_1 = pd.DataFrame(val_1, columns=['Datatypes','Setpoint' , "Unit", "DB"], index=title_1)

            data_2 = pd.DataFrame(val_2, columns=['Datatypes', 'Setpoint', "Unit", "DB"], index=title_2)

            print(val_2)
            return data_1,data_2,addr_1,addr_2
        else:
            # print(command)
            return 0,0
    def upateValue(self,colName, value, id):
        tmpColName =colName
        command =f'SELECT * from ValueList WHERE id ={id} '
        cursor = self.con.cursor()
        cursor.execute(command)
        if len(cursor.fetchall())>0:
            command = f'UPDATE ValueList SET {tmpColName} = {value} WHERE id ={id}'

        else:
            command = f"INSERT INTO ValueList( id, {tmpColName} ) VALUES ({id}, {value}); """
        cursor = self.con.cursor()
        try:
            # print(command)
            cursor.execute(command)
            self.con.commit()
        except:
            pass
    def removeRecipe(self,id ):
        command_1 =f'DELETE FROM RecipeList WHERE id={id}'
        command_2 = f'DELETE FROM ValueList WHERE id={id}'
        cursor = self.con.cursor()
        cursor.execute(command_1)
        cursor.execute(command_2)
        self.con.commit()

    def NewRecipe(self,Name,master, ckt):
        command_1 = f"INSERT INTO RecipeList( Name, Master, ckt ) VALUES ('{Name}', {master}, '{ckt}'); """
        cursor = self.con.cursor()
        cursor.execute(command_1)
        self.con.commit()
        command_2=f"SELECT id from RecipeList WHERE Name ='{Name}'"
        cursor.execute(command_2)
        newID=cursor.fetchall()
        command_3 = f"INSERT INTO ValueList( id ) VALUES ({newID[0][0]}) """
        cursor.execute(command_3)
        self.con.commit()


    def readRecipeValue(self,col,id):
        command = f"SELECT {col} from valueList where id = {id}"
        cursor = self.con.cursor()
        # print(command)
        cursor.execute(command)
        return cursor.fetchall()


