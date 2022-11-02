
import sqlite3

def sql_init():
    conn = sqlite3.connect('mission.db')
    c =conn.cursor()
    c.execute("create table marking_list6(ID INTEGER PRIMARY KEY,PORT STR,NAME STR,STATUS STR)")
    # a=3
    # c.execute("insert into marking_list(ID,NAME,TYPE) values (%d,'c',3)"%(a))
    # conn.commit()
    # c.execute("select ID,name,type from marking_list")
    # for row in c:
    #     print('ID = '+str(row[0]))
    #     print("NAME = "+row[1])
    #     print("SALARY = "+str(row[2])+"\n")

    c.close()


