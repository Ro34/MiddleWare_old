#!  /user/bin/bash
containerNames="ssdb rabbit "
function GetContainerStatus(){
	containerExist=$(sudo docker ps -a |grep -i $1 -c)
	if [  $containerExist != 0 ] ; 
		then
			pid=$(sudo docker stats --format "{{.PIDs}}" --no-stream $1)
		if [ $pid -eq 0 ];
			then				
				return  0
			else				
				return  1
		fi
	else
		
		return 2	
	fi
}

function startContainer(){
	sudo docker restart  $1
}


for containerName in $containerNames
	do
		for((i=1; i<=3; i++))
	do
		$(GetContainerStatus $containerName)
		statues=$?
	if [ $statues -eq 1 ];
		then
			echo -e  "\033[31m  the container named  $containerName  is started    \033[0m" 
			break
	fi
	if [ $statues -eq 2 ];
		then
			echo -e  "\033[31m container which named  $containerName  is not exit    \033[0m"				
			break
	fi
	if [  $statues -eq 0 ] ;
		then
			echo -e  "\033[33m container  $containerName  is preparing to start ......  \033[0m" 
			startContainer $containerName &> /dev/null
			$(GetContainerStatus $containerName)
			varifyStatus=$?
				if [ $varifyStatus -eq 1  ];
					then
						echo -e  "\033[32m  container  $containerName started success   \033[0m"
						break
					else
						echo -e  "\033[33m   container  $containerName  retry start......  \033[0m"
						$(startContainer $containerName)
				fi
	fi
	done
done

