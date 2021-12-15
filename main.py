from bs4 import BeautifulSoup
import requests
from time import sleep
import smtplib
import lxml
import os

MAIL_PROVIDER = os.environ.get("MAIL_PROVIDER")
FROM_EMAIL = os.environ.get("FROM_EMAIL")
PW = os.environ.get("PW")
TO_EMAIL = os.environ.get("TO_EMAIL")

HTTP_HEADERS ={
    "Accept-Language": "en-US,en;q=0.9,de;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
}

URL = "https://www.amazon.com/Apple-MacBook-16-inch-10%E2%80%91core-16%E2%80%91core/dp/B09JQKBQSB/ref=sr_1_4?keywords=mac+book+pro&qid=1639521572&sr=8-4"


def track_price():
    sleep(30)
    response = requests.get(url=URL, headers=HTTP_HEADERS)
    soup = BeautifulSoup(response.text, "lxml")
    price = soup.find(name="span", class_="a-offscreen").getText()
    price = price.replace("$", "").replace(",", "")
    price = float(price)
    desired_price = float(price * 0.75)

    if price <= desired_price:
        with smtplib.SMTP(MAIL_PROVIDER) as connection:
            connection.starttls()
            connection.login(FROM_EMAIL, PW)
            connection.sendmail(
                from_addr=FROM_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Price Alert, Act Quick!\n\n An item you've been watching is now available for {price}! See it here: "
                    f"{URL}")

while True:
    track_price()