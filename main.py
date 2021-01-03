import requests
from bs4 import BeautifulSoup

info = requests.get(
    "https://hyperxgaming.ca/collections/gaming-headsets/products/hyperx-cloud-ii-wired-gaming-headset?variant="
    "36496713482399"
)

soup = BeautifulSoup(info.text, "html.parser")

description = soup.find(class_="product-description rte").text
print(description)

price = soup.find(class_="product-normal-price").text
print(price)
