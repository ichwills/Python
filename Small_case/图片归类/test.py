import os
import sys
import time
from shutil import Error
from shutil import copystat
from shutil import copy2
#图片所处的绝对路径，其中r表示去掉python的内部转义
PicPath = r''#图片路径
CopyPath = r''#复制路径
#根据传参判断复制的目标地址是否存在如果不存在进行创建，并且执行复制操作
def copy_file(src_file,dst_dir):
    if os.path.isdir(dst_dir):
        pass
    else:
        os.makedirs(dst_dir)
    copy2(src_file,dst_dir)
 
#遍历整个图片路径底下的所有文件并获取其创建时间，根据创建时间进行复制操作
def walk_file(file_path):
    for root,dirs,files in os.walk(file_path,topdown=False):
        for name in files:
            com_name = os.path.join(root,name)
            t = os.stat(com_name)
            copy_path_str = CopyPath+"\\"+str(time.localtime(t.st_ctime).tm_year)+r"-"+str(time.localtime(t.st_ctime).tm_mon)
            copy_file(com_name,copy_path_str)
        for name in dirs:
            walk_file(name)
 
walk_file(PicPath)