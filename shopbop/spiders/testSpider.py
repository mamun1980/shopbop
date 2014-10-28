import scrapy
# from shopbop.SeleniumSpider import SeleniumSpider
from shopbop.items import *
from scrapy.contrib.linkextractors import LinkExtractor

class MySpider(scrapy.Spider):
    name = "test"
    items = []
    allowed_domains = ["www.shopbop.com"]
    start_urls = ["http://www.shopbop.com/bags/br/v=1/2534374302024667.htm"]

    def parse(self, response):
        import pdb; pdb.set_trace();
        urls = response.xpath('//*[@id="leftNavigation"]/ul/li[2]/a/@href').extract()
        # links = LinkExtractor(restrict_xpaths=('//*[@id="leftNavigation"]/ul'))
        for url in links:
            return scrapy.Request(url, callback=self.get_product_list)

    def get_product_list(self, response):
        import pdb; pdb.set_trace();
        product_list = response.xpath('//*[@id="product-container"]/li"]')


    def get_product(self, response):
        # import pdb; pdb.set_trace();
        product = Product()
        product_class = ProductClass()
        product_class['name'] = 'Clothing'
        product_class['slug'] = 'clothing'
        product_class['requires_shipping'] = True
        product_class['track_stock'] = True
        product['product_class'] = product_class

        related_products = []
        rp_id_links = response.xpath('//*[@id="similarities"]/li/div/a')
        for rp_id_li in rp_id_links:
            related_product = RelatedProduct()
            url = rp_id_li.xpath("@href").extract()[0]
            rp_id = url.split("=")[-1]
            related_product['releted_product_id'] = rp_id
            related_products.append(related_product)
        product['related_products'] = related_products
        
        product_cat = ProductCategory()
        cat_name = 'Activewear'
        product_cat['name'] = cat_name
        product['product_category'] = product_cat

        product_image = ProductImage()
        product_image['shopbop_thumb_url'] = response.xpath('//*[@id="slot-1"]/@src').extract()[0]
        big_image = response.xpath('//*[@id="productZoomImage"]/img')
        img_url = big_image.xpath('@src').extract()
        product_image['shopbop_image_url'] = img_url[0]
        product_image['shopbop_big_image_url'] = img_url[0].replace("_336x596","")
        product_image['original'] = 'images/products/t-shirt2.png'
        product['image'] = product_image

        product_sizes = []
        sizes = response.xpath('//*[@id="sizes"]/span')
        for size in sizes:
            product_size = ProductSize()
            product_size['size'] = size.xpath('@data-selectedsize').extract()[0]
            product_sizes.append(product_size)
        product['product_sizes'] = product_sizes

        product_colors = []
        colors = response.xpath('//*[@id="swatches"]/img')
        for color in colors:
            pcolor = color.xpath('@class').extract()[0]
            color_classes = pcolor.split(" ")
            if not 'hide' == color_classes:
                product_color = ProductColor()
                product_color['color'] = color.xpath('@title').extract()[0]
                product_color['shopbop_color_thumnail_url'] = color.xpath('@src').extract()[0]
                product_colors.append(product_color)
        product['product_colors'] = product_colors

        sizenfit = SizeNFit()
        allfits = response.xpath('//*[@id="sizeFitContainer"]/node()').extract()
        fittext = ''
        for allfit in allfits:
            fittext = fittext + allfit.strip()
        sizenfit['fit'] = fittext
        product['size_n_fit'] = sizenfit

        
        path_product_info = response.xpath('//*[@id="product-information"]')
        path_product_price = response.xpath('//*[@id="productPrices"]')

        product['product_id'] = response.xpath('//*[@id="productId"]/text()').extract()[0].strip()
        product['product_sku'] = path_product_info.xpath('//*[@id="productCode"]/@content').extract()[0].strip()
        product['brand_name'] = path_product_info.xpath('a/h1/text()').extract()[0].strip()
        product['title'] = path_product_info.xpath('//*[@id="product-information"]/p/text()').extract()[0].strip()
        product['description'] = response.xpath('//*[@id="detailsAccordion"]/div[@class="content"]/text()').extract()[0].strip()
        
        price = path_product_price.xpath('meta[1]/@content').extract()[0].strip()
        product['price'] = price
        product['price_new'] = float(price[1:].replace(",",""))/2
        product['product_currency'] = path_product_price.xpath('meta[2]/@content').extract()[0].strip()

        return product