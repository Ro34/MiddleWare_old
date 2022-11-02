#！/bin/bash
# container_status=$(docker inspect --netstat -ap | grep 8080 --format={{.NetworkSettings.Ports}}  ${1})
container_status=`docker inspect --format={{.NetworkSettings.Ports}}  ${1}`
echo "$container_status"
if  [ "$container_status" = "" ];
then
        echo "此容器不存在"
else
        echo "stopping"
        docker stop $1
        #sleep 10
        echo "stopped"
        docker rm -f  $1
        echo "removed"
fi