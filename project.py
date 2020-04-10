import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.flipkart.com/sajni-creations-back-cover-samsung-galaxy-a50/p/itmffukzx4jqqwfj?pid=ACCFFUGTRGAMAK34&lid=LSTACCFFUGTRGAMAK34H6K8VX&marketplace=FLIPKART&srno=s_1_5&otracker=AS_QueryStore_HistoryAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_5_na_na_na&fm=SEARCH&iid=ca143bad-676a-42af-889b-3a515b12a08b.ACCFFUGTRGAMAK34.SEARCH&ppt=sp&ppn=sp&ssid=hqroddp5wg0000001586521915553&qH=dbe1c09191ad45b6'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

page = requests.get(URL,headers=headers)

soup = BeautifulSoup(page.content,'html.parser')
def check_price(req_price):
    price = soup.find(class_="_1vC4OE _3qQ9m1").get_text()
    convert_price = float(price[1:])
    if(convert_price<req_price):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('newturn@gmail.com','mypassword')
    subject = "your stuff is available at right price"
    body = "link of that product is https://www.flipkart.com/sajni-creations-back-cover-samsung-galaxy-a50/p/itmffukzx4jqqwfj?pid=ACCFFUGTRGAMAK34&lid=LSTACCFFUGTRGAMAK34H6K8VX&marketplace=FLIPKART&srno=s_1_5&otracker=AS_QueryStore_HistoryAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_5_na_na_na&fm=SEARCH&iid=ca143bad-676a-42af-889b-3a515b12a08b.ACCFFUGTRGAMAK34.SEARCH&ppt=sp&ppn=sp&ssid=hqroddp5wg0000001586521915553&qH=dbe1c09191ad45b6"

    mail = f"Subject: {subject}\n\n\n{body}"

    server.sendmail{
        'newturn@gmail.com'
        'hackerashish25@gmail.com'
    }
    print('work done')
    server.quit()


