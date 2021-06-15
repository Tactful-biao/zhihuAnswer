from pathlib import Path

# 文件所在目录
p = Path('/Users/xxx/Documents/zhihuAnswer/pdfBetch')

# 文件类型
files = p.glob('*.pdf')

# 创建文件夹，把文件移到文件夹内
for x in files:
    p.joinpath(x.stem).mkdir()
    x.rename(p.joinpath(x.stem).joinpath(x.name))