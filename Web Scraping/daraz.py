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

# Define the XPath to the product container and pagination elements
product_xpath = "/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]"
next_page_xpath = "//li[contains(@title, 'Next Page')]/button"  # Update with the XPath for the next button

# Prepare lists to store all products' details
product_names = []
prices = []
sold_counts = []
ratings = []
image_urls = []

# Loop through all pages (up to 102 pages or until no next page)
page = 1  # Start from the first page
while page <= 102:
    # Get the product container's inner HTML on the current page
    element = driver.find_element(By.XPATH, product_xpath)
    html_content = element.get_attribute("innerHTML")
    
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Find all product elements and extract details as before
    products = soup.find_all("div", class_="Bm3ON")
    
    for product in products:
        name_tag = product.select_one("div.RfADt a")
        product_name = name_tag.get("title") if name_tag else "N/A"
        
        price_tag = product.select_one("div.aBrP0 span.ooOxS")
        price = price_tag.text if price_tag else "N/A"
        
        sold_tag = product.select_one("div._6uN7R span._1cEkb")
        sold_count = sold_tag.text.strip() if sold_tag else "N/A"
        
        rating_tag = product.select_one("div.mdmmT._32vUv")
        rating = rating_tag.text.strip() if rating_tag else "N/A"
        
        image_tag = product.select_one("div.picture-wrapper img")
        image_url = image_tag["src"] if image_tag else "N/A"
        
        product_names.append(product_name)
        prices.append(price)
        sold_counts.append(sold_count)
        ratings.append(rating)
        image_urls.append(image_url)

    # Try to navigate to the next page
    try:
        next_button = driver.find_element(By.XPATH, next_page_xpath)
        if "disabled" in next_button.get_attribute("class"):
            print(f"No more pages to navigate after page {page}. Ending scrape.")
            break
        
        next_button.click()
        time.sleep(3)  # Wait for the next page to load
        page += 1  # Increment the page counter
    except Exception as e:
        print(f"Could not find next button on page {page}. Ending scrape. Error: {e}")
        break

# Close the browser
driver.quit()

# Create a DataFrame with the accumulated data
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
df.to_csv("all_products.csv", index=False)
