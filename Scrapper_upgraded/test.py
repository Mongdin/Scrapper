import time
import random
from wordcloud import WordCloud
import os
from urllib.request import urlretrieve
from tqdm import tqdm
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
!pip install selenium
!apt update
!apt install chromium-chromedriver
!cp / usr/lib/chromium-browser/chromedriver / usr/bin
sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver', options=chrome_options)
print('done')


url = 'https://store.steampowered.com/search/?specials=1&filter=topsellers'
wd.get(url)
body = wd.find_element_by_tag_name("body")
for i in range(5):  # �� 100���� ���Ӹ��
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(random.random())
html_doc = wd.page_source

bs = BeautifulSoup(html_doc, 'html.parser')

soup = bs.find(name='div', id='search_resultsRows')

title = [i.find('span').get_text() for i in soup.find_all(
    'div', class_='col search_name ellipsis')]  # ���� ����
print(title)

discount = [i.find('span').get_text() for i in soup.find_all(
    'div', class_='col search_discount responsive_secondrow')]  # ������
print(discount)

price = [i.get_text().strip().split('$')[2] for i in soup.find_all(
    'div', class_='col search_price discounted responsive_secondrow')]  # ���ε� ����
print(price)
textDir = "/content/drive/My Drive/Colab Notebooks/20161661�ֵ���"
if not(os.path.isdir(textDir)):
    os.makedirs(textDir)
with open(textDir+'/text'+'.txt', 'w') as outf:  # txt���Ϸ� ����,������,���� ����
    for x in range(len(title)):
        outf.write(title[x]+' '+discount[x]+' '+price[x]+'\n')

# ���߿� ������ ���ϸ����� ����Ϸ��µ� �����̸��� '/'�� ���ԵǾ� �����߻� -> '&'���� ��ü
for x in range(len(title)):
    if title[x].count('/'):
        # print(title[x])
        title[x] = title[x].replace('/', '&')
        # print(title[x])

a_tags = soup.find_all('div', {'class': 'col search_capsule'})
# print(a_tags)
# print(len(a_tags))

src_urls = []
for tag in tqdm(a_tags):
    src_urls.append(tag.find('img').get('src'))

# print(src_urls)
# print(len(src_urls))


# ������ġ�� �Ϲ����� ��η� �Է��س����ϴ�
imageDir = "/content/drive/My Drive/Colab Notebooks/20161661�ֵ���/images"
if not (os.path.isdir(imageDir)):
    os.makedirs(imageDir)
for i, src in tqdm(enumerate(src_urls)):
    urlretrieve(src, imageDir+"/"+title[i]+' ' +
                str(discount[i])+' '+str(price[i])+".jpg")


!pip install wordcloud - -upgrade

imageDir = "/content/drive/My Drive/Colab Notebooks/20161661�ֵ���/wordcloud"

if not(os.path.isdir(imageDir)):
    os.makedirs(imageDir)

wordcloud = WordCloud().generate(' '.join(title))
wordcloud.to_file(imageDir+'/titlecloud.jpg')
wordcloud = WordCloud(include_numbers=True).generate(' '.join(discount))
wordcloud.to_file(imageDir+'/discountcloud.jpg')

