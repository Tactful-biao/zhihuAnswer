'''
  隐藏号码中的后四位
'''
n = input('请输入电话号码: ').strip()
if n.isdigit():
  if (len(n) == 8 and (n.startswith('6') or n.startswith('8'))) or (len(n) == 11 and (n.startswith('13') or n.startswith('18'))):
    print(n[:-4]+'*'*4)
  else:
    print('输入有误!')
else:
  print('输入有误!')