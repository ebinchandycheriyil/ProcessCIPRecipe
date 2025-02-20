import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('Recipe.db')

# cursor object
cursor_obj = connection_obj.cursor()



# # Creating table
# table = """ CREATE TABLE ValueList(
#             id,
#             testSP_1,
#             testSP_2
#         ); """



# table = """ALTER TABLE ValueList
#   ADD SP_1 FLOAT,
#   ADD SP_2 FLOAT,
#   ADD SP_3 FLOAT,
#
#   ;"""
i=1
# while i<100:
table =f'DELETE FROM RecipeList;'

cursor_obj.execute(table)
# table = """ INSERT INTO ValueList(
#             id, testSP_1 , testSP_2) VALUES (3, 11,22); """
# cursor_obj.execute(table)

connection_obj.commit()
i+=1


