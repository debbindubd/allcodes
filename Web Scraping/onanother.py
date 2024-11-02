from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

# Set up Selenium with Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL of the website to scrape
url = "https://www.daraz.com.bd/catalog/?spm=a2a0e.tm80335411.search.2.735279e050utNz&q=headphone&_keyori=ss&clickTrackInfo=textId--8253716290076390876__abId--None__pvid--d9c2db1e-9c08-4db3-b115-a203c0f89c02__matchType--1__abGroup--None__srcQuery--headphone__spellQuery--headphone__ntType--nt-common&from=suggest_normal&sugg=headphone_0_1"

# Open the URL
driver.get(url)
time.sleep(3)  # Allow time for the page to fully load

# Define the XPath to the product container
xpath = "/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]"

# Get inner HTML of the product container
element = driver.find_element(By.XPATH, xpath)
html_content = element.get_attribute("innerHTML")

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Prepare lists to store product details
product_names = []
prices = []
sold_counts = []
ratings = []
image_urls = []

# Find all product elements
products = soup.find_all("div", class_="Bm3ON")

# Loop through each product to extract details
for product in products:
    # Extract product name
    name_tag = product.select_one("div.RfADt a")
    product_name = name_tag.get("title") if name_tag else "N/A"
    
    # Extract product price
    price_tag = product.select_one("div.aBrP0 span.ooOxS")
    price = price_tag.text if price_tag else "N/A"
    
    # Extract number of items sold
    sold_tag = product.select_one("div._6uN7R span._1cEkb")
    sold_count = sold_tag.text.strip() if sold_tag else "N/A"
    
    # Extract product rating and number of reviews
    rating_tag = product.select_one("div.mdmmT._32vUv")
    rating = rating_tag.text.strip() if rating_tag else "N/A"
    
    # Extract image URL
    image_tag = product.select_one("div.picture-wrapper img")
    image_url = image_tag["src"] if image_tag else "N/A"
    
    # Append to lists
    product_names.append(product_name)
    prices.append(price)
    sold_counts.append(sold_count)
    ratings.append(rating)
    image_urls.append(image_url)

# Close the browser
driver.quit()

# Create a DataFrame with the extracted data
df = pd.DataFrame({
    "Product Name": product_names,
    "Price": prices,
    "Sold": sold_counts,
    "Rating": ratings,
    "Image URL": image_urls
})

# Display the first few entries of the DataFrame
print(df.head())

# Optionally, save to a CSV file
df.to_csv("products.csv", index=False)
