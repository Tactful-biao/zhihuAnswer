'''
以读读方式打开text2
以追加的方式打开text1
把text2的内容追加到text1中
'''
with open('text2.txt', 'r') as text:
  with open('text1.txt', 'a') as txt:
    txt.writelines(text.readlines())
