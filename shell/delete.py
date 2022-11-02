import sqlite3

def delete_info(a):
    conn = sqlite3.connect('mission.db')
    c = conn.cursor()
    c.execute("delete from marking_list6 where NAME=?",(a,))
    conn.commit()
    c.close()


def delete_all_info():
    conn = sqlite3.connect('mission.db')
    c = conn.cursor()
    c.execute("delete from marking_list6")
    conn.commit()
    c.close()

def delete_table():
    conn = sqlite3.connect('mission.db')
    c = conn.cursor()
    c.execute("drop table marking_list4")
    conn.commit()
    c.close()

# a= 'marking_34210'
# delete_info(a)


delete_all_info()


# delete_table()