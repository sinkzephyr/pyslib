import sys
import os

import files

if __name__ == '__main__':
  if len(sys.argv) < 1:
    print('no first arg')
    exit()

  fir_arg = sys.argv[1]

  snd_arg = None
  if len(sys.argv) > 2:
    snd_arg = sys.argv[2]

  thd_arg = None
  if len(sys.argv) > 3:
    thd_arg = sys.argv[3]


  if snd_arg is not None and snd_arg == "file_tail" :#去掉尾巴
    if thd_arg is None:
      print('need third arg:removed string')

    files.tail(fir_arg,thd_arg)

  if snd_arg is not None and snd_arg == "file_strip" :#去掉尾巴的空格
    files.strip(fir_arg)



