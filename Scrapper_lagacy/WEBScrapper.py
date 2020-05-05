from requests import get
from bs4 import BeautifulSoup

def Mongscrap(url):
    try:
        res = get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        s1 = soup.find('div',{'class':'game_area_purchase_game_wrapper'})
        try:
            title= soup.find('div',{'class':'apphub_AppName'}).string
        except:
            title = 'title error'
        try:
            ss1 = s1.find('div',{'class':'discount_pct'}).string
        except:
            ss1 = 'None'
        try:
            ss2 = s1.find('div',{'class':'discount_final_price'}).string
        except:
            ss2 = s1.find('div',{'class':'game_purchase_price'}).string
            ss2 = ss2[9:]
        print('\n현재 %s의\n할인율 : %s\n가격 : %s\n'%(title,ss1,ss2))
    except:
        print('\nurl error\n')
    
    
        

    


f = open('C:/Users/ajfqh/Desktop/URLs.txt','r')
data = f.readlines()
f.close()
for url in data:
    Mongscrap(url)


