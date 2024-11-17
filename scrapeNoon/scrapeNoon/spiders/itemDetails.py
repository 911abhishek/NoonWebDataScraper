import scrapy
import re
from datetime import datetime
import subprocess

class ItemDetailsSpider(scrapy.Spider):
    name = "itemDetails"
    allowed_domains = ["noon.com"]
    current_page = 1
    item_count = 1
    max_pages = 200
    custom_settings = {
        'FEED_FORMAT': 'csv', 
        'FEED_URI': 'Extractions.csv',  
    }
    def start_requests(self):
        yield scrapy.Request(
            url="https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/",
            callback=self.parse
        )

    def parse(self, response):
        # Locate the product blocks
        dataBlock = response.xpath("//div[contains(@class, 'sc-57fe1f38-0 eSrvHE')]")
        for rank, data in enumerate(dataBlock, start=1):
            self.item_count += 1
            # Extract product link
            product_link = data.xpath(".//a/@href").get()
            product_title = data.xpath(".//div[@data-qa='product-name']/@title").get()
            product_id = data.xpath(".//a/@id").get()
            sku_code = re.sub(r'^productBox-', '', product_id) if product_id else None
            #extract ratings
            #<div class="sc-9cb63f72-2 dGLdNc">5.0</div>
            average_rating = data.xpath(".//div[contains(@class, 'sc-9cb63f72-2 dGLdNc')]/text()").get()
            # <span class="sc-9cb63f72-5 DkxLK">58</span>
            rating_count = data.xpath('.//span[contains(@class, "sc-9cb63f72-5 DkxLK")]/text()').get()
            #check sponsered or not
            # <div class="sc-d96389d1-24 kXouJu">Sponsored</div>
            check_sponsered = data.xpath(".//div[contains(@class, 'sc-d96389d1-24 kXouJu')]/text()").get()
            if check_sponsered == "Sponsored":
                sponser = "Y"
            else:
                sponser = "N"
            #check price and old price
            # <strong class="amount">69.90</strong>
            price = data.xpath(".//strong[contains(@class, 'amount')]/text()").get()
            # <span class="oldPrice"> <!-- -->69.95</span>
            old_price = data.xpath(".//span[contains(@class, 'oldPrice')]/text()[normalize-space()]").get(default="Not Available")

            #express check
            # <img src="https://f.nooncdn.com/s/app/com/noon/images/fulfilment_express_v3-en.svg" alt="noon-express" class="sc-92fbb12b-1 hnMlkQ" width="auto" height="18px"> if this is present in the data express=Y else N i am attaching my code also
            express = data.xpath(".//img[contains(@class, 'sc-92fbb12b-1 hnMlkQ')]").get()
            express_staus = "Y" if express else "N"
            #extract date
            date_scraped = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if product_link:
                
                
                # Follow the product link to get the brand name
                yield response.follow(
                    product_link,
                    self.parse_product_details,
                    meta={
                        "Link": response.urljoin(product_link),
                        "Name": product_title,
                        "SKU": sku_code,
                        "Average Rating": average_rating,
                        "Rating Count": rating_count,
                        "Sponsered" : sponser,
                        "Price" : price,
                        "Old Price":old_price,
                        "Express":express_staus,
                        "Rank": rank,
                        "Date" :date_scraped
                    }
                )
            
        
        if self.item_count <= 300:
            self.current_page += 1
            next_page_url = f"https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?isCarouselView=false&limit=50&page={self.current_page}&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc"
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_product_details(self, response):
        # Extract the brand name from the product page
        brand_name = response.xpath(
            "//div[contains(@data-qa, 'pdp-brand')]/text()"
        ).get()
        
        # Yield the data including the brand name
        yield {
            "Date & Time": response.meta['Date'],
            "SKU": response.meta["SKU"],
            "Name": response.meta["Name"],
            "Brand": brand_name.strip() if brand_name else None,
            "Average Rating":response.meta['Average Rating'],
            "Rating Count":response.meta['Rating Count'],
            "Sponsered":response.meta['Sponsered'],
            "Price":response.meta['Price'],
            "Sales Price": response.meta['Old Price'],
            "Express": response.meta['Express'],
            "Rank": response.meta['Rank'],
            "Link": response.meta["Link"],
            
           }


  
