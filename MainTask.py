import requests
from bs4 import BeautifulSoup
import pandas as pd

output = []

def scrap(url):
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0: Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

  r = requests.get(url, headers=headers)   

  if r.status_code != 404:
    try:
      s = BeautifulSoup(r.content, features="lxml")

      pt = s.select("#productTitle")[0].get_text().strip()
      price = s.select(".a-color-price")[1].get_text().strip()[12:20]
      product_details = s.select(".normal, .a-expander-partial-collapse-content")
      pdetails = []
      for detail in product_details:
        pdetails.append(detail.get_text())
      image = s.select("#imgBlkFront")[0].get_attribute_list('src')[0]

      dic = {}
      dic['Product Title'] = pt
      dic["Product image"] = f"{image}"
      dic["Product Price"] = price
      dic["Product Details"] = f'{pdetails}'

      output.append(dic)

    except Exception as e:
      pass
  else: 
    print(url, "not available")

file = pd.read_csv("AmazonScraping.csv")

for row in range(0, 1000):
  country = file["country"][row]
  asin = file["Asin"][row]
  url = f"https://www.amazon.{country}/dp/{asin}"
  if url.endswith('X'):
    scrap(url)

print(output)

file1 = open('Output.json', 'w')

for element in output:
    file1.writelines(str(element))

file1.close()