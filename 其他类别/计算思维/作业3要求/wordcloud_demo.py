import jieba
import wordcloud
from matplotlib import pyplot as plt
from wordcloud import ImageColorGenerator, STOPWORDS
from PIL import Image
import numpy as np
from collections import Counter

def cloud():
    f = open("report.txt", "r", encoding="utf-8")
    t = f.read()
    f.close()

    ls = jieba.lcut(t)
    # txt = "".join(ls)
    c = Counter()
    for x in ls:
        if len(x)>1 and x != '\r\n':
            c[x] += 1
    for (k,v) in c.most_common(20):
        print('%s%s %s  %d' % ('  '*(5-len(k)), k, '*'*int(v/3), v))


    print(c)
    c = dict(c.most_common(100))
    print(c)


    img = Image.open(r'cloud.jpg')  # 打开图片
    img_array = np.array(img)  # 将图片装换为数组

    w = wordcloud.WordCloud(font_path="msyh.ttc",\
                            width=1000,height=500,\
                            background_color="white",\
                            mask=img_array
                            )

    # print(txt)
    w.generate_from_frequencies(c)
    image_colors = ImageColorGenerator(img_array)

    plt.imshow(w.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis('off')  # 横纵坐标是否显示在图上，一般要关闭
    plt.show()  # 显示图片

    filename = r'wordCloud_POM.png'
    w.to_file(filename)

if __name__ == '__main__':
    cloud()

