
#!/bin/bash
#检查8080端口是否被占用，如果占用输出1，如果没有被占用输入0
port=34230
pIDa=`sudo lsof -i:$port`
echo $pIDa
if [ "$pIDa" == "" ];
then
   echo "0"
else
   echo "1"
fi