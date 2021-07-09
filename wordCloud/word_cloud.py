import requests
import re
import numpy as np
from wordcloud import WordCloud
from font2pic import get_font_pic
import jieba
import cv2


def get_pic():
    url = 'http://www.akuziti.com/'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-HK;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '76',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'www.akuziti.com',
        'Origin': 'http://www.akuziti.com',
        'Pragma': 'no-cache',
        'Referer': 'http://www.akuziti.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }

    data = {
        'word': '赞',
        'fonts': '1043.ttf',
        'sizes': '400',
        'fontcolor': '#000000',
        'colors': '#FFFFFF',
    }

    content = requests.post(url, headers=headers, data=data).text

    _pic = re.search('cache/\d+\.png', content).group()

    pic_url = 'http://www.akuziti.com/' + _pic

    pic = requests.get(pic_url, headers=headers).content

    with open('fontPic/a.png', 'wb') as p:
        p.write(pic)

    mask = cv2.imdecode(np.frombuffer(pic, np.uint8), cv2.IMREAD_COLOR)

    # 剪切图片
    crop = mask[0:700, 0:600]

    return crop


def word_cloud():
    with open('text.txt', 'r') as f:
        txt = f.read()
    text = " ".join(jieba.cut(txt))
    # mask = get_pic()  # 从网络获取字体图片
    mask = get_font_pic('标')  # 自己生成字体图片

    font = 'fonts.ttc'
    wc = WordCloud(background_color='white', font_path=font, max_words=500, mask=mask)
    # wc = WordCloud(font_path=font, max_words=500, mask=mask)
    wc.generate(text)
    wc.to_file('output.png')


if __name__ == '__main__':
    word_cloud()
