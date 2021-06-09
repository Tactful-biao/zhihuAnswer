import random

random.seed(10)

# 位置码的生成
def posCode(source):
  lst = list(range(1, len(source)+1))
  random.shuffle(lst)
  pos_code = ''.join(str(x) for x in lst)

  return pos_code

# 原码加密
def changeCode(source, lst):
  res = ''.join(source[int(x) - 1] for x in lst)
  return res


if __name__ == '__main__':
  source = input('输入原码:')  #'010512'

  poscode = posCode(source)
  print(poscode)

  result = changeCode(source, poscode)
  print(result)