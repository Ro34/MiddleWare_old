import multiprocessing as mp
import sqlite3
from concurrent.futures import ThreadPoolExecutor
import threading

import requests
import json
import Judge
from Judge import aliyun_env
from Judge import judger
from Judge import AliyunCredentialsProvider2
from Judge.Operations.Services_.MissionInfo import init_list

from Judge.Operations.toPlatform import Heartbeat
import time
import API
from Judge.Operations.toPlatform.ReportProgress import report_progress
from Judge.Operations.toServer.Progress import progress_trans
from shell import runshell


############## 直接实例化 ############
def init_sql():
    conn = sqlite3.connect('mission.db')
    c = conn.cursor()
    c.execute(
        "create table if not exists training_list(ID INTEGER PRIMARY KEY,TASKID INT,MISSIONTYPE STR,PLATFORMCONTEXT STR,SERVERCONTEXT STR,PID STR,PROGRESS INT)")
    c.execute(
        "create table if not exists marking_list(ID INTEGER PRIMARY KEY,TASKID INT,MISSIONTYPE STR,PLATFORMCONTEXT STR,SERVERCONTEXT STR,CONTAINERNAME STR)")
    c.close()


def fun1_API():
    API.run_api()


def fun2_heartbeat():
    Heartbeat.run_heartbeat()


def fun3_judger():
    Judge.judger.run_judger()


def fun4_progress():
    print("ok")
    while True:
        print("++++++++进度++++++++++")
        res = requests.get(url='http://172.18.60.191:8006/progress/get_progress')
        # if res.status_code == 200:
        #     break
        data = res.json()
        print(res.json())
        time.sleep(0.5)
        # server_pid = res.json()[3]
        if res.status_code == 200:
            # data = json.loads(res.content)
            print(data)
            pid = data[0]
            mission_progress = data[1]
            # print(type(data))
            # mission_progress = data.get('progress')
            # total_epoch = max(data['epoch'], data['total_epoch'])
            # epoch = min(data['epoch'], data['total_epoch'])
            # context = data['serverContext']

            # print("mission_progress" + str(mission_progress))
            # print("total_epoch" + str(total_epoch))
            # print("epoch" + str(epoch))
            # print(context)
            serverContext = str(data[4])
            epoch = data[2]
            total_epoch = data[3]
            print(serverContext)

            conn = sqlite3.connect('mission.db')
            c = conn.cursor()
            #查找上下文
            #更新PID
            c.execute("UPDATE training_list SET PID =? WHERE SERVERCONTEXT=?", (pid,serverContext,))
            c.execute("SELECT PLATFORMCONTEXT FROM training_list WHERE SERVERCONTEXT=?",(serverContext,))

            # print(type(a))
            # ccc = a['PLATFORMCONTEXT']
            # print(ccc)
            platformContext = str(c.fetchone())[2:-3]
            print(platformContext)

            # 回报进度
            report_progress(platformContext, epoch, total_epoch, mission_progress)
            # time.sleep(5)


# def fun4_progress():
#     # 持续get_progress
#     time.sleep(5)
#     progress_trans()
#
# def fun5_stop_marking():
#     while True:
#         res = requests.get(url='http://139.196.192.142/marking_mission/get_stop_mission')
#         if res is not None:
#             runshell.stop_container(res)


def main():
    # pool = ThreadPoolExecutor(max_workers=2)
    # feature1 = pool.submit(fun1())
    # feature2 = pool.submit(fun2())
    # init_list()

    init_sql()

    # p1_api = mp.Process(target=fun1_API)
    # p1_api.start()

    # p2_heartbeat = mp.Process(target=fun2_heartbeat)
    # p2_heartbeat.start()

    p3_judger = mp.Process(target=fun3_judger)
    p3_judger.start()
    # time.sleep(5)
    # p4_progress = mp.Process(target=fun4_progress)
    # p4_progress.start()


############ 类封装 #############

# class MyProcess(mp.Process):
#     def __init__(self, interval):
#         mp.Process.__init__(self)

#     # 需要重载的函数
#     def run(self):
#         print('I'm running)

# p = MyProcess(1)
# p.start()

#################################

# p.terminal() # 主动结束进程
# p.join() #让主进程等待子进程结束


# # 一些常用的属性
# p.pid #获得进程的id号
# p.name #获得进程名
# p.is_alive() #判断进程是否还存活
# p.daemon = True #设置进程随主进程一起结束

# mp.active_children() #获得当前进程的所有子进程
# mp.current_process() #返回正在运行的进程
# os.getpid() #获得当前进程的pid

if __name__ == "__main__":
    main()
