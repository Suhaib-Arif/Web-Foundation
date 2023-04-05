import requests
from bs4 import BeautifulSoup
import os

Flipkart_url=os.environ["AMAZON_ENDPOINT"]

response=requests.get(url=Flipkart_url)
response.raise_for_status()

soup=BeautifulSoup(response.text, "html.parser")

price = soup.select_one(selector="._30jeq3").text

price = int(price.replace("₹", "").replace(",", ""))

budget= 45000

telegram_bot_key=os.environ["TELEGRAM_KEY"]
user_id=os.environ["USER_ID"]

if price <= budget:
    parameters={
        "chat_id":user_id,
        "text":f"ALERT\n\n"
               f"The item found at a low low "
               f"price of {price} on flipkart"
    }
    sendMessage=requests.post(url=f"https://api.telegram.org/bot{telegram_bot_key}/sendMessage",params=parameters)



