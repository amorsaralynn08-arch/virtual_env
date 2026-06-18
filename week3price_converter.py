import requests
from bs4 import BeautifulSoup
import pandas as pd




url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text , "html.parser")
book_price = []
allprice = soup.find_all("article" , class_ = "product_pod")

url_api = "https://v6.exchangerate-api.com/v6/8b8e32a812cc77afe5bca4f7/latest/GBP"
response_2 = requests.get(url_api)
data = response_2.json()
rate = data["conversion_rates"]["KES"]
    #  print(rate)

     
for content in allprice:
     price = content.find("p", class_ = "price_color").text
     title = content.h3.a["title"]
     new_price = float(price.replace("Â£" , ""))
     price_kes = int(new_price * rate)
     book_price.append({
          "title" : title,
          "price in Pounds is Pounds" : new_price,
          "price in KSH is Ksh": price_kes  
     })
    #  book_price.append({
    #       "title" :title,
    #       "price" : new_price
    #  })
    
    #  print(book_price)

     
df = pd.DataFrame(book_price)
print(df)
file_name = "scrapped_prices.xlsx"
df.to_excel(file_name, index=False)

