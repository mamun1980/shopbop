import scrapy
# from shopbop.SeleniumSpider import SeleniumSpider
from shopbop.items import *
from scrapy.contrib.linkextractors import LinkExtractor
# from scrapy.selector import HtmlXPathSelector
# from selenium import selenium


class ProductSpider(scrapy.Spider):
    name = "shopbop_product"
    allowed_domains = ["shopbop.com"]
    start_urls = [
        "http://www.shopbop.com/pajama-top-chemise-bop-basics/vp/v=1/845524441926315.htm?folderID=2534374302049464&fm=other-shopbysize&colorId=12867"
    ]

    def parse(self, response):
        # import pdb; pdb.set_trace()
        product_type = ProductType()
        product_category = ProductCategory()
        product_image = ProductImage()
        product_sizes = []
        product_colors = []
        sizenfit = SizeNFit()
        product = Product()

        product_type['name'] = 'Activewear'
        product['product_type'] = product_type
        
        product_category['name'] =  'Activewear'
        product_category['relative_to'] =  'Clothing'
        product['product_category'] = product_category

        product_image['shopbop_thumb_url'] = response.xpath('//*[@id="slot-1"]/@src').extract()
        # image_js = response.xpath('//*[@id="productZoomImage"]/@href').extract()
        product_image['shopbop_big_image_url'] = 'http://g-ecx.images-amazon.com/images/G/01/Shopbop/p/pcs/products/bopaa/bopaa4010912867/bopaa4010912867_q1_1-1.jpg'

        sizes = response.xpath('//*[@id="sizes"]/span')
        for size in sizes:
            product_size = ProductSize()
            product_size['size'] = size.xpath('@data-selectedsize').extract()[0]
            product_sizes.append(product_size)
        product['product_sizes'] = product_sizes

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

        fits = response.xpath('//*[@id="fitGuidance"]/node()').extract()
        sizenfit['measurement'] = fits
        model_measurements = response.xpath('//*[@id="modelSize"]/node()').extract()
        sizenfit['model_measurement'] = " ".join(model_measurements)
        size_n_charts = response.xpath('//*[@id="sizeFitContainer"]/table/node()').extract()
        sizenfit['size_table'] = " ".join(size_n_charts)
        size_n_char_descriptions = response.xpath('//*[@id="sizeFitContainer"]/p/node()').extract()
        sizenfit['description'] = " ".join(size_n_char_descriptions)
        # product['size_n_fit'] = sizenfit

        
        path_product_info = response.xpath('//*[@id="product-information"]')
        path_product_price = response.xpath('//*[@id="productPrices"]')
        path_product_color = response.xpath('//*[@id="swatches"]')

        product['product_id'] = response.xpath('//*[@id="productId"]/text()').extract()[0].strip()
        product['product_sku'] = path_product_info.xpath('//*[@id="productCode"]/@content').extract()[0].strip()
        product['brand_name'] = path_product_info.xpath('a/h1/text()').extract()[0].strip()
        product['brand_name'] = path_product_info.xpath('//*[@id="product-information"]/p/text()').extract()[0].strip()
        product['designer'] = response.xpath('//*[@id="designerContainer"]/text()').extract()[0].strip()
        product['description'] = response.xpath('//*[@id="detailsAccordion"]/div[@class="content"]/text()').extract()[0]
        
        price = path_product_price.xpath('meta[1]/@content').extract()[0].strip()
        product['price'] = price
        product['price_new'] = float(price[1:])/2
        product['product_currency'] = path_product_price.xpath('meta[2]/@content').extract()[0].strip()

        # product_sizes = []
        # for path_size in path_product_info.xpath('//*[@id="sizes"]/span'):
        #   product_size = ProductSize()
        #   product_size['size'] = path_size.xpath('text()')[0].extract()
        #   product_sizes.append(product_size)

        # product['product_sizes'] = product_sizes

        # product_colors = []
        # color_order = 0
        # color_selected = True
        # for path_color in path_product_color.xpath('img'):
        #   product_color = ProductColor()
        #   color = path_color.xpath('@title')[0].extract().strip()
        #   color_url = path_color.xpath('@src')[0].extract()
        #   product_color['color'] = color
        #   product_color['color_url'] = color_url
        #   product_color['order'] = color_order
        #   color_order += 1
        #   product_color['selected'] = color_selected
        #   color_selected = False
        #   product_colors.append(product_color)

        # product['product_colors'] = product_colors
        import pdb; pdb.set_trace()
        return product


class ProductTypeSpider(scrapy.Spider):
    name = "shopbop_product_type"
    allowed_domains = ["shopbop.com"]
    start_urls = [
        "http://www.shopbop.com/"
    ]

    def parse(self, response):
        product_types = []
        for sel in response.xpath('//*[@id="navList"]/li'):
            title = sel.xpath('a[1]/text()').extract()
            product_type = ProductType()
            product_type['name'] = title[0].strip()
            product_types.append(product_type)

        return product_types


class ProductCategorySpider(scrapy.Spider):
    name = "shopbop_product_category"
    allowed_domains = ["shopbop.com"]
    start_urls = [
        "http://www.shopbop.com/"
    ]

    def parse(self, response):
        # import pdb; pdb.set_trace()
        product_categories = []
        for sel in response.xpath('//*[@id="navList"]/li'):
            title = sel.xpath('a[1]/text()').extract()
            prod_cat = ProductCategory()
            prod_cat['name'] = title[0].strip()
            product_categories.append(prod_cat)
            sub_cats = sel.xpath('ul/li')
            for sub_cat in sub_cats:
                name = sub_cat.xpath('a/text()').extract()
                description = sub_cat.xpath('a/@data-cs-name').extract()
                prod_cat2 = ProductCategory()
                prod_cat2['name'] = name[0].strip()
                prod_cat2['description'] = description[0].strip()
                prod_cat2['relative_to'] = title[0].strip()
                product_categories.append(prod_cat2)

        return product_categories
