from requests import get
from bs4 import BeautifulSoup
yeah = []
yay = []
def Mongscrap(url):
    global yeah
    try:
        res = get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        s1 = soup.find('div',{'class':'game_area_purchase_game_wrapper'})
        try:
            title = soup.find('div',{'class':'apphub_AppName'}).string
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
            ss2 = ss2[11:-6]
        yeah.append('%s^%s^%s'%(title,ss1,ss2))
        #print('%s^%s^%s'%(title,ss1,ss2))
        #print(yeah)
    except:
        yeah.append('ERROR')
        #print('\nerror\n')

f = open('C:/Users/ajfqh/Desktop/URLs.txt','r')
data = f.readlines()
f.close()

for x in range(len(data)):
    Mongscrap(data[x])
    yeah[x] = yeah[x].split('^')
#print('\n\n')
#print(yeah)
    if yeah[x][1] != 'None':
        if int(yeah[x][1].rstrip('%'))<-70:
            yay.append('yay')
        print(yay)
