#!/usr/bin/python
#coding:utf8
import   os
s=raw_input("请输入一个文件夹:")
for  path,dirs,files in    os.walk(s):
       for  files in files:
                print (os.path.join(path,files))


#原型为：os.walk(top, topdown=True, onerror=None, followlinks=False)
#我们一般只使用第一个参数。（topdown指明遍历的顺序）
#该方法对于每个目录返回一个三元组，(dirpath, dirnames, filenames)。第一个是路径，第二个是路径下面的目录，第三个是路径下面的非目录（对于windows来说也就是文件）。请看示例#