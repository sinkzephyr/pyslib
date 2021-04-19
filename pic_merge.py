'''
 合并图片的脚本
 如 python pic_merge.py  '/Users/zaker_6/百度云同步盘/得到订阅/script/test'
 第一个参数为要遍历的目录
'''
import os
import sys
from PIL import Image

import dir


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
  topCrop = 130
  bottomCrop = 145
  return img.crop((0,topCrop,fWidth,fHeight - topCrop - bottomCrop))

if __name__ == '__main__':
  path = None
  # sub_path = None
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
      firstFileName = path_list[0]

      tWidth,tHeight = 0,0
      for file in path_list:
        if is_second_file(file):
          continue

        filePath,tName = os.path.split(file)
        fileName,ext = get_file_name_and_ext(file)
        print(fileName,ext)
        secondFileName = get_second_file_name(fileName)
        print(secondFileName)
        sndFullFile = os.path.join(filePath,secondFileName+ext) #被合并的第2个文件
        if os.path.exists(sndFullFile) == False:
          print('cannot find snd file:{0}'.format(sndFullFile))
          continue

        firstImg =  Image.open(file)
        firstImg = crop_img(firstImg)
        fWidth,fHeight = firstImg.size
        sndImg =  Image.open(sndFullFile)
        sndImg = crop_img(sndImg)
        sWidth,sHeight = sndImg.size
        tWidth = max(fWidth,sWidth)
        tHeight = fHeight + sHeight

        toImage = Image.new(firstImg.mode,(tWidth,tHeight))
        toImage.paste(firstImg,(0,0))
        toImage.paste(sndImg,(0,fHeight))

        if toImage is not None:
          fileName = fileName.replace('(1)','')
          saveFileName = os.path.join(filePath,fileName+" 合"+ext)
          print(saveFileName)
          toImage.save(saveFileName,'JPEG')

