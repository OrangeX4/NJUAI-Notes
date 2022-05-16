import requests
from time import sleep
from bs4 import BeautifulSoup

def content(i: int):
    url = "https://www.dati56.com/post/13659.html?ipage=" + str(i)
    sleep(1)
    content = requests.get(url).content.decode("utf-8")
    soup = BeautifulSoup(content, "html.parser")
    text = soup.find('div', class_='content').get_text(separator="\n")
    p_nums = set([str(num) for num in range(1, 34)])
    text = '\n'.join((line for line in text.split('\n') if line.strip() != '' and line not in p_nums))
    return text

with open('output.txt', 'w', encoding='utf-8') as f:
    for i in range(1, 34):
        f.write(content(i) + '\n')