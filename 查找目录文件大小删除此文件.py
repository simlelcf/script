import  os
#coding:utf8
x=raw_input('请输入要查找的目录：')
size=raw_input('请输入要查找的文件的大小')

find='find '+ x +  ' -size '+ size + '  -type  f > /root/yubenliu/ybl.txt'  
os.system(find)
f=open('/root/yubenliu/ybl.txt')
c=f.readlines()
for i   in   c:
      os.system('rm -rf ' + i)
      print  i
