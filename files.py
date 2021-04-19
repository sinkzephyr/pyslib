import os
import sys

import dir

def tail(path,ext):
  files_list = []
  dir.list_dir(path,files_list)
  if len(files_list) == 0:
    print("empty path")
    exit()

  for file in files_list:
    dest = file.replace(ext , '')

    if dest == file:
      continue

    print('dest:'+dest)
    os.rename(file, dest)

def strip(path):
  files_list = []
  dir.list_dir(path,files_list)
  if len(files_list) == 0:
    print("empty path")
    exit()

  for file in files_list:
    file_coms = os.path.splitext(os.path.split(file)[1])

    dest = file_coms[0].strip()

    if dest == file_coms[0]:
      continue

    dest = os.path.join(path,dest+file_coms[1])

    print('dest:'+dest)
    os.rename(file, dest)

