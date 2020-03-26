from plyer import notification
from bs4 import BeautifulSoup
import requests 
import time

def notifyMe(title,message):
    notification.notify(
    title = title,
    message = message,
    app_icon = "C:/Users/hammad/Desktop/Python Tuts/virus.ico",
    timeout = 6
    )

if __name__ == "__main__":
    pass
#notifyMe("Hammad","Corona Notifixation")
while True:
  def getData(url):
    r = requests.get(url)
    return r.text
  myHTMLData = getData('https://www.worldometers.info/coronavirus/')
  #print(myHTMLData)
  soup = BeautifulSoup(myHTMLData,'html.parser')
  #print(soup.prettify())
  myDataStr= ""
  for tr in soup.find_all('tbody')[0].find_all('tr'):
    myDataStr += tr.get_text()
  itemList =  myDataStr.split("\n\n")
  Country = ['Pakistan']
  for item in itemList[0:50]:
    DataList = item.split("\n")
    if DataList[0] in Country:
      #print(DataList)
      notiTitle = "Cases of Covid-19 in Pakistan"
      notiText = f"Total cases: {DataList[1]} \nNew Cases: {DataList[2]} \nTotal Deaths: {DataList[3]} \nRecoverd: {DataList[5]}"
      notifyMe(notiTitle,notiText)
      time.sleep(2)
  time.sleep(10)
