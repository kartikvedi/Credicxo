1. Read the csv file 
2. Fetch country code and ASIN
3. For every country & ASIN, frame a URL and make call for scrap() function
4. scrap() function make a GET request to the URL, with headers, used to ByPass Restrictions using User-Agent
5. Then scrap using BeautifulSoup & lxml parser library
6. Extracting Product Title, Product image URL, Product price, Product details
7. Create a dictionary of the product attributes
8. Append all the dictionaries into a list
9. Write the list into a json file

Google Colab link for the code:

https://colab.research.google.com/drive/18sPZdMDkXLtbBKYqGRnHt63EOCcZpM4u?usp=sharing
