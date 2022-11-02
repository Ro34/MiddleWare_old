import paramiko,time
 
# 创建SSH对象
ssh = paramiko.SSHClient()
 
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
# 连接服务器
ssh.connect(hostname='xx.xx.xx.xx', port=22, username='', password='')
 
 
# 执行命令
stdin, stdout, stderr = ssh.exec_command('python /xx/xx/xx.py')
 
# 获取命令结果
result = stdout.read().decode('utf8')
print(result)  # 如果有输出的话
 
# 关闭连接
ssh.close()