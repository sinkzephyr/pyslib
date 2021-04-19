import os

def list_dir(path,list_name):
  for file in os.listdir(path):
    file_path = os.path.join(path,file)
    if os.path.isdir(file_path) is False:
      list_name.append(file_path)


def list_deep_dir(path,list_name):
  for file in os.listdir(path):
    file_path = os.path.join(path,file)
    if os.path.isdir(file_path):
      list_deep_dir(file_path, list_name)
    else:
      list_name.append(file_path)