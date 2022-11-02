#!/bin/bash
#检查端口是否被占用，如果占用输出1，如果没有被占用输入0
for port in $(seq 34210 34340)
do
    # pIDa=`/usr/sbin/lsof -i :$port|grep -v "PID" | awk '{print $2}'`
    portStatus=$(sudo lsof -i:"${port}")
    echo "$portStatus"
    if [ "$portStatus" = "" ];
    then
        echo "$port""端口可用"
        systemctl start docker #!启动docker服务
#          docker load -i test.tar #!导入镜像
        docker run -itd --name marking_"$port" -p "$port":34340 --gpus all --shm-size 20g --privileged=false ubuntu /bin/bash
        systemctl daemon-reload
        echo "启动成功"
        echo marking_"$port"
        


        break

    else
        echo "$port""端口不可用"

    fi
done


# docker -v | grep "version"
# if [ $? -eq 0 ] ;then
# 	 systemctl start docker #!启动docker服务
# 	#  docker load -i test.tar #!导入镜像
# 	 docker run -it --name aaaccc -p $port ubuntu /bin/bash    #!启动容器
# 	 systemctl daemon-reload

# 	 docker logs -f -t test
# else
# 	echo " docker is not exist"
# fi

