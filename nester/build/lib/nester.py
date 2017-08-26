"""
這是 nester.py 模組，
練習建立模組並上傳至 PyPI。
"""

def print_lol(the_list, level=0):
  """
  需傳入 清單 list，名稱為 the_list 
  """
  for each_item in the_list:
    if isinstance(each_item, list):
      print_lol(each_item, level+1)
    else:
      for tab_stop in range(level):
        print("\t", end='')
      print(each_item)
