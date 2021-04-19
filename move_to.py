'''
 删除多余子目录的脚本
 如 python move_to.py  '/Users/zaker_6/百度云同步盘/得到订阅/LR 实战/2017-10' lr
 第一个参数为要遍历的目录，第二个参数为多余子目录
'''
import sys
import os
import re
import shutil

import dir


if __name__ == '__main__':

  path = None
  sub_path = None
  if len(sys.argv) > 1:
    path = sys.argv[1]
    sub_path = sys.argv[2]
    print('2nd arg:',sys.argv[1])
    print('3th arg:',sys.argv[2])
  else:
    print('no 2nd arg')

  # print(os.path.split(path))
  if os.path.isdir(path) == True and len(sub_path) > 0:
    path_list = []
    dir.list_deep_dir(path, path_list)
    print(path_list)


    for file in path_list:
      if os.path.isfile(file):
        # print("file found is file")
        file_coms = os.path.split(file)
        print(file_coms)
        if os.path.exists(file_coms[0]) == True:
          if file_coms[0].find('/'+sub_path) >= 0:
            dest = os.path.abspath(os.path.join(file_coms[0],os.path.pardir)) #re.sub('/'+sub_path, "",file_coms[0])
            print("dest:"+dest)
            shutil.move(file, os.path.join(dest,file_coms[1]))

            files = os.listdir(file_coms[0])
            if len(files) == 0 :
              os.rmdir(file_coms[0])
              print("remove dest path:"+ file_coms[0])



