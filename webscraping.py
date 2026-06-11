import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(response.text , "html.parser")

book_data= []
book_details = soup.find_all("div" , class_ = "quote")
for content in book_details:
 details = content.find("span" , class_ = "text").text
 auther = content.find("span")
 author_name = content.find("small" , class_ = "author").text
 print(f"Description:{details}")
 print(f"Author:{author_name}")
 book_data.append([details , author_name])
 print(book_data)

with open("books.csv", "w", newline="") as file:
    data = csv.writer(file)
    data.writerow(["decription" , "author"])
    data.writerows(book_data)