import pandas as pd
from bs4 import BeautifulSoup

# Sample HTML code for one product card
html_code = """
<div class="Bm3ON" data-qa-locator="product-item" data-tracking="product-card" data-sku-simple="215349589_BD-1836425817" data-item-id="215349589" data-listno="0" data-utlogmap="{&quot;listno&quot;:0,&quot;pageIndex&quot;:1,&quot;pvid&quot;:&quot;a1a3f4caf5c7be2e200fb5ff25e5f254&quot;,&quot;query&quot;:&quot;headphone&quot;,&quot;style&quot;:&quot;wf&quot;,&quot;x_item_ids&quot;:&quot;215349589&quot;,&quot;x_object_id&quot;:&quot;215349589&quot;,&quot;x_object_type&quot;:&quot;item&quot;}" data-aplus-ae="x1_2da5fd1" data-spm-anchor-id="a2a0e.searchlist.list.i0.49e24c07vTVXaC" data-aplus-clk="x1_2da5fd1">
    <div class="Ms6aG">
        <div class="qmXQo">
            <div class="ICdUp">
                <div class="_95X4G">
                    <a href="//www.daraz.com.bd/products/vivo-in-year-yearphone-is-the-best-sound-quality-white-with-free-one-emphasizing-value-i215349589.html">
                        <div class="picture-wrapper jBwCF ">
                            <img type="product" alt="Vivo In Year Yearphone is the best sound quality-white with free one - Emphasizing Value" src="https://img.drz.lazcdn.com/static/bd/p/ea974ce2b124f6d82b61a45ff60e4ed8.jpg_200x200q90.jpg_.webp" style="object-fit: fill;">
                        </div>
                    </a>
                </div>
            </div>
            <div class="buTCk">
                <div class="ajfs+"></div>
                <div class="RfADt">
                    <a href="//www.daraz.com.bd/products/vivo-in-year-yearphone-is-the-best-sound-quality-white-with-free-one-emphasizing-value-i215349589.html" title="Vivo In Year Yearphone is the best sound quality-white with free one - Emphasizing Value">
                        <i class="ic-dynamic-badge ic-dynamic-badge-120425 ic-dynamic-group-3" style="background-image: url(&quot;https://img.lazcdn.com/us/lazgcp/81b63c8e-2f77-474b-8b78-1a3543573d0f_ALL-134-52.png&quot;); width: 41.2308px; height: 16px; background-size: 100% 100%; background-repeat: no-repeat;"></i>
                        Vivo In Year Yearphone is the best sound quality-white with free one - Emphasizing Value
                    </a>
                </div>
                <div class="aBrP0" data-spm-anchor-id="a2a0e.searchlist.list.i40.49e24c07vTVXaC">
                    <span class="ooOxS">৳ 104</span>
                </div>
                <div class="WNoq3"></div>
                <div class="_6uN7R">
                    <span class="_1cEkb">
                        <span>5.3K sold</span>
                        <span class="brHcE"></span>
                    </span>
                    <div class="mdmmT *32vUv">
                        <i class="*9-ogB Dy1nx"></i>
                        <i class="_9-ogB Dy1nx"></i>
                        <i class="_9-ogB Dy1nx"></i>
                        <i class="_9-ogB Dy1nx"></i>
                        <i class="_9-ogB W1iJ5"></i>
                        <span class="qzqFw">(931)</span>
                    </div>
                    <span class="oa6ri "></span>
                </div>
            </div>
        </div>
    </div>
</div>
"""

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_code, 'html.parser')

# Extract the relevant data
product_name = soup.find('a', {'class': 'RfADt'}).text.strip()
product_price = soup.find('span', {'class': 'ooOxS'}).text.strip()
product_rating = soup.find('span', {'class': 'qzqFw'}).text.strip()
product_sales = soup.find('span', {'class': '_1cEkb'}).find('span').text.strip()
product_image = soup.find('img', {'type': 'product'})['src']

# Create a Pandas DataFrame
data = {
    'Product Name': [product_name],
    'Price': [product_price],
    'Rating': [product_rating],
    'Sales': [product_sales],
    'Image URL': [product_image]
}
df = pd.DataFrame(data)

print(df)