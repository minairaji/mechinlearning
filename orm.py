import requests
from bs4 import BeautifulSoup
import sys
url = "https://nerkhara.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}
sys.stdout.reconfigure(encoding="utf-8")

response = requests.get(url, headers=headers, timeout=15)

soup = BeautifulSoup(response.text, "html.parser")

# جستجوی متن مربوط به دلار
dollar = soup.find(string=lambda text: text and "دلار آزاد" in text)

if dollar:
    print("اطلاعات دلار پیدا شد:", dollar.parent.parent.get_text(" ", strip=True))
else:
    print("قیمت دلار پیدا نشد")