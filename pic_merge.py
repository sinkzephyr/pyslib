'''
 合并图片的脚本
 如 python pic_merge.py  '/Users/zaker_6/百度云同步盘/得到订阅/script/test'
 第一个参数为要遍历的目录
'''
import os
import sys
from PIL import Image
import re

import dir

topCrop = 130
bottomCrop = 145

def rm_hide_files(list):
  for i in range(len(list)-1,-1,-1):
    file = list[i]
    if (file.endswith('jpg') or file.endswith('png')) is False:
      del list[i]

def get_file_name_and_ext(fullFile):
  if os.path.isfile is False:
    return ''
  return os.path.splitext(os.path.split(fullFile)[1])

def get_file_name(fullFile):
  return get_file_name_and_ext(fullFile)[0]

def is_first_file(file):
  name = get_file_name(file).strip()
  if name is None or len(name) == 0:
    return False

  if name.endswith("(1)"):
    return True

  if_snd_file = (re.search(r'((\(\d+\))|\d+)$', name) is not None)
  return if_snd_file == False

def is_second_file(file):
  name = get_file_name(file).strip()
  return name.endswith('(2)') or name.endswith('2')

def get_second_file_name(fileName):
  if fileName.strip().endswith('(1)'):
    return fileName.replace('(1)','(2)')
  else:
    return fileName+'2'

def crop_img(img):
  fWidth,fHeight = img.size
  return img.crop((0,topCrop,fWidth,fHeight - bottomCrop))

if __name__ == '__main__':
  path = None
  # sub_path = None`
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    print('no 2nd arg')

  if os.path.isdir(path) == True :
    path_list = []
    dir.list_deep_dir(path, path_list)
    rm_hide_files(path_list)
    toImage = None
    # tWidth,tHeight = 0, 0

    print(path_list)
    if len(path_list) > 0:
      # firstFileName = path_list[0]

      tWidth,tHeight = 0,0
      for file in path_list:
        if is_first_file(file) == False:
          print('no first file:{0}'.format(file))
          continue

        print("first file:{0}".format(file))
        file_path,tName = os.path.split(file)
        file_name,ext = get_file_name_and_ext(file)
        second_file_with_simple_num = False #如果XXX2.jpg这类的文件存在
        merge_group = []

        for i in range(1,19,1):
          num_str = str(i+1)
          next_file = file_name+num_str
          next_full_file = os.path.join(file_path,next_file+ext)
          if os.path.exists(next_full_file) == True:
            # second_file_with_simple_num = True
            merge_group.append(next_full_file)
          else:
            break

        if len(merge_group) == 0:
          for i in range(1,19,1):
            num_str = '({0})'.format( i+1)
            next_file = file_name.replace('(1)',num_str)
            next_full_file = os.path.join(file_path,next_file+ext)
            print('find next file for:{0}'.format(next_full_file))
            if os.path.exists(next_full_file) == True:
              merge_group.append(next_full_file)
            else:
              break

        if len(merge_group) == 0:
          print('cannot find next file for:{0}'.format(file))
          continue



        merge_group.insert(0, file)

        print('merge_group',merge_group)

        all_height = 0
        to_width = 0
        size_list = []
        tmode = None
        for merge_file in merge_group:
          img = Image.open(merge_file)
          tsize = img.size
          tmode = img.mode
          size_list.append(tsize)
          all_height += (tsize[1] - topCrop - bottomCrop)
          to_width = max(to_width, tsize[0])

        toImage = Image.new(tmode,(to_width,all_height))

        insert_height = 0
        for i in range(0, len(merge_group),1):
          merged_file_name = merge_group[i]
          merged_img = Image.open(merged_file_name)
          merged_img = crop_img(merged_img)

          toImage.paste(merged_img,(0,insert_height))
          # if i > 0:
          insert_height += merged_img.size[1]
        # print(file_name,ext)

        if toImage is not None:
          file_name = file_name.replace('(1)','')
          saveFileName = os.path.join(file_path,file_name+" 合"+ext)
          print(saveFileName)
          toImage.save(saveFileName,'JPEG')
        # secondFileName = get_second_file_name(file_name)
        # print(secondFileName)
        # sndFullFile = os.path.join(file_path,secondFileName+ext) #被合并的第2个文件
        # if os.path.exists(sndFullFile) == False:
        #   print('cannot find snd file:{0}'.format(sndFullFile))
        #   continue

        # firstImg =  Image.open(file)
        # firstImg = crop_img(firstImg)
        # fWidth,fHeight = firstImg.size
        # sndImg =  Image.open(sndFullFile)
        # sndImg = crop_img(sndImg)
        # sWidth,sHeight = sndImg.size
        # tWidth = max(fWidth,sWidth)
        # tHeight = fHeight + sHeight

        # toImage = Image.new(firstImg.mode,(tWidth,tHeight))
        # toImage.paste(firstImg,(0,0))
        # toImage.paste(sndImg,(0,fHeight))



