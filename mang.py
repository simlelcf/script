
#-*- coding: utf-8 -*-
#!/usr/bin/python 
import paramiko
import threading
from time import sleep


def ssh2(ip,username,passwd,cmd):
    try:
	    
        ssh = paramiko.SSHClient()
        print('正在登陆各台服务器')
        print ('%s\tOK\n'%(ip))
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
#           stdin.write("Y")   #简单交互，输入 ‘Y’ 
            out = stdout.readlines()
            #print (stdout)
            #屏幕输出
            for o in out:
                print (o),
        #print ('%s\tOK\n '%(ip))
        
        
        ssh.close()
    except :
         print ('%s\tError 不能正常连接这台\n'%(ip))
			  
if __name__=='__main__':
    cmd=[]  
    username = "root"  
    passwd = "zxsoft0#"   
    print ("测试环境的服务有......")
    ip=['192.168.202.102','192.168.202.103','192.168.202.101','192.168.202.11','192.168.202.12','192.168.202.13']
    for i  in  ip:
      print (i)
      
    while 1:
      y=input('如果你想继续添加多条命令请输入yes,如果是其他则退去:')
      if  y=='yes':
       x=input('请输入你要批量执行的命令:')
       cmd.append(x)
      else:
        break
    #你要执行的命令列表
    print  ('如果命令必须是手动结束，所以在执行脚本一段时间后，如果想停止攻击，重新执行脚本输入命令  killall +命令 ')	  
    for i  in  ip:
      
     
      a=threading.Thread(target=ssh2,args=(i,username,passwd,cmd))
      a.start()
      