import jieba
import wordcloud
from matplotlib import pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
from PIL import Image
import numpy as np
from collections import Counter
from random import randint

def random_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):
    h  = randint(0, 20)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(randint(60, 120)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)

def cloud():
    f = open("article.txt", "r", encoding="utf-8")
    t = f.read()
    f.close()

    ls = jieba.lcut(t)
    txt = "".join(ls)

    img = Image.open(r'cloud.jpg')  # 打开图片
    img_array = np.array(img)  # 将图片装换为数组

    w = wordcloud.WordCloud(font_path="SourceHanSerifSC-Regular.otf",
                            width=2000,height=1000,
                            background_color="white",
                            mask=img_array
                            )

    # print(txt)
    # w.generate_from_text(txt)
    w.generate_from_frequencies(dict(Counter([v for v in ls if len(v) > 2])))
    image_colors = ImageColorGenerator(img_array)
    

    plt.imshow(w.recolor(color_func=random_color_func), interpolation="bilinear")
    plt.axis('off')  # 横纵坐标是否显示在图上，一般要关闭
    plt.show()  # 显示图片
    #
    filename = r'wordCloud_POM.png'
    w.to_file(filename)


if __name__ == '__main__':
    cloud()

