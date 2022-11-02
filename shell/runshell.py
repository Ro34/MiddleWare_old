# from imaplib import Commands

import os
import sqlite3
import subprocess
import time


def start_container():
    list = os.popen("sudo ./start_container.sh").read()
    container_name = list[-14:-1]
    # print(resout)
    print(container_name)
    return container_name


def add_info(container_name_start):
    conn = sqlite3.connect('mission.db')
    c = conn.cursor()
    c.execute("insert into marking_list6(ID,PORT,NAME,STATUS) values (NULL,?,?,'Running')",
              (container_name_start[-5:], container_name_start))
    c.close()
    conn.commit()
    print("marking mission list:")


def show_mission():
    conn = sqlite3.connect('mission.db')
    c = conn.cursor()
    c.execute("select ID,PORT,NAME,STATUS from marking_list6")
    for row in c:
        print("ID  " + str(row[0]) + '\t' + "Port:  " + str(row[1]) + '\t' + "Name:  " + str(row[2]))
    c.close()


def stop_container(con_name_to_stop):
    subprocess.call("sudo ./stop_container.sh " + con_name_to_stop, shell=True)
    print("stopped")


def delete_info(container_name_stop):
    conn = sqlite3.connect('mission.db')
    c = conn.cursor()
    c.execute("delete from marking_list6 where NAME=?", (container_name_stop,))
    conn.commit()
    c.close()


if __name__ == "__main__":
    # sql_init()

    for i in range(3):
        con_name = start_container()

        add_info(con_name)
        show_mission()
        # test delete
        if con_name == 'marking_34225':
            print("wait 3s to stop container")

            time.sleep(3)

            stop_container(con_name)
            delete_info(con_name)
